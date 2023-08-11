import sys
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsView
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt

class PlotlyTextWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = go.Layout(title='Plotly and PyQt')
        points = [(2, 3), (4, 8), (7, 5), (9, 2)]
        lines = [((2, 3), (4, 8)), ((4, 8), (7, 5)), ((7, 5), (9, 2))]

        fig = px.scatter()

        fig.add_scatter(x=[point[0] for point in points], y=[point[1] for point in points], mode='markers', name='Body', customdata=points, hovertemplate='(%{x}, %{y})')

        for line in lines:
            fig.add_scatter(x=[point[0] for point in line], y=[point[1] for point in line], mode='lines', name='Úsečky')

        plot_html = pio.to_html(fig, include_plotlyjs='cdn', full_html=False)

        self.web_view = QWebEngineView()
        self.web_view.setHtml(plot_html)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('Text Display with Plotly and PyQt')
        self.setGeometry(100, 100, 800, 600)

    def zoom(self, event):
        zoom_factor = 1.15 ** (event.angleDelta().y() / 120.0)
        self.graphics_view.scale(zoom_factor, zoom_factor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlotlyTextWindow()
    window.show()
    sys.exit(app.exec_())
