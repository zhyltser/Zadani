import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget, QGraphicsPathItem, QGraphicsEllipseItem, QGraphicsLineItem
from PyQt5.QtGui import QPixmap, QImage, QPen, QFont, QPainterPath
from PyQt5.QtCore import Qt, QPointF

class InteractiveLine(QGraphicsPathItem):
    def __init__(self, path, pen):
        super().__init__()
        self.setPath(path)
        self.setPen(pen)
        self.setFlag(self.ItemIsSelectable, True)
        self.setFlag(self.ItemIsFocusable, True)

    def mousePressEvent(self, event):
        # Handle the click event on the line
        print("Line clicked!")

class ImageProcessor(QMainWindow):
    def __init__(self):
        super().__init__()
            
        self.setWindowTitle("Image Processor")

        self.image_path = 'new-image.jpeg'
        self.image = cv2.imread(self.image_path)
        self.resolution = QImage(self.image_path)

        self.np_image = np.array(self.image)
        self.N = self.resolution.width()
        self.M = self.resolution.height()

        self.np_image = cv2.resize(self.image, dsize=(self.N, self.M), interpolation=cv2.INTER_CUBIC)

        self.lines_coordinates = [
            [(100, 50), (900, 1000)],
            [(50, 900), (980, 400)]
        ]

        self.grid_spacing = 100  # Adjust the grid spacing as needed

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)


        self.graphics_view = QGraphicsView(self)
        layout.addWidget(self.graphics_view)
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.graphics_scene)
        self.graphics_view.setDragMode(QGraphicsView.ScrollHandDrag)

        self.add_image()
        self.add_lines()
        self.add_grid()

        # Connect wheel event to custom zoom function
        self.graphics_view.wheelEvent = self.zoom

        self.show()

    def add_image(self):
        pixmap = QPixmap.fromImage(QImage(self.np_image.data, self.N, self.M, self.N * 3, QImage.Format_RGB888))
        self.graphics_scene.addPixmap(pixmap)

    def add_lines(self):
        pen = QPen(Qt.red)
        pen.setWidth(3)
        for coordinates in self.lines_coordinates:
            x0, y0 = coordinates[0]
            x1, y1 = coordinates[1]
            path = QPainterPath(QPointF(x0, y0))
            path.lineTo(x1, y1)
            line_item = InteractiveLine(path, pen)
            self.graphics_scene.addItem(line_item)

    def add_grid(self):
        pen = QPen(Qt.lightGray, 2, Qt.DashLine)
        font = QFont("Arial", 20)
        
        for x in range(self.grid_spacing, self.N, self.grid_spacing):
            self.graphics_scene.addLine(x, 0, x, self.M, pen)
            text_item = self.graphics_scene.addText(str(x), font)
            text_item.setDefaultTextColor(Qt.white)
            text_item.setPos(x, -20)
        
        for y in range(self.grid_spacing, self.M, self.grid_spacing):
            self.graphics_scene.addLine(0, y, self.N, y, pen)
            text_item = self.graphics_scene.addText(str(y), font)
            text_item.setDefaultTextColor(Qt.white)
            text_item.setPos(-40, y)

    def zoom(self, event):
        # Custom zoom function for the QGraphicsView
        zoom_factor = 1.15 ** (event.angleDelta().y() / 120.0)
        self.graphics_view.scale(zoom_factor, zoom_factor)

    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.statusBar().showMessage(f"Coordinates: ({x}, {y})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ImageProcessor()
    sys.exit(app.exec_())
