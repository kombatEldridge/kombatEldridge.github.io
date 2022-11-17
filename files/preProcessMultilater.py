import pandas as pd
import os
import re


def makeOneTxt(txtFilePath):
    dataAlready = pd.read_csv(txtFilePath, sep='\t',
                              header=None, skiprows=1).values.astype(str)
    masterPath = os.getcwd() + "/masterData.txt"
    masterFile = open(masterPath, "a")
    for rows in dataAlready:
        txt = "\t".join(rows)
        masterFile.write(txt+"\n")
    masterFile.close()


def createCSV(masterPath):
    primaryID = createID(os.getcwd())

    dataEsphere = pd.read_csv(
        masterPath, sep='\t', header=None, skiprows=1).values

    lamda = dataEsphere[:, 0]
    qEXT = dataEsphere[:, 1]
    qSCA = dataEsphere[:, 2]
    qABS = dataEsphere[:, 3]
    eSQUARED = dataEsphere[:, 4]

    fullFileName = dataEsphere[:, 5]
    core = []
    middle = []
    outer = []
    measurement = []

    # Example: 25core_10.5nm-Au_2nm-SiO2_outer_sphere
    for i in range(0, len(lamda)):
        componentList = fullFileName[i].split("_")

        core.append(re.findall(
            "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", componentList[0])[0])
        middle.append(re.findall(
            "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", componentList[2])[0])
        outer.append(re.findall(
            "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", componentList[1])[0])
        measurement.append(componentList[3])

    outputFileResults = "/Users/bldrdge1/Downloads/Research/Three Layer/FHU Data/Database Files/Results.csv"
    outputFileConditions = "/Users/bldrdge1/Downloads/Research/Three Layer/FHU Data/Database Files/Conditions.csv"

    file = open(outputFileResults, "w+")
    header = ",".join(["expID", "lambda", "qEXT", "qSCA", "qABS", "eSQU"])

    file.write(header)
    file.write("\n")

    for i in range(0, len(lamda)):
        text = ",".join([str(primaryID[i]),
                         str(lamda[i]),
                         str(qEXT[i]),
                         str(qSCA[i]),
                         str(qABS[i]),
                         str(eSQUARED[i])])
        file.write(text+"\n")
    file.close()

    file = open(outputFileConditions, "w+")
    header = ",".join(["expID", "coreSize", "sio2Size",
                      "shellSize", "outerBoolean"])

    file.write(header)
    file.write("\n")

    for i in range(0, len(primaryID)):
        text = ",".join([str(primaryID[i]),
                         str(core[i]),
                         str(middle[i]),
                         str(outer[i]),
                         str(measurement[i])])
        file.write(text+"\n")
    file.close()

    print("Files printed!")


def createID(filepath):
    dataEsphere = pd.read_csv(
        filepath, sep='\t', header=None, skiprows=1).values
    expConditions = dataEsphere[:, 5]
    primaryID = []
    for i in range(len(expConditions)):
        componentList = expConditions[i].split("_")
        text = []
        for x in range(len(componentList)):
            if (re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", componentList[x]) != []):
                text.append(re.findall(
                    "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", componentList[x])[0])
                text[x] = text[x].replace(".", "")

        if (componentList[3] == "outer"):
            text.append("1")
        if (componentList[3] == "inner"):
            text.append("0")

        primaryID.append("".join(text))
    return primaryID


# To be run in folder with all text files
for txtFilePath in os.listdir(os.getcwd()):
    makeOneTxt(txtFilePath)

# To be run in folder with masterData.txt
createCSV("masterData.txt")
