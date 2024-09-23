import pandas as pd


#Data frames are made up of columns and rows where the rows are known as indexes

df = pd.DataFrame([[1, 2, 3], [4,3,5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17]], columns=["A", 'B', "C"], index=["x", "y", "z", "k", "l", "m"]) #Create simple data frame out of python lists

"""

print(df.head()) #Vizualize first 5 rows of data frame
print(df.columns) #Vizualize the columns in the df
print(df.index.tolist()) #Vizualize the indexes (rows) in the df
print(df.info) #Vizualize info on the df (bytes used, size)
print(df.describe) #Useful information (count, mean, standard deviation)
print(df.size) #columns and rows

"""



coffee = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\pandas-study\data\coffee.csv") #Create a df by loading a csv (comma separated values) file. ALso possible with other formats

results_parquet = pd.read_parquet(r"C:\Users\Owner\ACSAI\Extra\pandas-study\data\results.parquet")

print(coffee.head())
print(results_parquet.head())
