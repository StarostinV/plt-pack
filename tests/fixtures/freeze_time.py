import datetime
import pytest

FAKE_TIME = datetime.datetime(2021, 12, 23, 9, 0, 59)


@pytest.fixture
def freeze_time(monkeypatch) -> datetime.datetime:
    class FrozenDateTime:
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, 'datetime', FrozenDateTime)

    return FAKE_TIME
