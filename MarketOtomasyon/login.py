from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 826)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:24px;\n"
"    \n"
"}\n"
"QFrame\n"
"{\n"
"    background:rgb(37, 42, 52);\n"
"    border-radius:15px\n"
"}\n"
"QPushButton\n"
"{\n"
"background: rgb(255, 46, 99);\n"
"border-radius:60px;\n"
"}\n"
"QToolButton\n"
"{\n"
"background:rgb(255, 46, 99);\n"
"border-radius:60px;\n"
"}\n"
"QLabel\n"
"{\n"
"color:rgb(234, 234, 234);\n"
"}\n"
"QPushButton\n"
"{\n"
"color:rgb(234, 234, 234);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color: #rgb(37, 42, 52);\n"
"border-radius:15px;\n"
"background:rgb(8, 217, 214);\n"
"}\n"
"QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 100, 521, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 360, 141, 51))
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 520, 391, 61))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 280, 381, 31))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 410, 381, 41))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 141, 51))
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(200, 90, 141, 51))
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(360, 40, 121, 121))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resimler/Sample_User_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "LOGIN HERE"))