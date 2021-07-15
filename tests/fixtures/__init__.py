import pytest

from .funcs_with_imports import (
    func_with_import1,
    func_with_import2,
    func_with_dependency_in_args,
    FUNC_WITH_IMPORT1_DICT,
    FUNC_WITH_IMPORT2_DICT,
    FUNC_WITH_DEPENDENCY_IN_ARGS,
)

from .funcs_with_globals import (
    func_with_globals,
    FUNC_WITH_GLOBALS_DICT
)


@pytest.fixture(
    params=[
        (func_with_import1, FUNC_WITH_IMPORT1_DICT),
        (func_with_import2, FUNC_WITH_IMPORT2_DICT),
        (func_with_globals, FUNC_WITH_GLOBALS_DICT),
        (func_with_dependency_in_args, FUNC_WITH_DEPENDENCY_IN_ARGS)
    ],
    ids=[
        'func_with_import1',
        'func_with_import2',
        'func_with_globals',
        'func_with_dependency_in_args',
    ]
)
def functions_with_func_dicts(request):
    func, func_dict = request.param
    return func, func_dict
