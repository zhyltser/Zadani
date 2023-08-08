import cv2
import numpy as np
import plotly.express as px
from PIL import Image

image_path = '/Users/sergzhyltsov/Downloads/bunka.jpeg'
image = cv2.imread(image_path)
resolution = Image.open(image_path)

np_image = np.array(image)
N = resolution.width
M = resolution.height

np_image = cv2.resize(image, dsize=(N, M), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('new-image.jpeg', np_image)

fig = px.imshow(np_image)
fig.update_layout(title='Image')
fig.show()
