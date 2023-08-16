import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import base64
import cv2
import numpy as np
from PIL import Image

app = dash.Dash(__name__)

# Load your image and convert it to base64
# image_path = 'im.jpeg'
# with open(image_path, "rb") as image_file:
#     encoded_image = base64.b64encode(image_file.read()).decode()

image_path = 'im.jpeg'
image = cv2.imread(image_path)
np_image = cv2.resize(image, dsize=(1000, 1283), interpolation=cv2.INTER_CUBIC)

app.layout = html.Div([
    # html.Img(id='image', style={'width': '20%'}, src='https://www.themoviedb.org/t/p/original/fpIoKtHsr9uwZO2dTH7sx9fpKMz.jpg'),
    dcc.Graph(figure=go.Figure().add_trace(go.Image(z=np_image)).add_shape(type='line', x0=100,y0=50,x1=900,y1=70, line=dict(color='red', width=3)), config={'scrollZoom': True}, style={'width': '200vh', 'height': '100vh'}),
    # dcc.Graph(id='plot', config={'scrollZoom': True}, style={'width': '200vh', 'height': '100vh'}),
    # dcc.Graph(
    #     figure={
    #         "data": [
    #             {"x": [1, 2, 3], "y": [4, 1, 2], "type":  "bar"},
    #             {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar"},
    #         ],
    #         "layout": {
    #             "title": "My Dash Graph",
    #             "height": 700,  # px
    #         },
    #     },
    #     config={'scrollZoom': True}
    # )
])

@app.callback(
    Output('plot', 'figure'),
    [Input('plot', 'relayoutData')]
)

def update_plot_zoom(relayout_data):
    # zoom = relayout_data.get('yaxis.range', None)

    # image = cv2.imread(image_path)
    # resolution = Image.open(image_path)

    # np_image = np.array(image)
    # N = resolution.width
    # M = resolution.height

    # np_image = cv2.resize(image, dsize=(N, M), interpolation=cv2.INTER_CUBIC)

    # lines_coordinates = [
    #     [(100, 50), (900, 1000)],
    #     [(50, 900), (980, 400)],
    #     [(322, 121), (328, 126)]
    # ]

    # fig = go.Figure()

    # # Add the specified lines to the figure
    # for coordinates in lines_coordinates:
    #     fig.add_shape(type='line', x0=coordinates[0][0], y0=coordinates[0][1],
    #                   x1=coordinates[1][0], y1=coordinates[1][1],
    #                   line=dict(color='red', width=2))

    # # Add the image to the figure
    # fig.add_trace(go.Image(z=np_image, x=0, y=0, x1=N, y1=M, opacity=0.5))

    # fig.update_layout(
    #     title='Image',
    #     shapes=[],
    #     annotations=[],
    #     yaxis=dict(range=zoom),
    #     height='100vh'  # Set the height of the figure to 100% of viewport height
    # )
    return 0


if __name__ == '__main__':
    app.run_server(debug=False)

########################################################
########################################################
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output
# import base64
# import cv2
# import numpy as np
# from PIL import Image

# app = dash.Dash(__name__)

# # Load your image and convert it to base64
# image_path = 'im.jpeg'
# with open(image_path, "rb") as image_file:
#     encoded_image = base64.b64encode(image_file.read()).decode()

# app.layout = html.Div([
#     dcc.Graph(id='plot', config={'scrollZoom': True}, style={'width': '200vh', 'height': '100vh'}),
#     html.Img(id='image', style={'width': '100%'}),
# ])

# @app.callback(
#     Output('plot', 'figure'),
#     [Input('plot', 'relayoutData')]
# )
# def update_plot_zoom(relayout_data):
#     zoom = relayout_data.get('yaxis.range', None)

#     image = cv2.imread(image_path)
#     resolution = Image.open(image_path)

#     np_image = np.array(image)
#     N = resolution.width
#     M = resolution.height

#     np_image = cv2.resize(image, dsize=(N, M), interpolation=cv2.INTER_CUBIC)

#     lines_coordinates = [
#         [(100, 50), (900, 1000)],
#         [(50, 900), (980, 400)],
#         [(322, 121), (328, 126)]
#     ]

#     fig = go.Figure()

#     # Add the specified lines to the figure
#     for coordinates in lines_coordinates:
#         fig.add_shape(type='line', x0=coordinates[0][0], y0=coordinates[0][1],
#                       x1=coordinates[1][0], y1=coordinates[1][1],
#                       line=dict(color='red', width=2))

#     # Add the image to the figure
#     fig.add_trace(go.Image(z=np_image, x=0, y=0, x1=N, y1=M, opacity=0.5))

#     # Add a scatter plot to the figure (example)
#     scatter_data = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='markers', marker=dict(size=10))
#     fig.add_trace(scatter_data)

#     fig.update_layout(
#         title='Image and Scatter Plot',  # Updated title
#         shapes=[],
#         annotations=[],
#         yaxis=dict(range=zoom),
#         height='100vh'  # Set the height of the figure to 100% of viewport height
#     )

#     return fig

# if __name__ == '__main__':
#     app.run_server(debug=False)


# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output
# import base64
# import cv2
# import numpy as np
# from PIL import Image

# app = dash.Dash(__name__)

# # Load your image and convert it to base64
# image_path = 'im.jpeg'
# with open(image_path, "rb") as image_file:
#     encoded_image = base64.b64encode(image_file.read()).decode()

# app.layout = html.Div([
#     dcc.Graph(id='plot'),
# ])

# @app.callback(
#     Output('plot', 'figure'),
#     [Input('plot', 'relayoutData')]
# )
# def update_plot_zoom(relayout_data):
#     zoom = relayout_data.get('xaxis.range', None)

#     image = cv2.imread(image_path)
#     resolution = Image.open(image_path)

#     np_image = np.array(image)
#     N = resolution.width
#     M = resolution.height

#     np_image = cv2.resize(image, dsize=(N, M), interpolation=cv2.INTER_CUBIC)

#     lines_coordinates = [
#         [(100, 50), (900, 1000)],
#         [(50, 900), (980, 400)],
#         [(322, 121), (328, 126)]
#     ]

#     fig = go.Figure()

#     # Add the specified lines to the figure
#     for coordinates in lines_coordinates:
#         fig.add_shape(type='line', x0=coordinates[0][0], y0=coordinates[0][1],
#                       x1=coordinates[1][0], y1=coordinates[1][1],
#                       line=dict(color='red', width=2))

#     # Add the image to the figure
#     fig.add_trace(go.Image(z=np_image, x=0, y=0, x1=N, y1=M, opacity=0.5))

#     fig.update_layout(
#         title='Image',
#         shapes=[],
#         annotations=[],
#         xaxis=dict(range=zoom),
#     )

#     return fig

# if __name__ == '__main__':
#     app.run_server(debug=False)

