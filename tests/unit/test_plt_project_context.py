from plt_pack.project_utils import PltProject


def test_plt_project_context(plt_project: PltProject):
    with plt_project(rewrite=True, suffix='suffix', datefmt='fmt'):
        save_opts = plt_project.get_save_opts()
        assert save_opts.rewrite
        assert save_opts.suffix == 'suffix'
        assert save_opts.datefmt == 'fmt'

    assert plt_project.default_opts == plt_project.get_save_opts()

    with plt_project(suffix='suffix', datefmt='fmt'):
        save_opts = plt_project.get_save_opts(rewrite=True)
        assert save_opts.rewrite
        assert save_opts.suffix == 'suffix'
        assert save_opts.datefmt == 'fmt'

    assert plt_project.default_opts == plt_project.get_save_opts()
