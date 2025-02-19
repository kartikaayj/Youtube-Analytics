import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Load Dataset
video_stats = pd.read_csv(r"C:\Users\karti\OneDrive\Desktop\Project Prototype\Youtube\Data set\videos-stats.csv")

# Data Preprocessing
video_stats.dropna(inplace=True)
video_stats["LikesPer1k"] = round(video_stats["Likes"] / (video_stats["Views"] / 1000), 2)
video_stats["CommentsPer1k"] = round(video_stats["Comments"] / (video_stats["Views"] / 1000), 2)
video_stats["TitleLen"] = video_stats["Title"].str.len()
video_stats["PubYear"] = video_stats["Published At"].astype(str).str[:4]

# 📊 1. Bar Chart - Number of Videos per Year
fig1 = px.bar(
    video_stats.groupby("PubYear").size().reset_index(name="Video Count"), 
    x="PubYear", 
    y="Video Count", 
    title="Number of Videos by Year", 
    labels={"PubYear": "Publication Year", "Video Count": "Number of Videos"}
)

# 📊 2. Line Chart - Total Comments Over Time
df_comments = video_stats.groupby(["PubYear", "Keyword"], as_index=False)["Comments"].sum()
df_comments["total_comments"] = df_comments["Comments"] / 1000
fig2 = px.line(df_comments, x="PubYear", y="total_comments", color="Keyword",
               title="Total Comments by Category Over Time (by 1k)")

# 📊 3. Line Chart - Average Title Length Over Time
df_title_len = video_stats.groupby(["PubYear", "Keyword"], as_index=False)["TitleLen"].mean()
fig3 = px.line(df_title_len, x="PubYear", y="TitleLen", color="Keyword",
               title="Avg Title Length by Category Over Time")

# 📊 4. Scatter Plot - Likes vs. Comments per 1k Views
fig4 = px.scatter(video_stats, x="LikesPer1k", y="CommentsPer1k", color="Keyword", size="Views",
                  title="Likes vs Comments per 1k Views", labels={"LikesPer1k": "Likes per 1k", "CommentsPer1k": "Comments per 1k"})

# 📊 5. Histogram - Distribution of Title Length
fig5 = px.histogram(video_stats, x="TitleLen", title="Distribution of Title Length", nbins=30)

# 🔹 Dash App Layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("YouTube Video Analytics Dashboard", style={"textAlign": "center"}),

    html.Div(children=[
        dcc.Graph(figure=fig1, style={"width": "20%", "display": "inline-block"}),
        dcc.Graph(figure=fig2, style={"width": "48%", "display": "inline-block"}),
    ]),

    html.Div(children=[
        dcc.Graph(figure=fig3, style={"width": "48%", "display": "inline-block"}),
        dcc.Graph(figure=fig4, style={"width": "48%", "display": "inline-block"}),
    ]),

    html.Div(children=[
        dcc.Graph(figure=fig5, style={"width": "98%", "display": "inline-block"}),
    ]),
])

# Run the Dash App
if __name__ == '__main__':
    app.run_server(debug=True)

