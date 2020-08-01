import numpy as np
import os
import PIL
from PIL import Image



def MasDataReadAll(path):
    Labelset = []
    ImputSet = []
    ## Wczytajnie txt pliku z opisaem danych
    pathToTxtFile = os.path.join(path+"\\PH2_dataset.txt")

    txtFile = open(pathToTxtFile,"r")

    labelName=txtFile.readline()

    labelName =labelName.replace(" ","")
    labelArray = labelName.split('||')
    print(labelArray)
    indexOfName = labelArray.index("Name")
    indexOfClinicalDiagnosis = labelArray.index("ClinicalDiagnosis")
    indexOfFirstValue = 0
    imageHeight = 576
    imageWith = 764
    numberOfCanal = 3
    typeOfImageResizeAproxymation = PIL.Image.ANTIALIAS

    while True:
        line =txtFile.readline()
        if(line[indexOfFirstValue]!="|"):
            break
        lineValuetable=line.split("||")
        diagnosticValue = int(lineValuetable[indexOfClinicalDiagnosis].replace(" ",""))
        numerOfImage = lineValuetable[indexOfName].replace(" ","")
        Labelset.append(diagnosticValue)
        pathToImage = path+"\\PH2 Dataset images\\"+numerOfImage+"\\"+numerOfImage+"_Dermoscopic_Image\\"+numerOfImage+".bmp"
        print(pathToImage)

        oneImg = Image.open(pathToImage)
        oneImg =oneImg.resize((imageWith,imageHeight),typeOfImageResizeAproxymation)
        tablizedImage = np.array(oneImg.getdata()).reshape(imageWith,imageHeight,numberOfCanal)
        ImputSet.append(tablizedImage)



    print(labelName)

    return ImputSet,Labelset

def main():
    print("Main function of the module")
    Inputset, Labelset = MasDataReadAll('D:\\PH2Dataset')
    print(Inputset.__sizeof__())
    print(Inputset)
    print(Labelset)

if __name__ == "__main__":
    # execute only if run as a script
    main()