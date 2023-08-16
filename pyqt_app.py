import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class PyQtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Dash Image and Plot App")
        self.setGeometry(0, 0, 800, 600)  # Set the window size

        layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.load_dash_app()

    def load_dash_app(self):
        self.web_view.setUrl(QUrl("http://localhost:8050"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pyqt_app = PyQtApp()
    pyqt_app.showMaximized()  # Show the window maximized
    sys.exit(app.exec_())

    sys.exit(app.exec_())
