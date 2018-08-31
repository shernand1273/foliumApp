import fileData
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import os

class DropDown():
    def __init__(self):
        self.stateIndex =None
        self.file= {0:"",1:["../data/Volcanoes_USA.txt","txt"],2:["../data/WorldTop100Peaks.xls","xls"]}
    def setStateIndex(self,val):
        self.stateIndex=val
    def getFileName(self):
        return self.file[self.stateIndex]
    def getDropDownIndex(self):
        return self.stateIndex


storedFrame = fileData.DataFrame()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 483)
        self.programWindow = QtWidgets.QWidget(MainWindow)
        self.programWindow.setObjectName("programWindow")
        self.gridLayout = QtWidgets.QGridLayout(self.programWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search = QtWidgets.QLineEdit(self.programWindow)
        self.dataTitle = QtWidgets.QLabel(self.programWindow)
        self.dataTitle.setText("")
        self.dataTitle.move(300,5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.findButton = QtWidgets.QPushButton(self.programWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findButton.sizePolicy().hasHeightForWidth())
        self.findButton.setSizePolicy(sizePolicy)
        self.findButton.setObjectName("findButton")
        self.findButton.clicked.connect(lambda: self.find())
        #self.viewDataList=QtWidgets.QPushButton(self.programWindow)#####################################
        self.horizontalLayout.addWidget(self.findButton)
        self.horizontalLayout.addWidget(self.dataTitle)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setContentsMargins(-1, 0, -1, -1)
        self._2.setObjectName("_2")
        self.dropDownLabel = QtWidgets.QLabel(self.programWindow)
        self.dropDownLabel.setObjectName("dropDownLabel")
        self._2.addWidget(self.dropDownLabel, 0, QtCore.Qt.AlignRight)
        self.fileDropDown = QtWidgets.QComboBox(self.programWindow)
        self.fileDropDown.currentIndexChanged.connect(self.selectionchange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileDropDown.sizePolicy().hasHeightForWidth())
        self.fileDropDown.setSizePolicy(sizePolicy)
        self.fileDropDown.setObjectName("fileDropDown")
        self.fileDropDown.addItem("")
        self.fileDropDown.addItem("")
        self.fileDropDown.addItem("")
        self._2.addWidget(self.fileDropDown)
        self.gridLayout.addLayout(self._2, 0, 1, 1, 1)
        self.mapFrame = QtWidgets.QFrame(self.programWindow)
        self.mapFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mapFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mapFrame.setObjectName("mapFrame")
        self.mapView= QWebEngineView(self.mapFrame)
        self.gridLayout.addWidget(self.mapFrame, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.mapView,1,0,1,2)
        MainWindow.setCentralWidget(self.programWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 22))
        self.menubar.setObjectName("menubar")
        self.menumapView = QtWidgets.QMenu(self.menubar)
        self.menumapView.setObjectName("menumapView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout_mapView = QtWidgets.QAction(MainWindow)
        self.actionAbout_mapView.setObjectName("actionAbout_mapView")
        self.menumapView.addAction(self.actionRefresh)
        self.menumapView.addSeparator()
        self.menumapView.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout_mapView)
        self.menubar.addAction(self.menumapView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Map"))
        self.findButton.setText(_translate("MainWindow", "Find"))
        self.dropDownLabel.setText(_translate("MainWindow", "Data"))
        self.fileDropDown.setItemText(0, _translate("MainWindow", "---Select Data---"))
        self.fileDropDown.setItemText(1, _translate("MainWindow", "US Volcanoes"))
        self.fileDropDown.setItemText(2, _translate("MainWindow", "Top 100 Peaks"))
        self.menumapView.setTitle(_translate("MainWindow", "mapView"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout_mapView.setText(_translate("MainWindow", "About mapView"))

    def selectionchange(self,i):
        self.selection = DropDown()
        self.selection.setStateIndex(i)

        if(self.selection.getDropDownIndex()==0):
            self.dataTitle.setText("")

        if(self.selection.getFileName()!=""):

            #get all the data here and create a map
            self.file = fileData.Data() #create the object to hold the datafile
            self.data = self.file.getData(self.selection.getFileName())
            #save the data for later reference if the user wants to search for certain objects within the currently selectd datafile
            #now that we have the data... lets use the current text method to set a lable in the GUI letting the user know what data they are looking at
            self.dataTitle.setText(self.fileDropDown.currentText())
            #to build the map, call buildMap() and pass it the data
            self.buildMap(self.data)

    def find(self):
        print("I shall find something for you")
        #use the dropdown return value from the object's dictionary
        #self.fileValue = self.selection.getDropDownIndex()
        #if(self.fileValue==0):
            #use a popup box to let the user know that he has to select a data file from the dropdown
           # print("You have to select something")
        #else:
           # print(self.fileDropDown.currentText())

    def buildMap(self,df):
        #df - this is the data frame we are going to work with
        import folium
        #use the .shape() method to retrieve information about the data frame.  This method returs a tuple (rows(indexes),columns)
        #.shape[0] will give us the index value needed to iterate through the table
        self.index = df.shape[0]#this index is the amoutn fo rows in the pandas table
        self.name=None
        self.elevation=None
        self.lat =None
        self.lon =None

        #WE HAVE TO STORE THE DATA FRAME SO THAT WE CAN LATER USE IT TO FIND LOCATIONS
        storedFrame.storeDataFrame(df)


        #we need the lattitude, longitude, name, elevation
        self.name = list(df["NAME"])
        self.lat =list(df["LAT"])
        self.lon = list(df["LON"])
        self.elev= list(df["ELEV"])

        map =folium.Map(location = [41.5,-102.35],tiles ="Stamen Terrain",zoom_start =4.5)


        for i in range(df.shape[0]):
            name =self.name[i]
            latit=self.lat[i]
            longit=self.lon[i]
            elevat=self.elev[i]

            pop=folium.Popup("{}, Elev: {}m".format(name,elevat),parse_html=True)

            map.add_child(folium.Marker(location =[latit,longit], popup =pop))


        map.save("map.html")
        #this will add the html file to the QWebview engine
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "map.html"))
        url = QtCore.QUrl.fromLocalFile(file_path)
        self.mapView.load(url)



def main():

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

main()
