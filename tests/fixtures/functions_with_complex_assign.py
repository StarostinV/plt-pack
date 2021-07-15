from inspect import getsource

from plt_pack.parse import FuncDict

k, v, arg, c, x, y, z, d = [None] * 8
real_global = 1


def func_with_complex_assign(a: int,
                             *args,
                             b: float = 2,
                             **kwargs):
    for k, v in kwargs.items():
        print(k, v)

    for i, arg in enumerate(args):
        print(arg, i + real_global)

    a, b, c, *d = _return_tuple(a, b=b)

    return a, b, c, d


def _return_tuple(a: int, *, b: float = 2):
    x, y, z = a, b, a * b
    return x, y, z, 1, 1, 1


FUNC_WITH_COMPLEX_ASSIGN = FuncDict(
    entry_func='func_with_complex_assign',
    functions={
        'func_with_complex_assign': getsource(func_with_complex_assign),
        '_return_tuple': getsource(_return_tuple),
    },
    modules=(),
    import_lines=(),
    module_versions={},
    global_vars=dict(real_global=real_global),
)
