import numpy as np
from plt_pack.parse import parse_function, FuncDict


def test_func_dicts(functions_with_func_dicts):
    func, func_dict = functions_with_func_dicts
    res = parse_function(func)
    compare_func_dicts(func_dict, res)


def compare_func_dicts(d1: FuncDict, d2: FuncDict):
    assert set(d1.import_lines) == set(d2.import_lines)
    assert set(d1.modules) == set(d2.modules)
    assert d1.functions == d2.functions
    assert d1.entry_func == d2.entry_func
    assert d1.global_vars == d2.global_vars
