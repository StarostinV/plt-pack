from inspect import getsource

from plt_pack.parse import FuncDict


def func_with_recursion(n: int):
    if n <= 1:
        return 1
    return n * func_with_recursion(n - 1)


def func_with_recursion_2(n: int):
    if n <= 1:
        return 1
    if n % 2:
        return n * func_with_recursion(n - 2)
    else:
        return n * func_with_recursion_2(n - 1)


FUNC_WITH_RECURSION_DICT = FuncDict(
    entry_func='func_with_recursion',
    functions={'func_with_recursion': getsource(func_with_recursion)},
    modules=(),
    import_lines=(),
    module_versions={},
    global_vars={},
)


FUNC_WITH_RECURSION_2_DICT = FuncDict(
    entry_func='func_with_recursion_2',
    functions={
        'func_with_recursion': getsource(func_with_recursion),
        'func_with_recursion_2': getsource(func_with_recursion_2),
    },
    modules=(),
    import_lines=(),
    module_versions={},
    global_vars={},
)
