import pytest

from pathlib import Path

import numpy as np

from plt_pack import PltProject

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


# TODO: allow some monkeypatch / test options to make this test possible
@pytest.mark.skip
def test_auto_save_not_working(tmpdir, functions_with_func_dicts, monkeypatch):
    args = (np.arange(10), 1, 'arg')
    kwargs = {'arg1': 1, 'arg2': np.arange(10).astype(np.float)}

    plt_project = PltProject(Path(tmpdir))
    plt_project._TEST = True

    func, func_dict = functions_with_func_dicts

    @plt_project.auto_save(name=func_dict.entry_func, rewrite=True)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)

    monkeypatch.setattr(wrapper_func, '__module__', func.__module__)
    monkeypatch.setattr(wrapper_func, '__name__', func.__name__)

    assert wrapper_func.__name__ == func_dict.entry_func

    wrapper_func()

    assert func_dict.entry_func == plt_project.list_files()[0]

    file = plt_project.load_file(func_dict.entry_func)
    compare_func_dicts(func_dict, file, args, kwargs)
