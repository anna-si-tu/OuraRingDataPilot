import pandas as pd

nuanic_data = pd.read_csv("data/nuanic.csv")

def convert_nuanic_eda(data):
    #only keep time and eda columns
    data = data[['time', 'eda']]
    #convert eda to conductance
    data['eda_conductance'] = 1 / data['eda']*1000000
    #time is in UTC, convert to US/Pacific
    data['time'] = pd.to_datetime(data['time']).dt.tz_convert('US/Pacific')
    return data

converted_nuanic_data = convert_nuanic_eda(nuanic_data)

print(converted_nuanic_data.head())