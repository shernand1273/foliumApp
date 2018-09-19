import sys
import os
import pandas
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView

#this class saves the current opened window and returns a boolean as a test case withing the showMiniMap(),
#this is used to determine if there is a window already opened when trying to open a new one
class savedWindow():
    def __init__(self):
        self.window = None

    def setSavedWindow(self,theWindow):
        self.window = theWindow

    def getSavedWindow(self):
        return self.window



lastWin = savedWindow()


def showMiniMap(name,information,coordinates,file):
    #check if there is a dialog window already opened and close it if a new one is coming up
    if(lastWin.getSavedWindow()!=None):
        theWindow = lastWin.getSavedWindow()
        print(type(theWindow))
        theWindow.close()
        lastWin.setSavedWindow(None)

    #create the dialog setWindowTitle
    if(lastWin.getSavedWindow()==None):
        window = QtWidgets.QDialog()
        window.setWindowTitle(name)


    #now we have the file that we are going to build the map out of, this is important because we have to display
    #specific information on mini map based on what their table columns are
        nameLabel = QtWidgets.QLabel(window)
        nameLabel.setText("Name: ")
        nameLabel.setStyleSheet("font: 12px; font-weight: bold")
        nameLabel.move(10,10)
        nameInfo = QtWidgets.QLabel(window)
        nameInfo.setText(name)
        nameInfo.move(80,10)

        elevationLabel = QtWidgets.QLabel(window)
        elevationLabel.setText("Elevation: ")
        elevationLabel.move(10,50)
        elevationLabel.setStyleSheet("font: 12px;font-weight: bold")

        elevationInfo = QtWidgets.QLabel(window)
        elevationInfo.setText(str(information.loc["ELEV"]))
        elevationInfo.move(80,50)


        if(file=="US Volcanoes"):
            print(information)
        #add these two additional labels
        #label for type
            typeLabel=QtWidgets.QLabel(window)
            typeLabel.setText("Type: ")
            typeLabel.move(10,70)
            typeLabel.setStyleSheet("font: 12px;font-weight: bold")
            typeInfo =QtWidgets.QLabel(window)
            typeInfo.setText(str(information.loc["TYPE"]))
            typeInfo.move(80,70)


        #label for status
            statusLabel =QtWidgets.QLabel(window)
            statusLabel.setText("Status: ")
            statusLabel.move(10,90)
            statusLabel.setStyleSheet("font: 12px;font-weight: bold")
            statusInfo = QtWidgets.QLabel(window)
            statusInfo.setText(str(information.loc["STATUS"]))
            statusInfo.move(80,90)


            locationLabel = QtWidgets.QLabel(window)
            locationLabel.setText("Location: ")
            locationLabel.move(10,30)
            locationLabel.setStyleSheet("font: 12px;font-weight: bold")
            locationInformation = QtWidgets.QLabel(window)
            locationInformation.setText(str(information.loc["LOCATION"]))
            locationInformation.move(80,30)

        elif(file=="Top 100 Peaks"):
        #create a custom label for the country
            countryLabel = QtWidgets.QLabel(window)
            countryLabel.setText("Country: ")
            countryLabel.move(10,30)
            countryLabel.setStyleSheet("font: 12px;font-weight: bold")
            countryInfo = QtWidgets.QLabel(window)
            countryInfo.setText(str(information.loc["COUNTRY"]))
            countryInfo.move(80,30)


        mapFrame=QtWidgets.QFrame(window)
        mapFrame.setGeometry(200,10,400,280)
        mapFrame.move(200,20)

    #we are going to build a map so that it can be shown in the mapFrame created actionAbove


        map =folium.Map(location = [coordinates[0],coordinates[1]],tiles ="Stamen Terrain",zoom_start =8)
    #creating the popup text.
        popup=folium.Popup("{}".format(name),parse_html=True)
    #this creates the point on the marker according to LAT and LON and attaches the popup to the marker
        map.add_child(folium.Marker(location =[coordinates[0],coordinates[1]], popup =popup))
        map.save("mini.html")
        miniMapView= QWebEngineView(mapFrame)
        miniMapView.resize(400,280)
    #this will add the html file to the QWebview engine
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "mini.html"))
        url = QtCore.QUrl.fromLocalFile(file_path)
        miniMapView.load(url)


    #save this window objects
        lastWin.setSavedWindow(window)

        window.show()
        window.exec_()
