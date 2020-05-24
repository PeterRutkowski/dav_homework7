from utils import import_temperatures, save_figure
import plotly.express as px

df = import_temperatures('France')

fig = px.scatter(df, x="year", y="temp")

fig.update_layout(
    title = 'Average temperature in France',
    titlefont = dict(size=14),
    title_x=0.5,
    autosize = False,
    width=650,
    height=500,
    xaxis=dict(title='Year', titlefont = dict(size=12)),
    yaxis=dict(title='Average temperature (Celsius)', titlefont = dict(size=12))
)

save_figure('scatter_france', fig)