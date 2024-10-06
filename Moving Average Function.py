import plotly.graph_objs as go

def moving_average(data, window_size):
    moving_avg = [] # empty list to store thw calculated moving averages
    for i in range(len(data) - window_size + 1): # iterates i from 0 to 7 (8 times)
        window = data[i:i + window_size] # Iterates over the data and extracts a slice of the list that is window_size long.
        window_avg = sum(window) / window_size # Calculate the average of the slice extracted
        moving_avg.append(window_avg) # Appended it to the list
    return moving_avg

# Sample data
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Adjust window size
window_size = 3
moving_avg = moving_average(data, window_size)

trace_original = go.Scatter(
    x = list(range(1, len(data) + 1)),
    y = data,
    mode = 'lines+markers',
    name = 'Original Data'
)

trace_moving_avg = go.Scatter(
    x = list(range(window_size, len(data) + 1)),
    y = moving_avg,
    mode = 'lines+markers',
    name = f'Moving Average (window={window_size})'
)

layout = go.Layout(
    title = 'Moving Average Plot',
    xaxis = {'title': 'Index'},
    yaxis = {'title': 'Value'}
)

fig = go.Figure(data=[trace_original, trace_moving_avg], layout=layout)
fig.show()