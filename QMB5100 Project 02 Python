import pandas as pd

FILE = "C://Users//milan//OneDrive//Desktop//Rasmussen College//QMB5100//train.csv"

# Read in the file
df = pd.read_csv(FILE)

# Count rows and columns
print("rows =", df.shape[0])
print("cols =", df.shape[1])

# Print column names and data types
print("Column Names =", df.columns)
print(df.dtypes)

# Perform data indexing
df.loc[0:3, ["Sex", "Survived"]]
df.iloc[0:4, [4, 1]]

# Check for nominal values
print("Sex =", df.Sex.unique())
print("Survived =", df.Survived.unique())
print("Passenger Class =", df.Pclass.unique())

# Analyze the average age by sex
print("Age =",df.Age.mean())
g = df.groupby("Sex")
print("Age by sex =", g.Age.mean())

# Analyze survival rate by sex
print("Survived =",df.Survived.mean())
print("Survived by sex =", g.Survived.mean())

# Flag
Flag1 = df.Pclass == 1
Flag2 = df.Pclass == 2
Flag3 = df.Pclass == 3
print(Flag1.size)
for i in range(5):
    print("Passenger Class =", df.Pclass[i])
    print("Flag1", Flag1[i])
    print("Flag2", Flag2[i])
    print("Flag3", Flag3[i])
    
# Analyze survival rate by class
g = df.groupby("Pclass")
print("Survived =", df.Survived.mean())
print("Survived by class =", g.Survived.mean())
print("=====")
print(df[Flag1].Survived.mean())
print(df[Flag2].Survived.mean())
print(df[Flag3].Survived.mean())

# Dictionary
d = dict()
d["1"] = df[Flag1].Survived
d["2"] = df[Flag2].Survived
d["3"] = df[Flag3].Survived
print("Keys =", d.keys())

# Print the first class survival rate
x = d["1"]
print("Mean 1...", x.mean())

