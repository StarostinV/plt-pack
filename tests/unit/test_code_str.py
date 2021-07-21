from plt_pack.file import PltFile


def test_code_str(func_dicts_with_code):
    func_dict, func_code = func_dicts_with_code
    file = PltFile(**func_dict)
    assert file.get_code_str() == func_code
