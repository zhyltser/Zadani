from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QListWidget, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        layout = QVBoxLayout()

                
        self.webEngineView = QWebEngineView(parent=self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(230, 10, 850, 811))
        self.webEngineView.setUrl(QtCore.QUrl("http://localhost:8050"))
        self.webEngineView.setObjectName("webEngineView")

        layout.addWidget(self.webEngineView)

        self.distance_button = QPushButton("Distance", parent=self.centralwidget)
        self.distance_button.clicked.connect(self.toggle_distance_mode)
        self.distance_button.setFixedHeight(30)  # Set the button height
        layout.addWidget(self.distance_button)

        self.listWidget = QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 25, 221, 741))
        self.listWidget.setObjectName("listWidget")
        layout.addWidget(self.listWidget)

        # self.centralwidget.setLayout(layout)

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

        self.is_distance_mode = False
        self.first_click = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def toggle_distance_mode(self):
        self.is_distance_mode = not self.is_distance_mode
        if self.is_distance_mode:
            self.distance_button.setStyleSheet("background-color: lightgreen;")
            self.clear_lines()  # Clear the previous lines
            self.open_distance_mode()  # Start the drawing mode
        else:
            self.distance_button.setStyleSheet("")
            self.close_distance_mode()  # Stop the drawing mode

    def clear_lines(self):
        self.webEngineView.page().runJavaScript("document.querySelectorAll('line').forEach(function(el) { el.remove(); });")

    def open_distance_mode(self):
        self.webEngineView.page().runJavaScript("""
            document.addEventListener('click', function(e) {
                if (window.distanceMode) {
                    if (!window.firstClick) {
                        window.firstClick = { x: e.clientX, y: e.clientY };
                    } else {
                        var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                        line.setAttribute('x1', window.firstClick.x);
                        line.setAttribute('y1', window.firstClick.y);
                        line.setAttribute('x2', e.clientX);
                        line.setAttribute('y2', e.clientY);
                        line.setAttribute('stroke', 'red');
                        line.setAttribute('stroke-width', '2');
                        document.querySelector('svg').appendChild(line);
                        window.firstClick = null;
                    }
                }
            });
        """)
        self.webEngineView.page().runJavaScript("window.distanceMode = true;")

    def close_distance_mode(self):
        self.webEngineView.page().runJavaScript("window.distanceMode = false;")


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
        return super(MyWin, self).eventFilter(obj, event)

    def add_coordinates(self, pos):
        item_text = f"X: {pos.x()}     Y: {pos.y()}"
        self.ui.listWidget.addItem(item_text)

    def delete_item(self, item):
        row = self.ui.listWidget.indexFromItem(item).row()
        self.ui.listWidget.takeItem(row)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWin()
    MainWindow.show()
    sys.exit(app.exec_())


