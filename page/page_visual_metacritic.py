# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:32:23 2024

@author: goldg
"""

import streamlit as st
from utils import utils_visual_metacritic as uv_meta

data = uv_meta.read_data(uv_meta.file_paths)
top_games_data = uv_meta.select_top_games(data)
plot01 = uv_meta.visualize_top_games(top_games_data)

positive_rate_fig, negative_rate_fig = uv_meta.visualize_review_rates(data)

avg_score_and_info = uv_meta.analyze_developers(data)


def app():
    st.subheader('Top Games Visualization')
    st.pyplot(plot01)
    st.plotly_chart(positive_rate_fig)
    st.plotly_chart(negative_rate_fig)
    st.write(avg_score_and_info)