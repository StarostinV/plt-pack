from tests.helpers import compare_func_dicts, check_auto_save


# cannot stack fixtures together: https://github.com/pytest-dev/pytest/issues/349
def test_auto_save_1(func_with_plt_project1, capsys):
    plt_project, func, func_dict = func_with_plt_project1
    func()
    out, err = capsys.readouterr()
    assert out == '()\n4.5\n'
    assert err == ''
    check_auto_save(plt_project, func_dict)
    func(11, 'arg')
    out, err = capsys.readouterr()
    assert out == "('arg',)\n5.0\n"
    assert err == ''
    check_auto_save(plt_project, func_dict, target_args=(11, 'arg'))


def test_auto_save_2(func_with_plt_project2):
    plt_project, func, func_dict = func_with_plt_project2
    func()
    check_auto_save(plt_project, func_dict)


def test_auto_save(plt_project, functions_with_func_dicts, func_args):
    args, kwargs = func_args
    func, func_dict = functions_with_func_dicts
    plt_project._TEST = True

    wrapped_func = plt_project.auto_save(name=func_dict.entry_func, rewrite=True)(func)

    wrapped_func(*args, **kwargs)

    assert func_dict.entry_func == plt_project.list_files()[0]

    file = plt_project.load_file(func_dict.entry_func)
    compare_func_dicts(func_dict, file, args, kwargs)


def test_multiple_auto_save_file_list(plt_project, functions_with_func_dicts, func_args, freeze_time):
    args, kwargs = func_args
    func, func_dict = functions_with_func_dicts
    plt_project._TEST = True
    date_fmt = '%H'
    expected_file_list = []
    name = func_dict.entry_func

    wrapped_func = plt_project.auto_save(
        name=func_dict.entry_func,
        rewrite=False,
        datefmt=date_fmt,
    )(func)

    wrapped_func(*args, **kwargs)

    expected_file_list.append(f'{name}_{freeze_time.strftime(date_fmt)}')

    assert set(expected_file_list) == set(plt_project.list_files())

    with plt_project(name='new_name', rewrite=True, suffix='some_suffix'):
        wrapped_func(*args, **kwargs)

    expected_file_list.append('new_name_some_suffix')

    assert set(expected_file_list) == set(plt_project.list_files())

    with plt_project(suffix='other_suffix'):
        wrapped_func(*args, **kwargs)

    expected_file_list.append(f'{name}_other_suffix_{freeze_time.strftime(date_fmt)}')

    assert set(expected_file_list) == set(plt_project.list_files())

    with plt_project(save_plt=False):
        wrapped_func(*args, **kwargs)

    assert set(expected_file_list) == set(plt_project.list_files())

    for file_name in expected_file_list:
        file = plt_project.load_file(file_name)
        compare_func_dicts(func_dict, file, args, kwargs)


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
