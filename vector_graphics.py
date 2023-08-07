import plotly.express as px

points = [(2, 3), (4, 8), (7, 5), (9, 2)]
lines = [((2, 3), (4, 8)), ((4, 8), (7, 5)), ((7, 5), (9, 2))]

fig = px.scatter()

fig.add_scatter(x=[point[0] for point in points], y=[point[1] for point in points], mode='markers', name='Body')

for line in lines:
    fig.add_scatter(x=[point[0] for point in line], y=[point[1] for point in line], mode='lines', name='Úsečky')

fig.update_layout(title='Vektorová grafika', xaxis_title='X', yaxis_title='Y')

fig.show()