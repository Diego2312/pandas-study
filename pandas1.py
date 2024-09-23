import pandas as pd


#Data frames are made up of columns and rows where the rows are known as indexes

df = pd.DataFrame([[1, 2, 3], [4,3,5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17]], columns=["A", 'B', "C"], index=["x", "y", "z", "k", "l", "m"]) #Create simple data frame out of python lists

"""
print(df) #Vizualize full dataframe
print(df.head()) #Vizualize first 5 rows of data frame (can pass in first number of rows desired to see)
print(df.tail()) #Same as head but last rows
print(df.sample()) #a sample of data (random)
print(df.columns) #the columns in the df
print(df.index.tolist()) #the indexes (rows) in the df
print(df.info) #Vizualize info on the df (bytes used, size)
print(df.describe) #Useful information (count, mean, standard deviation)
print(df.size) #columns and rows

"""



coffee = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\pandas-study\data\coffee.csv") #Create a df by loading a csv (comma separated values) file. ALso possible with other formats
results_parquet = pd.read_parquet(r"C:\Users\Owner\ACSAI\Extra\pandas-study\data\results.parquet") #Loading a parquet file
bios = pd.read_csv(r"https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv") #loading a file from github. Not locally downloaded

#print(coffee)



print(coffee.loc[[3, 10], ["Coffee Type"]]) #access data by specifying rows and columns (can use indexes and strings) [[rows], [columns]]
print(coffee.iloc[4:10, [2]]) #difference is columns are specified by index instead of name (in ilox upper index is not included)

coffee.loc[5, "Units sold"] = 1203 #Modify a value in the df using loc