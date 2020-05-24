import pandas as pd
import numpy as np
from sys import argv

def save_figure(filename, fig):
    if len(argv) > 1:
        if argv[1] == '0':
            fig.show()
        else:
            fig.write_html('plots/%s.html'%(filename), include_plotlyjs='cdn')
            print('plots/%s.html'%(filename))
    else:
        fig.write_html('plots/%s.html' % (filename), include_plotlyjs='cdn')
        print('plots/%s.html' % (filename))

def import_temperatures(country):
    data = pd.read_csv('data/temperatures_clean.csv')[['Country', 'year', 'AverageTemperatureCelsius']]
    data = np.asarray(data)
    country_list, df = [], []
    for el in data:
        if el[0] == country:
            country_list.append(el)
    country_list = np.asarray(country_list)
    country_years = np.unique(country_list[:,1])

    for year in country_years:
        year_temp_sum = 0
        year_quantity = 0
        for el in country_list:
            if el[1]==year:
                year_temp_sum += el[2]
                year_quantity += 1
        av_temp = year_temp_sum/year_quantity
        df.append([country, year, av_temp])

    return pd.DataFrame(df, columns=['country', 'year', 'temp'])