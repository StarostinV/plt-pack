from pathlib import Path

import numpy as np

from plt_pack import save_plt_file, read_plt_file
from tests.helpers import compare_func_dicts


def test_save_read(tmpdir, functions_with_func_dicts):
    args = (np.arange(10), 1, 'arg')
    kwargs = {'arg1': 1, 'arg2': np.arange(10).astype(np.float)}
    path = Path(tmpdir) / 'func.plt'
    func, func_dict = functions_with_func_dicts
    save_plt_file(path, func, *args, **kwargs)
    plt_file = read_plt_file(path)
    compare_func_dicts(func_dict, plt_file, target_args=args, target_kwargs=kwargs)
