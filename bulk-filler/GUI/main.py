import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from index import App_Window , MainWindowBase_Class

def launchAPP():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindowBase_Class()
    ui = App_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    launchAPP()
