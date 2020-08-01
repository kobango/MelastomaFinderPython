import numpy as np
import os
import PIL


def MasDataReadAll(path):
    Labelset = []
    ImputSet = []
    ## Wczytajnie txt pliku z opisaem danych
    e = os.path.join(path+"\\PH2_dataset.txt")

    f = open(e,"r")

    labelName=f.readline()

    while True:
        line =f.readline()
        if(line[0]!="|"):
            break
        lineValuetable=line.split("||")
        diagnosticValue = int(lineValuetable[3].replace(" ",""))
        numerOfImage = lineValuetable[1].replace(" ","")
        Labelset.append(diagnosticValue)
        pathToImage = path+"\\PH2 Dataset images\\"+numerOfImage+"\\"+numerOfImage+"_Dermoscopic_Image\\"+numerOfImage+".bmp"
        print(pathToImage)
        oneImg = PIL.Image.open(pathToImage)
        oneImg =oneImg.resize((764,576),PIL.Image.ANTIALIAS)
        tablizedImage = np.array(oneImg.getdata()).reshape(764,576,3)
        ImputSet.append(tablizedImage)



    print(labelName)

    return ImputSet,Labelset

def main():
    print("Main function of the module")
    Inputset, Labelset = MasDataReadAll('D:\\PH2Dataset')
    print(Inputset.__sizeof__())
    print(Labelset)

if __name__ == "__main__":
    # execute only if run as a script
    main()