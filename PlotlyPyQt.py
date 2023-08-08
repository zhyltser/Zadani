import sys
import plotly.graph_objs as go
import plotly.io as pio
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class PlotlyTextWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a Plotly figure with a text annotation
        layout = go.Layout(title='Plotly and PyQt')
        fig = go.Figure(layout=layout)
        fig.add_annotation(
            text="",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=24)
        )

        # Convert the Plotly figure to HTML including Plotly.js
        plot_html = pio.to_html(fig, include_plotlyjs='cdn', full_html=False)

        # Create a PyQt widget for displaying HTML (WebView)
        self.web_view = QWebEngineView()
        self.web_view.setHtml(plot_html)

        # Set up the main window layoutdd
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('Text Display with Plotly and PyQt')
        self.setGeometry(100, 100, 800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlotlyTextWindow()
    window.show()
    sys.exit(app.exec_())