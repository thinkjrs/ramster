"""
coupon_combos.py

Combine two product coupon frames.
"""
import pandas as pd

def combine_frames(df1, df2):
    """
    Assuming equal column headings, combine the dataframes
    into a single two column Pandas DataFrame.

    :param df1:     Pandas DataFrame N rows x M cols
    :param df2:     Pandas DataFrame N rows x M cols

    :returns:       Pandas DataFrame N x M rows x ['DF1', 'DF2']
    """
    # flatten frames
    t1, t2 = df1.unstack().values.flatten(), df2.unstack().values.flatten()
    # combine the frames with a new unique index
    result = pd.DataFrame({'DF1': t1, 'DF2': t2})
    return result
