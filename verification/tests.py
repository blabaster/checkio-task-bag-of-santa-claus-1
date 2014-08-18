init_code = """
if not "choose_good_gift" in USER_GLOBAL:
    raise NotImplementedError("Didn't find 'choose_good_gift'")
choose_good_gift = USER_GLOBAL['choose_good_gift']
"""

py3_code = """

from random import random, randint, uniform

def priority_post_factum(gifts):
    def accept_gift():
        nonlocal gift_value
        if gift_value is None:
            if idx < len(gifts):
                gift_value = gifts[idx]

    def gift_generator():
        nonlocal idx
        while idx:
            idx -= 1
            yield gifts[idx]

    idx, gift_value = len(gifts), None
    choose_good_gift(idx, gift_generator, accept_gift)
    if gift_value is None:
        return len(gifts)
    else:
        return sum(gift_value < x for x in gifts)

def check_solution(bag_count):
    standings = gift_count = best_gifts = 0
    for i in range(bag_count):
        gifts_in_bag = randint(10, 1000)
        gift_count += gifts_in_bag
        scale = (random() + random()) ** randint(0, 1024)
        priority = priority_post_factum([uniform(0., scale) for _ in range(gifts_in_bag)])
        standings += priority
        best_gifts += not priority
    return best_gifts, bag_count, gift_count

RET['code_result'] = check_solution(2000)
"""

py2_code = """
from random import random, randint, uniform

def priority_post_factum(gifts):
    def do_accept():
        if gift_value[0] is None:
            if idx[0] < len(gifts):
                gift_value[0] = gifts[idx[0]]

    def gift_generator():
        while idx[0]:
            idx[0] -= 1
            yield gifts[idx[0]]

    idx, gift_value = [len(gifts)], [None]
    choose_good_gift(idx[0], gift_generator, do_accept)
    if gift_value[0] is None:
        return len(gifts)
    else:
        return sum(gift_value[0] < x for x in gifts)

def check_solution(bag_count):
    standings = gift_count = best_gifts = 0
    for i in range(bag_count):
        gifts_in_bag = randint(10, 1000)
        gift_count += gifts_in_bag
        scale = (random() + random()) ** randint(0, 1024)
        priority = priority_post_factum([uniform(0., scale) for _ in range(gifts_in_bag)])
        standings += priority
        best_gifts += not priority
    return best_gifts, bag_count, gift_count

RET['code_result'] = check_solution(2000)
"""


TESTS = {
    "One": [
        {
            "test_code": {"python-3": init_code + py3_code, "python-27": init_code + py3_code},
            "show": {"python-3": "", "python-27": ""},
            "answer": ""
        }
    ]
}
