from tests.helpers import compare_func_dicts


def test_register(plt_project, functions_with_func_dicts, func_args):
    args, kwargs = func_args
    func, func_dict = functions_with_func_dicts
    plt_project._TEST = True
    expected_file_list = []
    name = func_dict.entry_func
    wrapped_func = plt_project.register(func)

    wrapped_func(*args, **kwargs)

    assert set(expected_file_list) == set(plt_project.list_files())

    with plt_project(name='func_name', rewrite=True):
        wrapped_func(*args, **kwargs)

    expected_file_list.append('func_name')

    assert set(expected_file_list) == set(plt_project.list_files())

    with plt_project(save_plt=False):
        wrapped_func(*args, **kwargs)

    assert set(expected_file_list) == set(plt_project.list_files())

    with plt_project(suffix='some_suffix', rewrite=True):
        wrapped_func(*args, **kwargs)

    expected_file_list.append(f'{name}_some_suffix')

    assert set(expected_file_list) == set(plt_project.list_files())

    for file_name in expected_file_list:
        file = plt_project.load_file(file_name)
        compare_func_dicts(func_dict, file, args, kwargs)


def test_description(plt_project, functions_with_func_dicts_short):
    func, func_dict = functions_with_func_dicts_short
    plt_project._TEST = True
    wrapped_func = plt_project.register(func)

    with plt_project(name='func_name', rewrite=True, description='Some description'):
        wrapped_func()

    file = plt_project.load_file('func_name')

    compare_func_dicts(func_dict, file, description='Some description')
