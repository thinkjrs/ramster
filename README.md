# ramster
Repo for stuff I make with Ram

#### ACFplot.py

Find `ACFplot.py` and `ACFplotExceptions.py` in `/examples`.

You can see the examples below in the workbook titled `ACFplot Quick Example`,
within the `examples` directory.

###### Example

Assume `xt` is a [Pandas](https://pandas.pydata.org) [Series](http://pandas.pydata.org/pandas-docs/stable/10min.html?highlight=series) object and `qqq` is a Pandas [DataFrame](http://pandas.pydata.org/pandas-docs/stable/10min.html?highlight=DataFrame) object.
```{python}
# Basic usage
ACFplot(xt)
```

Notice how that produces a shitty title. Let's improve this a little and add a title, custom z values and specify lags for more precision.
```{python}
ACFplot(np.exp(abs(qqq['Open'] - qqq['Close'])), maxlags=12,
        title="Open less Closing Price of QQQ",
        z1 = 1.96, z2 = 1.645)
```
#### `coupon_combos.py`

###### Example
Run the tests:
`pytest -vv test_coupon_combos.py`

```python
>>> from coupon_combos import combine_frames
>>> combine_frames(df1, df2)
```

For more, see the quick example notebook in the directory above.

Obviously do what you want with the code and cite me if you use it.

Feel free to contribute if you'd like.
