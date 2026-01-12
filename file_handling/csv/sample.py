import pandas as pd

df = pd.read_csv("file_handling/sample.csv")

#prints first 5 rows to check the data
a = df.head()
print(a)

#prints column names
b = df.columns

print(b)

#prints [rows, columns]

c = df.shape

print(c)

#prints location

d = df.loc[5]

print(d)

#prints mean, median, mode

e = df['marks'].mean()

print(e)

#print max (first find index of max by idxmax then location)

f = df.loc[df['marks'].idxmax()]

print(f)

#print mean of marks grouped by name
g = df.groupby('name')['marks'].mean()

print(g)