import pandas as pd

read = pd.read_csv('D:\\python\\pandas\\read.csv')

print(read.shape)
print("\n",read.describe())  #Count Mean , Standard deviation Min and max 
print("\n",read.info()) #Number of entries (rows)  Data types of each column Memory usage
print("\t",read.columns) #Displays the column names of the DataFrame.
