# Read CSV data and take Timestamp, RPM, and TPS
# Convert timestamp to datetime
# Remove NaN Values
# Plot out RPM and TPS (x) against Datetime (y)
# Take those values and graph it via Plotly

import pandas as pd
import plotly.express as px

# All Data
data = pd.read_csv("can_data.csv", usecols=['timestamp', 'RPM', 'TPS'])

# Convert timestamp to datetime
data['Time'] = pd.to_datetime(data['timestamp'], unit='s')

# Remove Null Values
data = data.dropna();

# Plot Dataframes as a line graph
rpmPlot = px.line(data, x = 'Time', y = "RPM", title = "RPM over Time");
tpsPlot = px.line(data, x = 'Time', y = "TPS", title = "TPS over Time");

# # Show Data on Graph
rpmPlot.show()
tpsPlot.show()