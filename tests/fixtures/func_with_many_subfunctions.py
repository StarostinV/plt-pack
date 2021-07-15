from inspect import getsource

import matplotlib as mpl
from matplotlib.patches import Arc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

from plt_pack.parse import FuncDict


def func_with_many_subfunctions(data, cmap=plt.cm.bone, plot_arcs: bool = True,
                                figsize: tuple = (7.5, 6),
                                arc_color: str = 'blue',
                                arc_dict: dict = None,
                                qxy: float = 3.2,
                                qz: float = 3.2,
                                use_gray: bool = False, **kwargs):
    q_max = np.sqrt(qxy ** 2 + qz ** 2)

    img = data['img']
    boxes = data['boxes']
    rr, phi = get_coords(img)

    norm = plt.Normalize(img.min(), img.max())

    if use_gray:
        rgba_gray = plt.cm.gray(norm(img))

        for (x0, y0, x1, y1) in boxes:
            mask = (rr > x0) & (rr < x1) & (phi > y0) & (phi < y1)
            rgba_gray[mask] *= np.array(mpl.colors.to_rgba(arc_color))

        plot_q_space(rgba_gray, figsize=figsize, qxy=qxy, qz=qz, cbar=False, cmap=None, **kwargs)

    else:

        plot_q_space(img, figsize=figsize, qxy=qxy, qz=qz, cbar=True, cmap=cmap, **kwargs)

    if plot_arcs:
        default_arc_dict = dict(lw=2, ls='--')
        default_arc_dict.update(arc_dict or {})
        arc_dict = default_arc_dict

        ax = plt.gca()

        for (x0, y0, x1, y1) in boxes:
            c = arc_color

            r = (x0 + x1) / 2 / 512 * q_max
            w = abs(x1 - x0) / 2 / 512 * q_max
            angle = (y0 + y1) / 2 / 512 * 90
            a_width = abs(y1 - y0) / 2 / 512 * 90

            ax.add_patch(Arc((0, 0), 2 * r - w * 2.5, 2 * r - w * 2.5, angle=angle,
                             theta1=-a_width, theta2=a_width,
                             color=c, **arc_dict))
            ax.add_patch(Arc((0, 0), 2 * r + w * 2.5, 2 * r + w * 2.5, angle=angle,
                             theta1=-a_width, theta2=a_width,
                             color=c, **arc_dict))


def plot_q_space(img, figsize: tuple = (8, 5),
                 cmap: str = 'jet',
                 qxy: float = 3.2,
                 qz: float = 3.2,
                 cbar: bool = True, **kwargs):
    if isinstance(img, dict):
        img = img['img']
    img = np.flip(img, 0)

    plt.figure(figsize=figsize)
    im = plt.imshow(img, cmap=cmap, origin='lower', extent=(0, qz, 0, qxy), **kwargs)
    if cbar:
        cb = colorbar(im)
    plt.xlabel('$Q_{||}$ ($\AA^{-1}$)')
    plt.ylabel('$Q_{z}$ ($\AA^{-1}$)')


def get_coords(img):
    x, y = np.ogrid[0:img.shape[0], 0:img.shape[1]]

    rr = np.sqrt(x ** 2 + y ** 2)
    rr = np.flip(rr, 0)
    rr = rr / rr.max() * 512

    phi = np.arctan2(x, y)
    phi = np.flip(phi, 0)
    phi = phi / phi.max() * 512
    return rr, phi


def colorbar(mappable):
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax)
    plt.sca(last_axes)
    return cbar


FUNC_WITH_MANY_SUBFUNCTIONS_DICT = FuncDict(
    entry_func='func_with_many_subfunctions',
    functions={
        'func_with_many_subfunctions': getsource(func_with_many_subfunctions),
        'plot_q_space': getsource(plot_q_space),
        'get_coords': getsource(get_coords),
        'colorbar': getsource(colorbar),
    },
    modules=('matplotlib', 'numpy', 'mpl_toolkits'),
    import_lines=(
        'import matplotlib as mpl',
        'from matplotlib.patches import Arc',
        'import numpy as np',
        'import matplotlib.pyplot as plt',
        'from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable',
    ),
    module_versions={},
    global_vars={},
)
