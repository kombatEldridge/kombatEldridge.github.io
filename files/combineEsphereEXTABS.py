import pandas as pd
import os


def combineEsphereEXTABS():
    innerOuterBool = "ERROR"
    alreadyCreatedOuter = False
    alreadyCreatedInner = False

    # If directory is not named in the format xcore/ynm-Au_znm-SiO2/ comment this out until the stars
    for pathFolder in os.listdir(os.getcwd()):
        if '__data.txt' in pathFolder:
            if 'outer' in pathFolder:
                alreadyCreatedOuter = True
            if 'inner' in pathFolder:
                alreadyCreatedInner = True

    for pathFolder in os.listdir(os.getcwd()):
        if pathFolder.startswith('outer') and not alreadyCreatedOuter:
            innerOuterBool = "outer_sphere"
        elif pathFolder.startswith('inner') and not alreadyCreatedInner:
            innerOuterBool = "inner_sphere"

    directories = os.getcwd().split('/')
    outputFile = "_".join(
        [directories[-2], directories[-1], innerOuterBool, "_data.txt"])
    # *********

    # Comment this in if directory not named properly
    # outputFile = "xcore_ynm-Au_znm-SiO2_outer_sphere__data.txt"
    # outputFile = "xcore_ynm-Au_znm-SiO2_inner_sphere__data.txt"

    Esphere = "_".join([innerOuterBool, "average_Esphere.txt"])
    Extabs = "_".join([innerOuterBool, "average_EXTABS_sphere.txt"])

    dataEsphere = pd.read_csv(
        Esphere, sep='\t', header=None, skiprows=1).values
    dataEXTABS = pd.read_csv(Extabs, sep='\t', header=None, skiprows=1).values

    lamda = dataEXTABS[:, 0]
    qEXT = dataEXTABS[:, 5]
    qABS = dataEXTABS[:, 6]
    qSCA = qEXT - qABS
    eSQUARED = dataEsphere[:, 6]

    file = open(outputFile, "w+")
    header = ",".join(["lambda", "qEXT", "qSCA", "qABS", "eSQU", "fileName"])

    file.write(header)
    file.write("\n")

    for i in range(0, len(lamda)):
        text = ",".join([str(lamda[i]),
                         str(qEXT[i]),
                         str(qSCA[i]),
                         str(qABS[i]),
                         str(eSQUARED[i]),
                         outputFile])
        file.write(text+"\n")
    file.close()

    print("File printed: ", outputFile)


# To be run on raw HPC output files
combineEsphereEXTABS()
