init_code = """
if not "choose_good_gift" in USER_GLOBAL:
    raise NotImplementedError("Didn't find 'choose_good_gift'")
choose_good_gift = USER_GLOBAL['choose_good_gift']
"""

py3_code = """

from random import random, randint, uniform


scale = (random() + random()) ** randint(0, 1024)

standings = gift_count = best_gifts = 0
for i in range(2000):
    gifts_in_bag = randint(10, 1000)
    gift_count += gifts_in_bag

    gifts = []
    selected_gift = None
    for i in range(gifts_in_bag):
        new_gift = uniform(0., scale)
        gifts.append(new_gift)
        decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
        if decision:
            selected_gift = gift
            gifts.extend([uniform(0., scale) for _ in range(gifts_in_bag - i - 1)])
            break
    if gift_value is None:
        priority = len(gifts_in_bag)
    else:
        priority = sum(gift_value < x for x in gifts)
    standings += priority
    best_gifts += not priority
return best_gifts, bag_count, gift_count

RET['code_result'] = best_gifts, bag_count, gift_count
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
