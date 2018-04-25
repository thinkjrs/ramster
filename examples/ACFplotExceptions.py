"""
Exception handling classes for ACFplot function.

InvalidLengthError: Some value is too large for the samples in the data
NevativeValueError: Some value is below 0
"""

class InvalidLengthError(Exception):
    def __init__(self):
        self.name = "Invalid length error - entered value is larger than the series index"
    def __str__(self):
        return repr(self.name)
class NegativeValueError(Exception):
    def __init__(self):
        self.name = "Negative value error - entered value is negative"
    def __str__(self):
        return repr(self.name)
