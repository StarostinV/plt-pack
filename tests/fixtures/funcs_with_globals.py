from inspect import getsource

import matplotlib.pyplot as plt
import numpy as np

from plt_pack.parse import FuncDict

COLOR = 'red'
x = (np.arange(10)).tolist()
y = (np.arange(10) / 2).tolist()
lw = 2
ls = '--'


def func_with_stated_globals():
    global COLOR, ls


def func_with_globals():
    _plt_xy(y)
    plt.show()


def _plt_xy(y):
    plt.plot(x, y, c=COLOR, lw=lw, ls=ls)


FUNC_WITH_STATED_GLOBALS: FuncDict = FuncDict(
    entry_func='func_with_stated_globals',
    functions={
        'func_with_stated_globals': getsource(func_with_stated_globals),
    },
    modules=(),
    import_lines=(),
    module_versions={},
    global_vars=dict(COLOR=COLOR, ls=ls),
)

FUNC_WITH_GLOBALS_DICT: FuncDict = FuncDict(
    entry_func='func_with_globals',
    functions={
        'func_with_globals': getsource(func_with_globals),
        '_plt_xy': getsource(_plt_xy),
    },
    modules=('matplotlib',),
    import_lines=(
        'import matplotlib.pyplot as plt',
    ),
    module_versions={},
    global_vars=dict(COLOR=COLOR,
                     x=x,
                     y=y,
                     lw=lw,
                     ls=ls),
)


FUNC_WITH_GLOBALS_CODE: str = '''# Imports:
import matplotlib.pyplot as plt

# Global variables:
COLOR = 'red'
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
lw = 2
ls = '--'

# Main function:

def func_with_globals():
    _plt_xy(y)
    plt.show()


# Sub-functions:

def _plt_xy(y):
    plt.plot(x, y, c=COLOR, lw=lw, ls=ls)
'''
