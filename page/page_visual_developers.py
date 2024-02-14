# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:13:38 2024

@author: goldg
"""

import streamlit as st
from utils import utils_visual_developers as uv_developer

df = uv_developer.df
dev_avg_playtime, dev_med_playtime, pub_avg_playtime, pub_med_playtime = uv_developer.calculate_playtime(df)
plot01 = uv_developer.plot_playtime(dev_avg_playtime, dev_med_playtime, pub_avg_playtime, pub_med_playtime)
top_devs = uv_developer.top_developers_by_playtime(df)



def app():
    st.pyplot(plot01)
    # 플레이 타임별 상위 개발사
    st.subheader("Top Developers by Playtime")
    st.write(top_devs)
    