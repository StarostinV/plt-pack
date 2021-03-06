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
    FUNC_WITH_GLOBALS_DICT,
    func_with_stated_globals,
    FUNC_WITH_STATED_GLOBALS,
    FUNC_WITH_GLOBALS_CODE,
)

from .func_with_many_subfunctions import (
    func_with_many_subfunctions,
    FUNC_WITH_MANY_SUBFUNCTIONS_DICT
)

from .functions_with_complex_assign import (
    func_with_complex_assign,
    FUNC_WITH_COMPLEX_ASSIGN,
)

from .function_with_recursion import (
    func_with_recursion,
    func_with_recursion_2,
    FUNC_WITH_RECURSION_DICT,
    FUNC_WITH_RECURSION_2_DICT,
)

from .plt_project import (
    func_with_plt_project1,
    func_with_plt_project2,
    plt_project,
)

from .functions_from_readme import (
    FUNC_FROM_README_CODE,
)

from .freeze_time import freeze_time

from .func_args import func_args


@pytest.fixture(
    params=[
        (func_with_import1, FUNC_WITH_IMPORT1_DICT),
        (func_with_import2, FUNC_WITH_IMPORT2_DICT),
        (func_with_globals, FUNC_WITH_GLOBALS_DICT),
        (func_with_stated_globals, FUNC_WITH_STATED_GLOBALS),
        (func_with_dependency_in_args, FUNC_WITH_DEPENDENCY_IN_ARGS),
        (func_with_many_subfunctions, FUNC_WITH_MANY_SUBFUNCTIONS_DICT),
        (func_with_complex_assign, FUNC_WITH_COMPLEX_ASSIGN),
        (func_with_recursion, FUNC_WITH_RECURSION_DICT),
        (func_with_recursion_2, FUNC_WITH_RECURSION_2_DICT),
    ],
    ids=[
        'func_with_import1',
        'func_with_import2',
        'func_with_globals',
        'func_with_stated_globals',
        'func_with_dependency_in_args',
        'func_with_many_subfunctions',
        'functions_with_complex_assign',
        'func_with_recursion',
        'func_with_recursion_2',
    ]
)
def functions_with_func_dicts(request):
    func, func_dict = request.param
    return func, func_dict


@pytest.fixture(
    params=[
        (func_with_import1, FUNC_WITH_IMPORT1_DICT),
        (func_with_dependency_in_args, FUNC_WITH_DEPENDENCY_IN_ARGS),
        (func_with_many_subfunctions, FUNC_WITH_MANY_SUBFUNCTIONS_DICT),
    ],
    ids=[
        'func_with_import1',
        'func_with_dependency_in_args',
        'func_with_many_subfunctions',
    ]
)
def functions_with_func_dicts_short(request):
    func, func_dict = request.param
    return func, func_dict


@pytest.fixture(
    params=[
        (FUNC_WITH_GLOBALS_DICT, FUNC_WITH_GLOBALS_CODE),
    ],
    ids=[
        'func_with_globals',
    ]
)
def func_dicts_with_code(request):
    func_dict, func_code = request.param
    return func_dict, func_code


@pytest.fixture
def func_from_readme_code():
    return FUNC_FROM_README_CODE
