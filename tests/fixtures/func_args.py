import pytest
import numpy as np


@pytest.fixture
def func_args():
    args = (np.arange(10), 1, 'arg')
    kwargs = {'arg1': 1, 'arg2': np.arange(10).astype(np.float)}

    return args, kwargs
