import streamlit as st
import os


def app():
    st.title('프로젝트 다이어그램')

    #st.write("[진행 다이어그램]")    
    # 이미지 파일의 경로 설정
    image_path = 'page/image/diagram.png'

    # 이미지 표시
    st.image(image_path, caption='다이어그램 이미지', use_column_width=False)

    # 다이어그램에 관련된 내용을 추가하세요.
    