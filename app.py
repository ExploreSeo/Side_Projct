import streamlit as st
from page import intro
from page import page_project_goals  # 변경된 순서에 따라 임포트 추가
from page import page_diagram
from page import page_data_analyze_v01 as pv1
from page import page_data_analyze_v02 as pv2
from page import page_data_analyze_v03 as pv3
from page import page_recommendation_by_tags_top30 as pr4
from page import page_recommendation_by_tags_select as pr5

# wide mode 비활성화
# st.set_page_config(wide_mode=False)


item_list = ['item0', 'item3', 'item1', 'item2', 'item4']

item_labels = {'item0': '메인', 'item3': '프로젝트 목표', 'item1': '다이어그램', 'item2': '분석 및 시각화', 'item4': '추천시스템'}

FIL = lambda x: item_labels[x]
item = st.sidebar.selectbox('Select a page', item_list, format_func=FIL)

if item == 'item0':
    intro.app()
elif item == 'item3':
    page_project_goals.app()
elif item == 'item1':
    page_diagram.app()
elif item == 'item2':
    side_select = st.sidebar.selectbox('분석내용을 선택하세요.', ['스팀게임데이터 분석 및 시각화', '상관분석', '태그 및 장르분석'])
    if side_select == '스팀게임데이터 분석 및 시각화':
        pv1.app()
    elif side_select == '상관분석':
        pv2.app()
    elif side_select == '태그 및 장르분석':
        pv3.app()
elif item == 'item4':
    sub_item = st.sidebar.selectbox('추천 서비스 구현화', ['상위 태그 30개 이용한 추천', '대표 태그 이용한 추천'])
    if sub_item == '상위 태그 30개 이용한 추천':
        pr4.app()
    elif sub_item == '대표 태그 이용한 추천':
        pr5.app()