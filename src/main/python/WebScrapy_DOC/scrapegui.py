from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 616)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SCgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SCgroupBox.setGeometry(QtCore.QRect(30, 20, 341, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.SCgroupBox.setFont(font)
        self.SCgroupBox.setObjectName("SCgroupBox")
        self.scFilebox = QtWidgets.QLineEdit(self.SCgroupBox)
        self.scFilebox.setEnabled(False)
        self.scFilebox.setGeometry(QtCore.QRect(10, 111, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.scFilebox.setFont(font)
        self.scFilebox.setObjectName("scFilebox")
        self.scFilebtn = QtWidgets.QPushButton(self.SCgroupBox)
        self.scFilebtn.setEnabled(False)
        self.scFilebtn.setGeometry(QtCore.QRect(280, 110, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.scFilebtn.setFont(font)
        self.scFilebtn.setObjectName("scFilebtn")
        self.fileUpldlbl = QtWidgets.QLabel(self.SCgroupBox)
        self.fileUpldlbl.setEnabled(True)
        self.fileUpldlbl.setGeometry(QtCore.QRect(12, 81, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.fileUpldlbl.setFont(font)
        self.fileUpldlbl.setWordWrap(True)
        self.fileUpldlbl.setObjectName("fileUpldlbl")
        self.freeformSrch = QtWidgets.QPlainTextEdit(self.SCgroupBox)
        self.freeformSrch.setEnabled(False)
        self.freeformSrch.setGeometry(QtCore.QRect(10, 176, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.freeformSrch.setFont(font)
        self.freeformSrch.setObjectName("freeformSrch")
        self.frame = QtWidgets.QFrame(self.SCgroupBox)
        self.frame.setGeometry(QtCore.QRect(9, 25, 321, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.upldRdBtn = QtWidgets.QRadioButton(self.frame)
        self.upldRdBtn.setGeometry(QtCore.QRect(209, 4, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.upldRdBtn.setFont(font)
        self.upldRdBtn.setObjectName("upldRdBtn")
        self.freeformRdBtn = QtWidgets.QRadioButton(self.frame)
        self.freeformRdBtn.setGeometry(QtCore.QRect(209, 28, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.freeformRdBtn.setFont(font)
        self.freeformRdBtn.setObjectName("freeformRdBtn")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 5, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.manEntrylbl = QtWidgets.QLabel(self.SCgroupBox)
        self.manEntrylbl.setEnabled(True)
        self.manEntrylbl.setGeometry(QtCore.QRect(12, 146, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.manEntrylbl.setFont(font)
        self.manEntrylbl.setWordWrap(True)
        self.manEntrylbl.setObjectName("manEntrylbl")
        self.startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.startbtn.setGeometry(QtCore.QRect(330, 290, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.startbtn.setFont(font)
        self.startbtn.setStyleSheet("background-color: rgb(16, 88, 82);\n"
                                    "color: rgb(255, 255, 255);")
        self.startbtn.setFlat(False)
        self.startbtn.setObjectName("startbtn")
        self.MFgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.MFgroupBox.setGeometry(QtCore.QRect(390, 20, 341, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.MFgroupBox.setFont(font)
        self.MFgroupBox.setObjectName("MFgroupBox")
        self.mFilebox = QtWidgets.QLineEdit(self.MFgroupBox)
        self.mFilebox.setGeometry(QtCore.QRect(10, 111, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.mFilebox.setFont(font)
        self.mFilebox.setObjectName("mFilebox")
        self.mFilebtn = QtWidgets.QPushButton(self.MFgroupBox)
        self.mFilebtn.setGeometry(QtCore.QRect(280, 110, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.mFilebtn.setFont(font)
        self.mFilebtn.setObjectName("mFilebtn")
        self.mstrFilelbl = QtWidgets.QLabel(self.MFgroupBox)
        self.mstrFilelbl.setEnabled(True)
        self.mstrFilelbl.setGeometry(QtCore.QRect(11, 71, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.mstrFilelbl.setFont(font)
        self.mstrFilelbl.setWordWrap(True)
        self.mstrFilelbl.setObjectName("mstrFilelbl")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 350, 461, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.scrapingDialogue = QtWidgets.QTextEdit(self.groupBox)
        self.scrapingDialogue.setGeometry(QtCore.QRect(10, 20, 441, 191))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.scrapingDialogue.setFont(font)
        self.scrapingDialogue.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrapingDialogue.setObjectName("scrapingDialogue")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 350, 221, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblRuntime = QtWidgets.QLabel(self.groupBox_2)
        self.lblRuntime.setGeometry(QtCore.QRect(10, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lblRuntime.setFont(font)
        self.lblRuntime.setObjectName("lblRuntime")
        self.txtRuntime = QtWidgets.QLabel(self.groupBox_2)
        self.txtRuntime.setGeometry(QtCore.QRect(140, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.txtRuntime.setFont(font)
        self.txtRuntime.setStyleSheet("color:  rgb(198, 45, 66)")
        self.txtRuntime.setText("")
        self.txtRuntime.setObjectName("txtRuntime")
        self.lblSrchItm = QtWidgets.QLabel(self.groupBox_2)
        self.lblSrchItm.setGeometry(QtCore.QRect(10, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lblSrchItm.setFont(font)
        self.lblSrchItm.setObjectName("lblSrchItm")
        self.txtSrchItm = QtWidgets.QLabel(self.groupBox_2)
        self.txtSrchItm.setGeometry(QtCore.QRect(140, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.txtSrchItm.setFont(font)
        self.txtSrchItm.setStyleSheet("color:  rgb(198, 45, 66)")
        self.txtSrchItm.setText("")
        self.txtSrchItm.setObjectName("txtSrchItm")
        self.txtScrapes = QtWidgets.QLabel(self.groupBox_2)
        self.txtScrapes.setGeometry(QtCore.QRect(140, 102, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.txtScrapes.setFont(font)
        self.txtScrapes.setStyleSheet("color:  rgb(16, 88, 82)")
        self.txtScrapes.setText("")
        self.txtScrapes.setObjectName("txtScrapes")
        self.lblScrapes = QtWidgets.QLabel(self.groupBox_2)
        self.lblScrapes.setGeometry(QtCore.QRect(10, 102, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lblScrapes.setFont(font)
        self.lblScrapes.setObjectName("lblScrapes")
        self.txtCompleted = QtWidgets.QLabel(self.groupBox_2)
        self.txtCompleted.setGeometry(QtCore.QRect(140, 134, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.txtCompleted.setFont(font)
        self.txtCompleted.setStyleSheet("color:  rgb(198, 45, 66)")
        self.txtCompleted.setText("")
        self.txtCompleted.setObjectName("txtCompleted")
        self.lblCompleted = QtWidgets.QLabel(self.groupBox_2)
        self.lblCompleted.setGeometry(QtCore.QRect(10, 134, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lblCompleted.setFont(font)
        self.lblCompleted.setObjectName("lblCompleted")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(31, 330, 701, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.startbtn.raise_()
        self.MFgroupBox.raise_()
        self.SCgroupBox.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "Division of Corporations - "
                                             "Entity Search"))
        self.SCgroupBox.setTitle(
            _translate("MainWindow", "Search Criteria Data"))
        self.scFilebtn.setText(_translate("MainWindow", "File"))
        self.fileUpldlbl.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span "
                                            "style=\" text-decoration: "
                                            "underline;\">File "
                                            "Upload</span><span style=\" "
                                            "font-style:italic;\"> (all "
                                            "uploaded data needs to be "
                                            "located on first Excel sheet "
                                            "within first "
                                            "column)</span><br/></p></body></html>"))
        self.upldRdBtn.setText(_translate("MainWindow", "File Upload"))
        self.freeformRdBtn.setText(_translate("MainWindow", "Manual Entry"))
        self.label.setText(_translate("MainWindow",
                                      "Do you want to upload an Excel file or "
                                      "do a manual search?"))
        self.manEntrylbl.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span "
                                            "style=\" text-decoration: "
                                            "underline;\">Manual "
                                            "Entry</span><span style=\" "
                                            "font-style:italic;\"> (for "
                                            "multiple search items, "
                                            "use a &quot;,&quot; to separate, "
                                            "e.g. Dog, Cat, "
                                            "Bird)<br/></span></p></body></html>"))
        self.startbtn.setText(_translate("MainWindow", "Start Scraping"))
        self.MFgroupBox.setTitle(_translate("MainWindow", "Master File"))
        self.mFilebtn.setText(_translate("MainWindow", "File"))
        self.mstrFilelbl.setText(_translate("MainWindow",
                                            "Upload an Excel file (scraper "
                                            "will append new data to any "
                                            "existing data within file)"))
        self.groupBox.setTitle(_translate("MainWindow", "Scraping Dialogue"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Scraping Stats"))
        self.lblRuntime.setText(_translate("MainWindow", "Status:"))
        self.lblSrchItm.setText(_translate("MainWindow", "# of Search items:"))
        self.lblScrapes.setText(
            _translate("MainWindow", "# of Successful Scrapes:"))
        self.lblCompleted.setText(_translate("MainWindow", "% Completed:"))