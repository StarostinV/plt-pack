import pytest

from plt_pack.parse import FuncDict
from inspect import getsource
from typing import Tuple
import matplotlib as mpl
from matplotlib.patches import Rectangle
from matplotlib.pyplot import show as plt_show
from matplotlib import pyplot as plt


def func_with_import1(args: Tuple[int, float] = (10, 1)):
    import numpy as np
    import matplotlib

    n, a = args

    matplotlib.rcParams.update({'font.size': 12})

    x = np.arange(n)
    y = np.sin(x * a)

    plt.plot(x, y)
    plt.gca().add_patch(Rectangle((0, 0), 1, 1))
    plt.show()


def func_with_import2(n: int = 10, a: float = 1.):
    from matplotlib.pyplot import plot, gca
    import numpy as np

    def plot_rectangle(ax):
        ax.add_patch(Rectangle((0, 0), 1, 1))

    mpl.rcParams.update({'font.size': 12})

    x = np.arange(n)
    y = np.sin(x * a)

    plot(x, y)
    plot_rectangle(gca())
    func_with_import1((n, a))
    plt_show()


FUNC_WITH_IMPORT1_DICT = FuncDict(
    entry_func='func_with_import1',
    functions={'func_with_import1': getsource(func_with_import1)},
    modules=('numpy', 'matplotlib', 'typing'),
    import_lines=(
        'import matplotlib.pyplot as plt',
        'from typing import Tuple',
        'from matplotlib.patches import Rectangle',
    ),
    module_versions={},
    global_vars={},
)

FUNC_WITH_IMPORT2_DICT = FuncDict(
    entry_func='func_with_import2',
    functions={
        'func_with_import2': getsource(func_with_import2),
        'func_with_import1': getsource(func_with_import1),
    },
    modules=('numpy', 'matplotlib', 'typing'),
    import_lines=(
        'import matplotlib.pyplot as plt',
        'from typing import Tuple',
        'import matplotlib as mpl',
        'from matplotlib.patches import Rectangle',
        'from matplotlib.pyplot import show as plt_show',
    ),
    module_versions={},
    global_vars={},
)
