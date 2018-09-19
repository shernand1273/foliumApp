import fileData
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import os
import miniMap

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

class Map():#may need this for later
    def __init__(self):
        self.theMap=None

    def save(self,m):
        self.theMap=m

    def open(self):
        return self.theMap



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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.searchText= self.search.text()
        self.searchText = self.searchText.title()#sets the first letter of each word to upper case, which is what the data expects
        self.dataFound = None

        #first check that the user has entered something in the search field.
        if(len(self.searchText)==0):
            print("Nothing Entered") #use a popup to let the user know that he needs to enter somthing
        #now that we know the user entered something, lets retrieve the stored data frame, but first lets check that the dropdown menu is something onther than --select-- which is nothing

        elif(len(self.searchText)>0):
            if(self.fileDropDown.currentText()=="---Select Data---"):

                ###################TO DO: Call a popup window######################
                print("Select a data list to load and search through")
                #####################################################
            else:
                #here we are retrieving the stored dataframe, which will return the table belonging to whichever map the user chooses to load
                self.dataTable= storedFrame.getStoredDataFrame()
                #because we are retrieving a pandas data frame, we need to set the index to "NAME" because that is what the user is suppossed to enter
                self.temp=self.dataTable.set_index("NAME")


                #Now we are using the .loc method to find the name entered by the user in the table index

                try:#we will try to find the search text with this method
                    self.information = self.temp.loc[self.searchText]#this is going to get passed to the popup box and the build single map function
                    self.cordinates = self.temp.loc[self.searchText,"LAT":"LON"]#we are also passing
                    #the statement above returns a panda series, we need to convert that into a list so that we can use the values
                    self.cordinates= list(self.cordinates)
                    self.dataTitle.setText("{} found in {}".format(self.searchText, self.fileDropDown.currentText()))

                    #######################################################

                    #when the object is found, create a new map, then load it with the marker of the object

                    #self.buildSinglePointMap(self.information,self.cordinates)
                    miniMap.showMiniMap(self.searchText,self.information,self.cordinates,self.fileDropDown.currentText())



                    ######################################################3


                except:#we are using an exception because if the .loc doesn't find anything, it can crash the program
                    self.dataTitle.setText("Nothing found in {}".format(self.fileDropDown.currentText()))



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

        #this is just going to center the map around the united states as a point to start
        map =folium.Map(location = [41.5,-102.35],tiles ="Stamen Terrain",zoom_start =4.5)

        #we are going to loop through the lists in order to add all the points within the file to the map
        for i in range(self.index):
            name =self.name[i]
            latit=self.lat[i]
            longit=self.lon[i]
            elevat=self.elev[i]
            #creating the popup text.
            pop=folium.Popup("{}, Elev: {}m".format(name,elevat),parse_html=True)
            #this creates the point on the marker according to LAT and LON and attaches the popup to the marker
            map.add_child(folium.Marker(location =[latit,longit], popup =pop))

        self.loadMap(map)

    def loadMap(self,theMap):
        theMap.save("map.html")
        # this will add the html file to the QWebview engine
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "map.html"))
        url = QtCore.QUrl.fromLocalFile(file_path)
        self.mapView.load(url)

    def testing(messgage):
        print(message)

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
