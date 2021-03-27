import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from Country column to avoid errors
filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Sorting values and select first top 20 Countries
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Olympic 2016 Total Medals of 20 First Top Countries', xaxis_title="Country",
                   yaxis_title="Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='olympic-barchart.html')
