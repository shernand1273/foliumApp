#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *
#from PyQt5 import QtWidgets

import pandas

class Data():
    def __init__(self):
        self.thedata = None


    def getData(self,fileInfoList):
        #fileInfoList is a parameter that expects a list with index 0 being the file path and index 1 being the file extension(xls,txt...)
        filePath = fileInfoList[0]
        fileType = fileInfoList[1]

        #we need to determine the extension fo the filePath because pandas reads files of different types differently
        if(fileType =="txt" or fileType =="csv"):
            tempData = pandas.read_csv(filePath)
            return tempData
        if(fileType =="xls"):
            tempData = pandas.read_excel(filePath)
            return tempData
        if(fileType =="json"):#in case there is a json file added later
            tempData= pandas.read_json(filePath)
            return tempData


class DataFrame():
    def __init__(self):
        self.storedDataFrame = None

    def storeDataFrame(self, df):
        self.storedDataFrame = df


    def getStoredDataFrame(self):
        return self.storedDataFrame