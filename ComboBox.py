# -------------------------------------------------------------------------------
# Name:             ComboBox.py
# Purpose:          Simple example of the use of a ComboBox
#
# Author:           Jeffreaux
#
# Created:          08July24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QAction,
    QComboBox,
    QStatusBar,
    QLineEdit,
)
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("ComboBox_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.btnAdd = self.findChild(QPushButton, "btnAdd")

        self.cboEvents = self.findChild(QComboBox, "cboEvents")

        self.actExit = self.findChild(QAction, "actExit")

        self.statusbar = self.findChild(QStatusBar, "statusbar")

        self.txtInput = self.findChild(QLineEdit, "txtInput")



        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.btnAdd.clicked.connect(self.add_to_combobox)

        # Call function when ComboBox is changed
        self.cboEvents.currentIndexChanged.connect(self.send_to_statusbar)

        self.actExit.triggered.connect(self.closeEvent)




        # Show the app
        self.show()

        # Adding Items to ComboBox
        self.cboEvents.addItem("Test")
        self.cboEvents.addItem("Again")

    def add_to_combobox(self):
        self.cboEvents.addItem(self.txtInput.text())  # Adds the text from text box to ComboBox selections
        self.txtInput.clear()  # Clears the text after adding.
    
    def send_to_statusbar(self):
        self.statusbar.showMessage(self.cboEvents.currentText())
        print(self.cboEvents.currentText())  # Get current text in ComboBox

    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
