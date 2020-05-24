from utils import import_temperatures, save_figure
import plotly.express as px

df = import_temperatures('Poland')

fig = px.scatter(df, x="year", y="temp")

fig.update_layout(
    title = 'Average temperature in Poland',
    titlefont = dict(size=14),
    title_x=0.5,
    autosize = False,
    width=800,
    height=600,
    xaxis=dict(title='Year', titlefont = dict(size=12)),
    yaxis=dict(title='Average temperature (Celsius)', titlefont = dict(size=12))
)

save_figure('scatter_poland', fig)