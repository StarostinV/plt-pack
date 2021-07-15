import numpy as np
from plt_pack.parse import FuncDict


def compare_func_dicts(
        target_dict: FuncDict,
        res_dict: FuncDict,
        target_args: tuple = None,
        target_kwargs: dict = None
):
    assert target_dict.functions.keys() == res_dict.functions.keys()
    assert set(target_dict.import_lines) == set(res_dict.import_lines)
    assert set(target_dict.modules) == set(res_dict.modules)
    assert target_dict.entry_func == res_dict.entry_func
    assert target_dict.global_vars == res_dict.global_vars
    assert target_dict.functions == res_dict.functions

    if target_args is not None:
        res_args = [_to_list(v) for v in res_dict.args]
        target_args = [_to_list(v) for v in target_args]
        assert res_args == target_args

    if target_kwargs is not None:
        res_kwargs = {k: _to_list(v) for k, v in res_dict.kwargs.items()}
        target_kwargs = {k: _to_list(v) for k, v in target_kwargs.items()}
        assert res_kwargs == target_kwargs


def _to_list(v):
    if isinstance(v, np.ndarray):
        return v.tolist()
    return v
