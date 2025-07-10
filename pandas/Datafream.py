import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],	
    'Age': [25, 30, 35],	
    'Score': [85, 90, 95]	
}

d1 = pd.DataFrame(data)
print(d1)