import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# Preparing data
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Actual Max Temp')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Actual Min Temp')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Actual Mean Temp')
data = [trace1, trace2, trace3]


# Preparing layout
layout = go.Layout(title='Actual Max, Min, and Mean Temperatures From 2014-07-01 to 2015-06-30', xaxis_title="Date",
                   yaxis_title="Actual Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weather-multilinechart.html')