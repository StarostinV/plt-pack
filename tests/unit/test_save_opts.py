from plt_pack.project_utils.save_opts import SaveOpts


def test_save_opts_dict():
    save_opts = SaveOpts()
    assert len(save_opts) == 0
    assert save_opts.name is None


def test_save_opts_repr():
    assert str(SaveOpts()) == 'SaveOpts()'
    assert str(SaveOpts(rewrite=True)) == 'SaveOpts(rewrite=True)'
    assert str(SaveOpts(rewrite=True, datefmt='%H:%S')) in [
        "SaveOpts(rewrite=True, datefmt='%H:%S')",
        "SaveOpts(datefmt='%H:%S', rewrite=True)"
    ]
