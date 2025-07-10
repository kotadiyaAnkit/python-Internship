import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

"""
Create Labels
With the index argument, you can name your own labels.
"""

number = [1, 7, 2]

data = pd.Series(number, index = ["x", "y", "z"])

print(data)