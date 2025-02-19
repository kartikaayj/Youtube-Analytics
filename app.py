import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Initialize Dash App
app = dash.Dash(__name__)

# Sample Data
video_stats = pd.DataFrame({
    "Keyword": ["Tech", "Food", "Travel", "Tech", "Food"],
    "LikesPer1k": [50, 30, 70, 90, 20],
    "CommentsPer1k": [5, 10, 7, 12, 3],
    "Views": [100000, 200000, 150000, 300000, 50000]
})

# Plotly Chart
fig = px.scatter(
    video_stats, x="LikesPer1k", y="CommentsPer1k",
    color="Keyword", size="Views", size_max=70, opacity=0.5,
    title="Likes VS Comments per 1k Views"
)

# App Layout
app.layout = html.Div(children=[
    html.H1("Video Stats Dashboard"),
    dcc.Graph(figure=fig)
])

# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
