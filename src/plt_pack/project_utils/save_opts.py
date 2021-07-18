from types import FunctionType
from typing import Tuple


PLT_FORMAT: str = 'plt'

# dataclasses are not available in python 3.6 =/
class SaveOpts(object):
    __slots__ = (
        'name',
        'rewrite',
        'datefmt',
        'save_figure',
        'fig_format',
        'save_plt',
    )

    def __init__(self,
                 name: str = None,
                 rewrite: bool = False,
                 datefmt: str = '%d-%b-%H-%M-%S',
                 save_figure: bool = False,
                 fig_format: str = 'eps',
                 save_plt: bool = True,
                 ):

        self.name = name
        self.rewrite = rewrite
        self.datefmt = datefmt
        self.save_figure = save_figure
        self.fig_format = fig_format
        self.save_plt = save_plt

    def asdict(self):
        return {
            'name': self.name,
            'rewrite': self.rewrite,
            'datefmt': self.datefmt,
            'save_figure': self.save_figure,
            'fig_format': self.fig_format,
            'save_plt': self.save_plt
        }

    def new_opts(self, **kwargs):
        opts_dict = self.asdict()
        opts_dict.update(**kwargs)
        return SaveOpts(**opts_dict)

    @property
    def time_str(self):
        return dt.now().strftime(self.datefmt)

    def get_names(self, func: FunctionType = None) -> Tuple[str, str]:
        func_name = self._get_func_name(func)

        return self._get_file_names_from_func_name(func_name)

    def _get_func_name(self, func: FunctionType = None) -> str:
        func_name = self.name or _get_func_name(func)
        if not self.rewrite:
            func_name = f'{func_name}_{self.time_str}'
        return func_name

    def _get_file_names_from_func_name(self, func_name: str) -> Tuple[str, str]:
        return f'{func_name}.{PLT_FORMAT}', f'{func_name}.{self.fig_format}'


def _get_func_name(func: FunctionType = None) -> str:
    # TODO: optionally parse a function to get its real name if __name__ does not exist.
    # check with partial, decorators, etc.
    if func is not None:
        try:
            return func.__name__
        except AttributeError:
            raise ValueError('A function has no attribute __name__, '
                             '"name" attribute should be provided instead.')
    else:
        raise ValueError('Neither name attribute nor a function is provided.')
