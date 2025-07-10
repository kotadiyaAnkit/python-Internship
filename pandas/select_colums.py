import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)

# Select one column: 'Age'
print("Single column - Age:")
print(df['Age'])

print("\nMultiple columns - Name and Score:")
# Select multiple columns: 'Name' and 'Score'
print(df[['Name', 'Score']])
