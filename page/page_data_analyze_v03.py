import streamlit as st
#from utils import utils_visual_metacritic as uv_meta

def app():
    st.title('상관분석 및 시각화')

    #st.write("[진행 다이어그램]")    
    # 이미지 파일의 경로 설정
    image_path01 = 'page/image/ay_v03_01.png'
    image_path02 = 'page/image/ay_v03_02.png'
    image_path03 = 'page/image/ay_v03_03.png'
    image_path04 = 'page/image/ay_v03_04.png'
    image_path05 = 'page/image/ay_v03_05.png'

    # 이미지 표시
    st.image(image_path01, use_column_width=False)
    st.image(image_path02, use_column_width=False)
    st.image(image_path03, use_column_width=False)
    st.image(image_path04, use_column_width=False)
    st.image(image_path05, use_column_width=False)
    

    # 다이어그램에 관련된 내용을 추가하세요.
    