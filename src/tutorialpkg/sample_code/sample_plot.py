from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def draw_sample_plot(df):
    """Draw a sample plot using pandas.plot() method.

    Args:
        df (pd.DataFrame): Sample DataFrame to plot.

    Returns:
        None
    """

    # Using pandas.plot directly creates the figure, axes and allows for some customisation
    # matplotlib examples typically split this into separate commands defining fig and ax then adding customisation
    df.plot(title='Sample Plot', xlabel='X-axis Label', ylabel='Y-axis Label')

    # Show the plot
    plt.show()


def save_sample_boxplot(df):
    """Draw a sample boxplot using pandas.plot() method and save to .png file.

    Args:
        df (pd.DataFrame): Sample DataFrame to plot.

    Returns:
        None

    """
    df.boxplot()
    # df.plot.box()  # This syntax is also valid
    fig_fp = Path(__file__).parent.joinpath('plt-boxplot.png')
    plt.savefig(fig_fp)


if __name__ == '__main__':
    # Sample DataFrame
    df_sample = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]})

    # Draw the sample plot
    draw_sample_plot(df_sample)

    # Save boxplot to .png file
    df_another_sample = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
