from types import FunctionType

from .save_opts import SaveOpts


class RegisteredFunc(object):
    def __init__(self, func: FunctionType, save_opt: SaveOpts):
        self._func = func
        self.save_opt = save_opt

    @property
    def func(self) -> FunctionType:
        return self._func
