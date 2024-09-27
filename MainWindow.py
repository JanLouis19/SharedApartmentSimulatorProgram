# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import sys
import time
import threading
import random
from Residents import *
from Total import *



# ----- LiveLine is the dynamic colored line at the bottom of the program, this thread makes it move horizontally -----
class LiveLineThread(QThread):
    LiveLineLabel1 = QtCore.pyqtSignal()
    LiveLineLabel2 = QtCore.pyqtSignal()

    # ----- Constant horizontal moving of the line -----
    def run(self):
        while (True):
            self.LiveLineLabel2.emit()
            time.sleep(0.2)
            self.LiveLineLabel1.emit()
            time.sleep(0.2)

# ----- LiveLineThreadSwitch is the Thread that makes the colors purple and white switch -----
class LiveLineThreadSwitch(QThread):
    LiveLineLabel1_1 = QtCore.pyqtSignal()
    LiveLineLabel2_2 = QtCore.pyqtSignal()

    # ----- constant switching of purple and white colors -----
    def run(self):
        while (True):
            self.LiveLineLabel1_1.emit()
            time.sleep(0.3)
            self.LiveLineLabel2_2.emit()
            time.sleep(0.3)

# ----- MainWindow Class -----
class Ui_MainWindow(object):

    # ----- Open the residents window -----
    def openResidents(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    # ----- Open the Total Window -----
    def openTotal(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Total()
        self.ui.setupUi(self.window)
        self.window.show()

    # ----- Start the LiveLine -----
    def clickedBtnLiveLine(self):
        # ----- The StartStopPixel and LiveLinePixel are explained in the description of the ComboPressed Function below -----
        # ----- They have no visual effect for the user, they just help make the program work -----
        # ----- The integers c1 and c2 are also just a help for the program, informing whether the button Start/Stop was clicked or not -----
        c1 = 0
        c2 = 1
        if (self.StartStopPixel.isVisible() == False):
            if (self.combo.currentText() == " purple-white"):
                self.workerrr = LiveLineThreadSwitch()
                self.workerrr.start()
                self.workerrr.LiveLineLabel1_1.connect(self.LiveLineLabel1_1_exec)
                self.workerrr.LiveLineLabel2_2.connect(self.LiveLineLabel2_2_exec)
                self.LiveLinePixel.show()
                self.workerjoa = LiveLineThread()
                self.workerjoa.start()
                self.workerjoa.LiveLineLabel1.connect(self.LiveLineLabel1_exec)
                self.workerjoa.LiveLineLabel2.connect(self.LiveLineLabel2_exec)

            else:
                self.workerjoa = LiveLineThread()
                self.workerjoa.start()
                self.workerjoa.LiveLineLabel1.connect(self.LiveLineLabel1_exec)
                self.workerjoa.LiveLineLabel2.connect(self.LiveLineLabel2_exec)
            c1 = 1
        if (self.StartStopPixel.isVisible() == True):
            self.workerjoa.terminate()
            self.workerjoa.quit()
            c2 = 0
        if (c1 == 1):
            self.StartStopPixel.show()
        if (c2 == 0):
            self.StartStopPixel.hide()
        if (self.LiveLinePixel.isVisible() == True and c2 == 0):
            self.workerrr.terminate()
            self.workerrr.quit()
            self.LiveLinePixel.hide()

    # ----- Make the LiveLine move horizontally 1/2 -----
    def LiveLineLabel1_exec(self):
        self.LiveLine1.setText("  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /")
        self.LiveLine2.setText(" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /")

    # ----- Make the LiveLine move horizontally 2/2 -----
    def LiveLineLabel2_exec(self):
        self.LiveLine1.setText("   / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /")
        self.LiveLine2.setText("  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /")

    # ----- Make the LiveLine switch its colors from purple-white to white-purple 1/2 -----
    def LiveLineLabel1_1_exec(self):
        self.LiveLine1.setStyleSheet("QLabel { color : darkviolet; }")
        self.LiveLine2.setStyleSheet("QLabel { color : white; }")

    # ----- Make the LiveLine switch its colors from purple-white to white-purple 2/2 -----
    def LiveLineLabel2_2_exec(self):
        self.LiveLine1.setStyleSheet("QLabel { color : white; }")
        self.LiveLine2.setStyleSheet("QLabel { color : darkviolet; }")

    # ----- Click on the Go-Button next to the combobox (to applicate the change of the colors chosen in the combobox -----
    def comboPressed(self):
        # ----- If the StartStopPixel is Visible, the LiveLine is running currently -----
        # ----- If the LiveLinePixel is visible, the LiveLine color is set to purple-white (switching) -----
        if (self.combo.currentText() == " purple-white" and self.StartStopPixel.isVisible() == True):
            self.workerrr = LiveLineThreadSwitch()
            self.workerrr.start()
            self.workerrr.LiveLineLabel1_1.connect(self.LiveLineLabel1_1_exec)
            self.workerrr.LiveLineLabel2_2.connect(self.LiveLineLabel2_2_exec)
            self.LiveLinePixel.show()
        if (self.combo.currentText() == " purple-white" and self.StartStopPixel.isVisible() == False):
            self.LiveLine1.setStyleSheet("QLabel { color : white; }")
            self.LiveLine2.setStyleSheet("QLabel { color : darkviolet; }")
        if (self.combo.currentText() == " white"):
            if (self.LiveLinePixel.isVisible() == True):
                self.workerrr.terminate()
                self.workerrr.quit()
            self.LiveLine1.setStyleSheet("QLabel { color : white; }")
            self.LiveLine2.setStyleSheet("QLabel { color : white; }")
            self.LiveLinePixel.hide()
        if (self.combo.currentText() == " purple"):
            if (self.LiveLinePixel.isVisible() == True):
                self.workerrr.terminate()
                self.workerrr.quit()
            self.LiveLine1.setStyleSheet("QLabel { color : darkviolet; }")
            self.LiveLine2.setStyleSheet("QLabel { color : darkviolet; }")
            self.LiveLinePixel.hide()
        if (self.combo.currentText() == " red"):
            if (self.LiveLinePixel.isVisible() == True):
                self.workerrr.terminate()
                self.workerrr.quit()
            self.LiveLine1.setStyleSheet("QLabel { color : red; }")
            self.LiveLine2.setStyleSheet("QLabel { color : red; }")
            self.LiveLinePixel.hide()
        if (self.combo.currentText() == " blue"):
            if (self.LiveLinePixel.isVisible() == True):
                self.workerrr.terminate()
                self.workerrr.quit()
            self.LiveLine1.setStyleSheet("QLabel { color : mediumblue; }")
            self.LiveLine2.setStyleSheet("QLabel { color : mediumblue; }")
            self.LiveLinePixel.hide()
        if (self.combo.currentText() == " light-blue"):
            if (self.LiveLinePixel.isVisible() == True):
                self.workerrr.terminate()
                self.workerrr.quit()
            self.LiveLine1.setStyleSheet("QLabel { color : aqua; }")
            self.LiveLine2.setStyleSheet("QLabel { color : aqua; }")
            self.LiveLinePixel.hide()
        if (self.combo.currentText() == " green"):
            if (self.LiveLinePixel.isVisible() == True):
                self.workerrr.terminate()
                self.workerrr.quit()
            self.LiveLine1.setStyleSheet("QLabel { color : lime; }")
            self.LiveLine2.setStyleSheet("QLabel { color : lime; }")
            self.LiveLinePixel.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 652)
        MainWindow.setStyleSheet("background-color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.headline = QLabel(self.centralwidget)
        self.headline.setText("Main-Hub")
        self.headline.setGeometry(310, 15, 250, 70)
        self.headline.setFont(QFont('Arial', 35))

        # ----- The background is made of various small pictures, forming one big background-image -----
        self.photoOben = QtWidgets.QLabel(self.centralwidget)
        self.photoOben.setGeometry(QtCore.QRect(0, 0, 852, 130))
        self.photoOben.setText("")
        self.photoOben.setPixmap(QtGui.QPixmap("./pics/OBEN.png"))
        self.photoOben.setScaledContents(True)
        self.photoOben.setObjectName("photoOben")
        self.photoLinksMitte = QtWidgets.QLabel(self.centralwidget)
        self.photoLinksMitte.setGeometry(QtCore.QRect(0, 130, 360, 280))
        self.photoLinksMitte.setText("")
        self.photoLinksMitte.setPixmap(QtGui.QPixmap("./pics/linksMitte.png"))
        self.photoLinksMitte.setScaledContents(True)
        self.photoLinksMitte.setObjectName("photoLinksMitte")
        self.photoRechtsMitte = QtWidgets.QLabel(self.centralwidget)
        self.photoRechtsMitte.setGeometry(QtCore.QRect(491, 130, 361, 280))
        self.photoRechtsMitte.setText("")
        self.photoRechtsMitte.setPixmap(QtGui.QPixmap("./pics/RechtsMitte.png"))
        self.photoRechtsMitte.setScaledContents(True)
        self.photoRechtsMitte.setObjectName("photoRechtsMitte")
        self.photoLinksUnten = QtWidgets.QLabel(self.centralwidget)
        self.photoLinksUnten.setGeometry(QtCore.QRect(0, 410, 240, 243))
        self.photoLinksUnten.setText("")
        self.photoLinksUnten.setPixmap(QtGui.QPixmap("./pics/linksUnten.png"))
        self.photoLinksUnten.setScaledContents(True)
        self.photoLinksUnten.setObjectName("photoLinksUnten")
        self.photoRechtsUnten = QtWidgets.QLabel(self.centralwidget)
        self.photoRechtsUnten.setGeometry(QtCore.QRect(611, 410, 241, 243))
        self.photoRechtsUnten.setText("")
        self.photoRechtsUnten.setPixmap(QtGui.QPixmap("./pics/RechtsUnten.png"))
        self.photoRechtsUnten.setScaledContents(True)
        self.photoRechtsUnten.setObjectName("photoRechtsUnten")
        self.photoUnterStart = QtWidgets.QLabel(self.centralwidget)
        self.photoUnterStart.setGeometry(QtCore.QRect(240, 561, 371, 92))
        self.photoUnterStart.setText("")
        self.photoUnterStart.setPixmap(QtGui.QPixmap("./pics/UnterStart.png"))
        self.photoUnterStart.setScaledContents(True)
        self.photoUnterStart.setObjectName("photoUnterStart")
        self.photoUnterTotal = QtWidgets.QLabel(self.centralwidget)
        self.photoUnterTotal.setGeometry(QtCore.QRect(360, 321, 131, 89))
        self.photoUnterTotal.setText("")
        self.photoUnterTotal.setPixmap(QtGui.QPixmap("./pics/UnterTotal.png"))
        self.photoUnterTotal.setScaledContents(True)
        self.photoUnterTotal.setObjectName("photoUnterTotal")
        self.photoUnterResidents = QtWidgets.QLabel(self.centralwidget)
        self.photoUnterResidents.setGeometry(QtCore.QRect(360, 201, 131, 49))
        self.photoUnterResidents.setText("")
        self.photoUnterResidents.setPixmap(QtGui.QPixmap("./pics/UnterResidents.png"))
        self.photoUnterResidents.setScaledContents(True)
        self.photoUnterResidents.setObjectName("photoUnterResidents")

        # ----- Defining the default LiveLines -----
        self.LiveLine1 = QLabel(self.centralwidget)
        self.LiveLine1.setText(" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /")
        self.LiveLine1.setGeometry(0, 582, 852, 25)
        self.LiveLine1.setFont(QFont('Arial', 21))
        self.LiveLine1.setStyleSheet("QLabel { color : darkviolet; }")
        self.LiveLine2 = QLabel(self.centralwidget)
        self.LiveLine2.setText("/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /")
        self.LiveLine2.setGeometry(2, 607, 847, 25)
        self.LiveLine2.setFont(QFont('Arial', 21))
        self.LiveLine2.setStyleSheet("QLabel {color : darkviolet; }")

        # ----- The LiveLinePixel and StartStopPixel are not visible for the user and just help the program running -----
        # ----- They are explained in the description of the comboPressed function -----
        self.LiveLinePixel = QLabel(self.centralwidget)
        self.LiveLinePixel.setText("")
        self.LiveLinePixel.setGeometry(0, 583, 1, 1)
        self.LiveLinePixel.setStyleSheet("background-color : black")
        self.LiveLinePixel.hide()
        self.StartStopPixel = QLabel(self.centralwidget)
        self.StartStopPixel.setText("")
        self.StartStopPixel.setGeometry(0, 585, 1, 1)
        self.StartStopPixel.setStyleSheet("background-color : black")
        self.StartStopPixel.hide()

        # ----- The combo box to choose colors for the LiveLine -----
        self.combo = QComboBox(self.centralwidget)
        self.combo.addItem(" purple")
        self.combo.addItem(" white")
        self.combo.addItem(" red")
        self.combo.addItem(" blue")
        self.combo.addItem(" light-blue")
        self.combo.addItem(" green")
        self.combo.addItem(" purple-white")
        self.combo.setGeometry(670, 545, 100, 30)
        self.combo.setStyleSheet("background-color : white;"
                                 "color : black;"
                                 "border :3px solid;"
                                 "border-top-color : black; "
                                 "border-left-color :black;"
                                 "border-right-color :black;"
                                 "border-bottom-color : black"
                                 )

        # ----- The "Go-Button" next to the combobox -----
        self.comboBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.comboPressed())
        self.comboBtn.setGeometry(777, 545, 70, 30)
        self.comboBtn.setText("Go")
        self.comboBtn.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color : white;"
                                    "border :3px solid ;"
                                    "border-top-color : black; "
                                    "border-left-color :black;"
                                    "border-right-color :black;"
                                    "border-bottom-color : black"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : white;"
                                    "border :3px solid ;"
                                    "border-top-color : white; "
                                    "border-left-color :white;"
                                    "border-right-color :white;"
                                    "border-bottom-color : white"
                                    "}"
                                    )

        # ----- The Start/Stop Button -----
        self.btnLiveLine = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickedBtnLiveLine())
        self.btnLiveLine.setText("Start / Stop")
        self.btnLiveLine.setFont(QFont('Arial', 8))
        self.btnLiveLine.setGeometry(40, 535, 150, 40)
        self.btnLiveLine.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : white;"
                                       "border :3px solid ;"
                                       "border-top-color : black; "
                                       "border-left-color :black;"
                                       "border-right-color :black;"
                                       "border-bottom-color : black"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : white;"
                                       "border :5px solid ;"
                                       "border-top-color : darkviolet; "
                                       "border-left-color :darkviolet;"
                                       "border-right-color :darkviolet;"
                                       "border-bottom-color : darkviolet"
                                       "}"
                                       )

        # ----- The Residents Button -----
        self.btn_Residents = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openResidents())
        self.btn_Residents.setGeometry(QtCore.QRect(360, 130, 131, 71))
        self.btn_Residents.setObjectName("btn_Residents")
        self.btn_Residents.setStyleSheet("QPushButton"
                                         "{"
                                         "background-color : white;"
                                         "border :3px solid ;"
                                         "border-top-color : black; "
                                         "border-left-color :black;"
                                         "border-right-color :black;"
                                         "border-bottom-color : black"
                                         "}"
                                         "QPushButton::pressed"
                                         "{"
                                         "background-color : white;"
                                         "border :7px solid ;"
                                         "border-top-color : darkviolet; "
                                         "border-left-color :darkviolet;"
                                         "border-right-color :darkviolet;"
                                         "border-bottom-color : darkviolet"
                                         "}"
                                         )

        # ----- The Total Button -----
        self.btn_Total = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openTotal())
        self.btn_Total.setGeometry(QtCore.QRect(360, 250, 131, 71))
        self.btn_Total.setObjectName("btn_Total")
        self.btn_Total.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : white;"
                                     "border :3px solid ;"
                                     "border-top-color : black; "
                                     "border-left-color :black;"
                                     "border-right-color :black;"
                                     "border-bottom-color : black"
                                     "}"
                                     "QPushButton::pressed"
                                     "{"
                                     "background-color : white;"
                                     "border :7px solid ;"
                                     "border-top-color : darkviolet; "
                                     "border-left-color :darkviolet;"
                                     "border-right-color :darkviolet;"
                                     "border-bottom-color : darkviolet"
                                     "}"
                                     )
        # ----- The Start Button (has no functionality yet) -----
        self.btn_Start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Start.setGeometry(QtCore.QRect(240, 410, 371, 151))
        self.btn_Start.setObjectName("btn_Start")
        self.btn_Start.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : white;"
                                     "border :3px solid ;"
                                     "border-top-color : black; "
                                     "border-left-color :black;"
                                     "border-right-color :black;"
                                     "border-bottom-color : black"
                                     "}"
                                     "QPushButton::pressed"
                                     "{"
                                     "background-color : white;"
                                     "border :7px solid ;"
                                     "border-top-color : darkviolet; "
                                     "border-left-color :darkviolet;"
                                     "border-right-color :darkviolet;"
                                     "border-bottom-color : darkviolet"
                                     "}")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # '-------------------------------------------------------------------------------------------------------------------'

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("OkaBf", "OkaBF"))
        self.btn_Residents.setText(_translate("MainWindow", "Residents"))
        self.btn_Total.setText(_translate("MainWindow", "Total"))
        self.btn_Start.setText(_translate("MainWindow", "Start"))



# ----- the actual functioning that is run when you start the program via the main-class -----
def runMain():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
