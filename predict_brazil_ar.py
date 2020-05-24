from statsmodels.tsa.ar_model import AutoReg
from utils import import_temperatures, save_figure
import numpy as np
import plotly.express as px
import pandas as pd

df = import_temperatures('Brazil')
x = list(df['year'])
y = list(np.asarray(df['temp']))

for i in range(250):
    if (i+1)%50 == 0:
        print('%d/250'%(i+1))
    model = AutoReg(y, lags=1)
    model_fit = model.fit()
    output = model_fit.predict(len(y),len(y))
    y.append(output[0])

x = x + [2014+i for i in range(250)]
df = []
for i in range(len(x)):
    df.append([x[i],y[i]])
df = pd.DataFrame(df, columns=['x','y'])
fig = px.line(df, x='x', y='y')

fig.update_layout(
    title = 'The prediction of average temperature in Brazil using AR model',
    titlefont = dict(size=14),
    title_x=0.5,
    autosize = False,
    width=650,
    height=500,
    xaxis=dict(title='Year', titlefont = dict(size=12)),
    yaxis=dict(title='Average temperature (Celsius)', titlefont = dict(size=12))
)

save_figure('predict_brazil_ar', fig)