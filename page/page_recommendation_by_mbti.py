# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:04:29 2024

@author: goldg
"""

import streamlit as st
from utils import utils_recommendation_by_mbti as ur_mbti

games_df = ur_mbti.games_df

def app():
    st.title("MBTI 유형별 게임 추천 시스템")

    # 사용자의 MBTI 유형 입력
    user_mbti_type = st.selectbox("MBTI 유형을 선택하세요:", list(ur_mbti.mbti_tag_mapping.keys()))

    # 사용자가 지정할 컬럼 입력
    #selected_columns = st.multiselect("원하는 컬럼을 선택하세요:", games_df.columns)

    # 추천할 게임 개수 입력
    max_games = st.number_input("추천할 게임의 최대 개수를 입력하세요:", min_value=1, max_value=20, value=10)

    # MBTI 유형에 해당하는 게임 추천
    recommended_games = ur_mbti.recommend_games_by_mbti(user_mbti_type, games_df, max_games=max_games)

    # 게임 추천 결과 출력
    st.write("게임 추천 결과:")
    st.dataframe(recommended_games[['AppID', 'Name', 'Price', 'Positive', 'Developers', 'Tags']])

if __name__ == "__main__":
    app()