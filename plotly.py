import cv2
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from PIL import Image

image_path = 'new-image.jpeg'
image = cv2.imread(image_path)
resolution = Image.open(image_path)

np_image = np.array(image)
N = resolution.width
M = resolution.height

np_image = cv2.resize(image, dsize=(N, M), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('new-image.jpeg', np_image)

lines_coordinates = [
    [(100, 50), (900, 1000)],
    [(50, 900), (980, 400)],
    [(322, 121), (328, 126)]
]

fig = go.Figure()

config = dict({'scrollZoom': True})

# Add the image to the figure
fig.add_trace(go.Image(z=np_image))


fig.update_layout(
    title='Image',
    shapes=[],
    annotations=[])


def add_line_shape(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    fig.add_shape(type='line',
                  x0=x0, y0=y0,
                  x1=x1, y1=y1,
                  line=dict(color='red', width=2))

# Add the specified lines to the figure
for coordinates in lines_coordinates:
    add_line_shape(coordinates)

fig.update_layout(dragmode='pan')
fig.show(config=config)


