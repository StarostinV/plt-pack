# PltPack

## _Bind your matplotlib functions with data_

[![Test](https://github.com/StarostinV/plt-pack/actions/workflows/run-tests.yaml/badge.svg)](https://github.com/StarostinV/plt-pack/)

[comment]: <> ([![codecov]&#40;https://codecov.io/gh/StarostinV/plt-pack/branch/master/graph/badge.svg&#41;]&#40;https://codecov.io/gh/StarostinV/plt-pack&#41;)

[![PyPI version fury.io](https://badge.fury.io/py/plt-pack.svg)](https://pypi.python.org/pypi/plt-pack/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/plt-pack.svg)](https://pypi.python.org/pypi/plt-pack/)
[![PyPI license](https://img.shields.io/pypi/l/plt-pack.svg)](https://pypi.python.org/pypi/plt-pack/)
[![PyPI status](https://img.shields.io/pypi/status/plt-pack.svg)](https://pypi.python.org/pypi/plt-pack/)

PltPack is a lightweight packaging tool for storing and exchanging data & code bound in a single file. It is mainly
created to accelerate scientific work and is focused on supporting matplotlib package for exchanging scientific figures.
Integrated with Jupyter Notebook.

Install from PyPi with pip:

```
pip install plt_pack
```

### Usage

PltPack saves minimal atomic part of your code and the data required to run a function and plot a figure:
* arguments
* imports
* function code  
* called sub-functions
* global variables 
* used module versions
* non-default matplotlib rcParams

The most convenient way to use PltPack is to define a project with a 
folder where all the .plt files will be saved, and register the entry functions
you would like to save. The alternative is to decorate a function with 'auto_save'
method to save it with new arguments on every call.

Below is a self-explanatory example:

```python
# imports
from matplotlib import pyplot as plt
import numpy as np

from plt_pack import PltProject

# define your project with directory for figures
plt_project = PltProject('FiguresDir')

# define your functions
# decorate them with 'register' or 'auto_save' method

@plt_project.register
def plot(x, y_list, label_list):
    for y, label in zip(y_list, label_list):
        plot_line(x, y, label)
    add_legend()


@plt_project.auto_save(rewrite=False, datefmt='%H-%M-%S')
def plot_hist(y, bins: int = 10):
    plt.hist(y, bins=bins)


# some util functions & globals defined somewhere in your
# file or Jupyter Notebook

COLOR = 'red'

def plot_line(x, y, label: str = None, ls: str = '--'):
    plt.plot(x, y, ls=ls, lw=2, c=COLOR, label=label)

def add_legend():
    plt.legend()
    
    
# Registered function can be saved with context parameters:
x = np.arange(10)
y_list = [np.arange(10) * i for i in range(5)]
label_list = [f'Curve #{i}' for i in range(5)]

with plt_project(rewrite=True, name='my_function'):
    plot(x, y_list, label_list)
    
# function will be executed but also saved to my_function.plt
# file to your project folder:

assert plt_project.list_files() == ['my_function']
```

Now you can upload this file later (non necessarily on the same machine)
and reproduce the result with one call.


```python
from plt_pack import read_plt_file

file = read_plt_file('my_function')
# or using plt_project: 
# file = plt_project.load_file('path/to/file')

file.exec()  # that will re-run the function

print(file.get_code_str())  # that will show all the code to reproduce it
```

Expected output:

```python
# Imports:
import matplotlib.pyplot as plt

# Global variables:
COLOR = 'red'

# Main function:

def plot(x, y_list, label_list):
    for y, label in zip(y_list, label_list):
        plot_line(x, y, label)
    add_legend()


# Sub-functions:

def add_legend():
    plt.legend()


def plot_line(x, y, label: str = None, ls: str = '--'):
    plt.plot(x, y, ls=ls, lw=2, c=COLOR, label=label)


```




### LICENSE

MIT