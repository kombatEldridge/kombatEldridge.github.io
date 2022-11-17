from pylab import *
import secrets
import matplotlib.pyplot as plt
import pymysql
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# --------------- connection --------------- #

hostdb = "localhost"
portdb = int(3306)
userdb = "root"
passworddb = "123456789"
namedb = "multilayer"

conn = pymysql.connect(host=hostdb, port=portdb,
                       user=userdb, passwd=passworddb, db=namedb)
dfConditions = pd.read_sql_query("SELECT * FROM conditions", conn)
dfResults = pd.read_sql_query("SELECT * FROM results", conn)

numWhere = int(input("How many WHERE clauses do you want to add?\n> "))
print()

for i in range(len(dfConditions.columns)):
    print(dfConditions.columns[i])

print()
whereClause = []
for x in range(numWhere):
    whereClause.append(
        input("Please enter your WHERE clause (ex: \"coreSize = 5\"):\n> "))

dfString = "SELECT * FROM results NATURAL JOIN conditions WHERE {}".format(
    " AND ".join(whereClause))

df = pd.read_sql_query(dfString, conn)

print("Experiments found:")
print(df["expID"].unique())

# --------------- conditions entry --------------- #

lamda = df["lambda"].unique()

class xVar:
    def __init__(self, name):
        self.name = name
        self.dictionary = {}
        for expID in df["expID"].unique():
            self.dictionary[expID] = expVar(expID, name)

class expVar:
    def __init__(self, expID, parent):
        self.expID = expID
        self.name = parent
        dfStringTemp = " ".join([dfString, "AND expID =", str(expID)])
        dfTemp = pd.read_sql_query(dfStringTemp, conn)
        self.data = dfTemp[self.name].to_numpy()
        self.lamda = dfTemp["lambda"].to_numpy()
        self.color = f"#{secrets.token_hex(3)}"

numSeries = int(input("How many series do you want to map?\n> "))
print()

for i in range(len(dfResults.columns)):
    print("\t".join([":".join([str(i), ""]), dfResults.columns[i]]))

print()
series = {}
for x in range(numSeries):
    index = int(input("Please select index of series:\n> "))
    series["series{}".format(x)] = xVar(dfResults.columns[index])

# --------------- figure creation --------------- #

expIDi = []
expIDo = []
for expID in df["expID"].unique():
    if (str(expID)[-1] == "0"):
        expIDi.append(expID)
    else:
        expIDo.append(expID)


for ser in series:
    for outer in expIDo:
        plt.plot(series[ser].dictionary[outer].lamda, series[ser].dictionary[outer].data, '-',
                 c=series[ser].dictionary[outer].color, label=series[ser].dictionary[outer].expID)

    plt.legend()
    plt.ylabel(series[ser].name, fontsize=20)
    plt.xlabel('Wavelength (nm)', fontsize=20)
    plt.title(" ".join([dfString, "(Outer Sphere)"]), fontsize=16)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(14, 8)
    plt.show()

    for inner in expIDi:
        plt.plot(series[ser].dictionary[inner].lamda, series[ser].dictionary[inner].data, '-',
                 c=series[ser].dictionary[inner].color, label=series[ser].dictionary[inner].expID)

    plt.legend()
    plt.ylabel(series[ser].name, fontsize=20)
    plt.xlabel('Wavelength (nm)', fontsize=20)
    plt.title(" ".join([dfString, "(Inner Sphere)"]), fontsize=16)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(14, 8)
    plt.show()
