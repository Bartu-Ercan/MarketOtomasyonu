import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import *
from login import *

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


import sqlite3

sys.exit(uygulama.exec_())