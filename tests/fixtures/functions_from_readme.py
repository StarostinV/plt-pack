FUNC_FROM_README_CODE: str = '''# Imports:
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
'''
