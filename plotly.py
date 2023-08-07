import cv2
import numpy as np
import plotly.express as px

image_path = '/Users/sergzhyltsov/Downloads/3D4A6853.jpg'  
loaded_image = cv2.imread(image_path)

numpy_image = np.array(loaded_image)

fig = px.imshow(numpy_image)
fig.update_layout(title='Image')
fig.show()

