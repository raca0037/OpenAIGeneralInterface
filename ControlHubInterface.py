# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_ControlHub.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

#Goal is to have this file be a class to just call into ControlHubIntegration.py
from PyQt5 import QtCore, QtGui, QtWidgets

#class giving us our main display window:
class Ui_MainWindow(object):
   # action = a #initializing variable action

    def __init__(self):
       self._reward = 0.0
       self._action = ''
       self.a = (0,0,0)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 784)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Gas_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.get_action("W"))
        self.Gas_Button.setGeometry(QtCore.QRect(390, 180, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(41)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Gas_Button.setFont(font)
        self.Gas_Button.setObjectName("Gas_Button")
        self.Turn_Right = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.get_action("D"))
        self.Turn_Right.setGeometry(QtCore.QRect(540, 330, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(41)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Turn_Right.setFont(font)
        self.Turn_Right.setObjectName("Turn_Right")
        self.Turn_Left = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.get_action("A"))
        self.Turn_Left.setGeometry(QtCore.QRect(240, 330, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(41)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Turn_Left.setFont(font)
        self.Turn_Left.setObjectName("Turn_Left")
        self.Brake_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.get_action("S"))
        self.Brake_Button.setGeometry(QtCore.QRect(390, 480, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(41)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Brake_Button.setFont(font)
        self.Brake_Button.setObjectName("Brake_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Action function for the interface, will result in action in the racecar when pressed.
    def get_action(self,pressed): #need to fix what a will mean, main.py used a control variable to log action being taken on keyboard vs. action imported into display.

            if pressed == "S":
                self.a = (0, 0, 1)
                self._action = 'brake' #feed in list of actions, assign an action to the list, to prevent changing lower level functions.
            elif pressed == "W":
                self.a = (0, 1, 0)
                self._action = 'gas'
            elif pressed == "A":
                self.a= (-1, 0, 0)
                self._action = 'left'
            elif pressed == "D":
                self.a = (+1, 0, 0)
                self._action = 'right'
            else:
                self.a= (0, 0, 0)
                self._action = ''


#GUI designer using a translater.
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow_ControlHub"))
        self.Gas_Button.setText(_translate("MainWindow", "W"))
        self.Turn_Right.setText(_translate("MainWindow", "D"))
        self.Turn_Left.setText(_translate("MainWindow", "A"))
        self.Brake_Button.setText(_translate("MainWindow", "S"))





#if __name__ == "__main__":

    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #control_action = get_action()
   # control_action = ui.action() #assigning the action output to control_action
    #sys.exit(app.exec_())
