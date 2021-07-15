import pytest
from pathlib import Path
from inspect import getsource

import numpy as np

from plt_pack import PltProject
from plt_pack.parse import FuncDict


def func_1(a: int = 10, *args):
    res = func_2(a, *args)
    print(res)


def func_2(a: int, *args):
    x = np.arange(a)
    print(args)
    return x.mean()


def wrapper_func(i):
    return f'def func_with_auto_save{i}(a: int = 10, *args):\n    func_{i}(a, *args)\n'


FUNC_1_DICT = FuncDict(
    entry_func='func_with_auto_save1',
    functions={
        'func_with_auto_save1': wrapper_func(1),
        'func_1': getsource(func_1),
        'func_2': getsource(func_2),
    },
    modules=('numpy',),
    import_lines=('import numpy as np',),
    module_versions={},
    global_vars={},
)

FUNC_2_DICT = FuncDict(
    entry_func='func_with_auto_save2',
    functions={
        'func_with_auto_save2': wrapper_func(2),
        'func_2': getsource(func_2),
    },
    modules=('numpy',),
    import_lines=('import numpy as np',),
    module_versions={},
    global_vars={},
)


@pytest.fixture(scope='function')
def plt_project(tmpdir):
    plt_project = PltProject(Path(tmpdir))
    return plt_project


@pytest.fixture
def func_with_plt_project1(plt_project):
    @plt_project.auto_save(name='func_with_auto_save1', rewrite=True)
    def func_with_auto_save1(a: int = 10, *args):
        func_1(a, *args)

    return plt_project, func_with_auto_save1, FUNC_1_DICT


@pytest.fixture
def func_with_plt_project2(plt_project):
    @plt_project.auto_save(name='func_with_auto_save2', rewrite=True)
    def func_with_auto_save2(a: int = 10, *args):
        func_2(a, *args)

    return plt_project, func_with_auto_save2, FUNC_2_DICT
