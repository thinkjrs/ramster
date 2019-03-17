"""
test_coupon_combos.py

Unit tests for coupon_combos.py
"""

import pytest
import pandas as pd
from coupon_combos import combine_frames

@pytest.fixture
def test_data():
    """
    Return a two column ['A', 'B'], [0, 4] index DataFrame.
    """
    return pd.DataFrame({
        'A': [1, 2, 3, 4,],
        'B': [5, 6, 7, 8,]
    })

def test_combine_frames(test_data):
    """
    Test the overall functionality of coupon_combos
    """
    test = combine_frames(test_data, test_data)
    assert test.equals(pd.DataFrame({'DF1':[1, 2, 3, 4, 5, 6, 7, 8], 
                                    'DF2':[1, 2, 3, 4, 5, 6, 7, 8]}))
