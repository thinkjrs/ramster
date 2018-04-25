"""
ACFplot.py

Plotting for Autocorrelation Function (ACF)

See [Autocorrelation]https://en.wikipedia.org/wiki/Autocorrelation
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from ACFplotExceptions import InvalidLengthError, NegativeValueError
# make the plot look sweet
plt.style.use('seaborn-whitegrid')
def ACFplot(timeseries, maxlags = 36, title = None, z1 = None, z2 = None):
    """
    This function takes a Pandas Series object and plots its autocorrelation function.
    The plot is in the 'R style' found in the timeseries module; as such it shows
    a basic, positive ACF of the series (as opposed to the signal processing literature which
    typically shows an ACF centered at zero).

    ARGUMENTS:
    [required]
    timeseries (Pandas Series object)
    [optional]
    maxlags (integer): number of lags to plot, up to length(timeseries)
    name (string): Heading for series
        ex: name = "Closing price of AAPL" will provide the following plot labels
            title = "ACF of Timeseries Clossing price of AAPL"
            ylab = "Autocorrelation"
            xlab = "Lag"

        **Note: only the title is mutable
    z1, z2 (numeric): z values for horizontal p-value boundaries. Defaults to 95% and 99%.

    """

    # Exception Handling

    try:
        if maxlags > len(timeseries.index): raise InvalidLengthError
        if maxlags < 0: raise NegativeValueError

        if not title:
            title = timeseries.name
        lags, c, line, b = plt.acorr(timeseries, color = 'b');
        plt.xlim(xmin=1,xmax=maxlags )
        plt.ylim(ymin=min(-.2, min(c[c != -1]) - .05), ymax=max(c[c != 1])+.05)
        n = len(timeseries)
        # from pandas source "https://github.com/pandas-dev/pandas/" -> plotting/_misc.py
        if not z1:
            z1 = 1.959963984540054
        if not z2:
            z2 = 2.5758293035489004
        plt.axhline(y=z2 / np.sqrt(n-1), linestyle='--', color='grey')
        plt.axhline(y=z1 / np.sqrt(n-1), color='grey')
        plt.axhline(y=0.0, color='black')
        plt.axhline(y=-z1 / np.sqrt(n-1), color='grey')
        plt.axhline(y=-z2 / np.sqrt(n-1), linestyle='--', color='grey')
        plt.xlabel("Lag")
        plt.ylabel("Autocorrelation")
        plt.title("ACF of Timeseries "+ title)
        plt.show()
    except InvalidLengthError:
        print(InvalidLengthError().name)
    except NegativeValueError:
        print(NegativeValueError().name)
    except:
        print("Unknown exception thrown. Examine inputs and usage.")
