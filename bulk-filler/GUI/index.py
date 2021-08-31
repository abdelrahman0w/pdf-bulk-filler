import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic

MainWindowUI_Class, MainWindowBase_Class = uic.loadUiType(
    os.path.join(sys.path[0], 'main_screen.ui'))

class App_Window(MainWindowUI_Class, MainWindowBase_Class):
    pass


