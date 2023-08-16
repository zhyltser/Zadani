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

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output
# import base64

# app = dash.Dash(__name__)

# # Load your image and convert it to base64
# image_path = 'im.jpeg'
# with open(image_path, "rb") as image_file:
#     encoded_image = base64.b64encode(image_file.read()).decode()

# app.layout = html.Div([
#     dcc.Graph(id='plot'),
#     html.Img(id='image', src='data:image/jpg;base64,{}'.format(encoded_image), style={'width': '100%'}),
# ])

# @app.callback(
#     Output('plot', 'figure'),
#     [Input('plot', 'relayoutData')]
# )
# def update_plot_zoom(relayout_data):
#     zoom = relayout_data.get('xaxis.range', None)

#     fig = go.Figure()

#     # Example plotly figure update
#     figure = {
#         'data': [go.Scatter(x=[1, 2, 3], y=[4, 5, 6])],
#         'layout': {
#             'xaxis': {'range': zoom},
#             'yaxis': {'title': 'Y-Axis'},
#         }
#     }

#     return figure

# if __name__ == '__main__':
#     app.run_server(debug=False)
