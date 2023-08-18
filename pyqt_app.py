from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QListWidget, QPushButton, QVBoxLayout, QWidget
import requests
from PyQt5.QtCore import pyqtSignal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.webEngineView = QWebEngineView(parent=self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(230, 10, 850, 811))
        self.webEngineView.setUrl(QtCore.QUrl("http://localhost:8050"))
        self.webEngineView.setObjectName("webEngineView")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 10, 221, 741))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    # def open_distance_mode(self):
    #     self.ui = MyWin()
    #     self.ui.show()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.webEngineView.focusProxy().installEventFilter(self)
        self.key_pressed = False

        self.ui.listWidget.itemDoubleClicked.connect(self.delete_item)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_C:
                self.key_pressed = True
            return super(MyWin, self).eventFilter(obj, event)
        elif event.type() == QtCore.QEvent.KeyRelease:
            if event.key() == QtCore.Qt.Key_C:
                self.key_pressed = False
            return super(MyWin, self).eventFilter(obj, event)
        elif obj is self.ui.webEngineView.focusProxy() and event.type() == event.MouseButtonPress and self.key_pressed:
            self.add_coordinates(event.pos())
        return super(MyWin, self).eventFilter(obj, event)

    def open_distance_mode(self):
        self.special_mode_active = True
        self.ui.webEngineView.page().runJavaScript('activateSpecialMode()')

    def add_coordinates(self, pos):
        item_text = f"X: {pos.x()}     Y: {pos.y()}"
        self.ui.listWidget.addItem(item_text)

    def delete_item(self, item):
        row = self.ui.listWidget.indexFromItem(item).row()
        self.ui.listWidget.takeItem(row)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWin()
    MainWindow.show()
    sys.exit(app.exec_())
