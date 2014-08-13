"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"

checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.

checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.

"""

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.code import CheckiORefereeCode
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS


from checkio import api

from checkio.referees.io import CheckiOReferee

REQ = 'req'
REFEREE = 'referee'


class CheckiORefereeCodeScore(CheckiORefereeCode):


    def check_current_test(self, data):

        test_result = data["result"]
        best_gifts, bag_count, gift_count = test_result
        self.current_test.update(test_result)

        self.current_test["result"] = bool(best_gifts)
        self.current_test["result_addon"] = "'You do won {:n} best gifts from {:n} bags with {:,} gifts!".format(
            best_gifts, bag_count, gift_count)

        api.request_write_ext(self.current_test)

        if not self.current_test["result"]:
            return api.fail(self.current_step, self.get_current_test_fullname())
        api.success(best_gifts)



api.add_listener(
    ON_CONNECT,
    CheckiORefereeCodeScore(
        tests=TESTS,
        # checker=None,  # checkers.float.comparison(2)
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
