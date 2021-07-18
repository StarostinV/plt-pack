import logging
from pathlib import Path
from datetime import datetime as dt
from functools import wraps
from typing import List, Dict, Tuple, Any, Optional
from types import FunctionType
from contextlib import contextmanager

import matplotlib.pyplot as plt

from .save_opts import SaveOpts, PLT_FORMAT
from .registered_func import RegisteredFunc
from ..file import save_plt_file, read_plt_file, PltFile


class PltProject(object):
    _TEST: bool = False

    def __init__(self,
                 folder: Path or str,
                 save_opts: SaveOpts = None,
                 **save_opt_kwargs,
                 ):
        self.folder = Path(folder)
        self.folder.mkdir(exist_ok=True)

        self.default_opts = save_opts or SaveOpts(**save_opt_kwargs)
        self.current_opts: SaveOpts = None
        self.registered_functions: Dict[str, RegisteredFunc] = {}

    def _get_save_opts(self, **kwargs) -> SaveOpts:
        opts = self.current_opts or self.default_opts
        return opts.new_opts(**kwargs)

    @contextmanager
    def __call__(self,
                 save_opts: SaveOpts = None,
                 **save_opt_kwargs
                 ):

        self.current_opts = save_opts or self._get_save_opts(**save_opt_kwargs)
        try:
            yield
        finally:
            self.current_opts = None

    def save(self,
             func: FunctionType,
             args: Optional[Tuple[Any, ...]],
             kwargs: Optional[Dict[str, Any]] = None,
             save_opts: Optional[SaveOpts] = None,
             **save_opt_kwargs,
             ) -> Path:

        save_opts = save_opts or self._get_save_opts(**save_opt_kwargs)

        plt_name, fig_name = save_opts.get_names(func)
        plt_path = self.folder / plt_name

        kwargs = kwargs or {}

        if save_opts.save_figure:
            _save_figure(func, self.folder / fig_name, args, kwargs)

        if save_opts.save_plt:
            save_plt_file(plt_path, func, *args, **kwargs)

        return plt_path

    def auto_save(self, save_opts: Optional[SaveOpts] = None, **save_opt_kwargs):
        save_opts = save_opts or self._get_save_opts(**save_opt_kwargs)

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if not self._TEST:
                    func(*args, **kwargs)
                self.save(func, args, kwargs, save_opts)

            return wrapper

        return decorator

    def register(self, func: FunctionType):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self._register_called(func, args, kwargs)

        return wrapper

    def _register_called(self, func: FunctionType, args: List[Any], kwargs: Dict[str, Any]):
        func(*args, **kwargs)
        self.save(func, args, kwargs)

    def list_files(self) -> List[str]:
        return [path.stem for path in self.folder.glob(f'*.{PLT_FORMAT}')]

    def load_file(self, name: str) -> PltFile:
        return read_plt_file(self.folder / f'{name}.{PLT_FORMAT}')

    def __getitem__(self, name: str):
        return self.load_file(name)


def _save_figure(
        func: FunctionType,
        path: Path,
        args: Tuple[Any, ...],
        kwargs: Dict[str, Any]
):

    path = str(path.absolute())
    plt.ioff()
    try:
        func(*args, **kwargs)
    except Exception as err:
        logger = logging.getLogger(__name__)
        logger.exception(err)
        logger.error(f'Function execution failed. Could not save to {path}.')
    plt.savefig(path)
    plt.ion()
