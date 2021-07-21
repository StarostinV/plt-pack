import numpy as np
import matplotlib.pyplot as plt


def test_functions_from_readme(plt_project, func_from_readme_code):
    plt_project._TEST = True

    # define some functions; register them or turn on auto_save

    # some util functions & globals defined somewhere in your
    # file or Jupyter Notebook

    COLOR = 'red'

    def plot_line(x, y, label: str = None, ls: str = '--'):
        plt.plot(x, y, ls=ls, lw=2, c=COLOR, label=label)

    def add_legend():
        plt.legend()

    @plt_project.register
    def plot(x, y_list, label_list):
        for y, label in zip(y_list, label_list):
            plot_line(x, y, label)
        add_legend()

    @plt_project.auto_save(rewrite=False, datefmt='%H-%M-%S')
    def plot_hist(y, bins: int = 10):
        plt.hist(y, bins=bins)

    x = np.arange(10)
    y_list = [np.arange(10) * i for i in range(5)]
    label_list = [f'Curve #{i}' for i in range(5)]

    with plt_project(rewrite=True, name='my_function'):
        plot(x, y_list, label_list)

    file = plt_project.load_file('my_function')

    assert func_from_readme_code == file.get_code_str()
