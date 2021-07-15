from plt_pack.parse import parse_function
from tests.helpers import compare_func_dicts


def test_func_dicts(functions_with_func_dicts):
    func, func_dict = functions_with_func_dicts
    res = parse_function(func)
    compare_func_dicts(func_dict, res)
