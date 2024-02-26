# page_intro.py

import streamlit as st
import os

def app():
    
    # 페이지 배경색 설정
    # 페이지 배경색 설정
    #st.set_page_config(page_title="Your Page Title", page_icon="🚀", layout="wide", initial_sidebar_state="expanded", bg_color="#f6f6f6")
    
    # 1. 작은 타이틀
    st.subheader("Side Project")

    # 2. 메인 타이틀
    st.header("[취향에 맞는 Steam 게임 추천서비스]")

    # 3. 이미지 불러오기
    image_path = 'page/image/main_01.png'
    st.image(image_path, use_column_width=False)

    # 추가적인 내용이 있다면 여기에 작성하세요.
    #st.write("여기에 Intro 페이지에 관한 추가적인 내용을 작성하세요.")