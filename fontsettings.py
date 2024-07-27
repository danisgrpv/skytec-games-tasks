import locale
import matplotlib
import matplotlib.pyplot as plt


def set_font_settings(size=14,
                      family='Times New Roman',
                      weight='regular'):
    
    """
    Set the font settings
    """
    locale.setlocale(locale.LC_NUMERIC, "de_DE")
    plt.rcParams['axes.formatter.use_locale'] = True

    font = {'family' : 'Times New Roman',
            'weight' : 'regular',
            'size'   : 14}

    matplotlib.rc('font', **font)