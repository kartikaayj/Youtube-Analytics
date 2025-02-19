import streamlit as st
import pandas as pd
import plotly.express as px

# Sample Data (Replace with video_stats DataFrame)
video_stats = pd.DataFrame({
    "Keyword": ["Tech", "Food", "Travel", "Tech", "Food"],
    "LikesPer1k": [50, 30, 70, 90, 20],
    "CommentsPer1k": [5, 10, 7, 12, 3],
    "Views": [100000, 200000, 150000, 300000, 50000]
})

# Streamlit App
st.title("Video Stats Dashboard 📊")

# Scatter Plot
fig = px.scatter(
    video_stats, x="LikesPer1k", y="CommentsPer1k", 
    color="Keyword", size="Views", size_max=70, opacity=0.5,
    title="Likes VS Comments per 1k Views"
)
st.plotly_chart(fig)

# Run this dashboard with: `streamlit run dashboard.py`
