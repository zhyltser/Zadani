import cv2
import numpy as np
import plotly
# import plotly.express as px
import plotly.express as px

N = 200
M = 300
numpy_image = np.random.randint(0, 256, size=(N, M, 3), dtype=np.uint8)

fig = px.imshow(numpy_image)
fig.update_layout(title='Barevný obrázek')
fig.show()