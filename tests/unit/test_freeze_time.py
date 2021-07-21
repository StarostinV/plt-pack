import datetime
from plt_pack.project_utils.save_opts import SaveOpts


def test_freeze_time(freeze_time):
    assert datetime.datetime.now() == freeze_time


def test_save_opts_time_format(freeze_time):
    date_fmt = '%d-%b-%H-%M-%S'
    save_opts = SaveOpts(datefmt=date_fmt)
    assert save_opts.time_str == freeze_time.strftime(date_fmt)
