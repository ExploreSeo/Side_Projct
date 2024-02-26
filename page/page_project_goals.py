import streamlit as st

def app():
    # 1. 타이틀 수정
    st.title("주제 : 스팀게임 추천서비스 개발")

    st.text("\n" * 4)  # 엔터 4번을 통한 간격 조정
    st.text("\n" * 4)  # 엔터 4번을 통한 간격 조정


    image_path = 'page/image/intro_01.png'
    
    
    intro_tilte = """
    ## [프로젝트 개요]
    """
    st.markdown(intro_tilte)

    # 이미지를 왼쪽에 배치, 컬럼 비율을 조절 및 중앙 정렬
    col1, col2 = st.columns([3, 8])  # 이미지가 들어가는 컬럼은 3, 텍스트 부분이 들어가는 컬럼은 7

    with col1:
        st.text("\n" * 2)  # 엔터 4번을 통한 간격 조정
        #st.text("\n" * 4)  # 엔터 4번을 통한 간격 조정
        #st.text("\n" * 4)  # 엔터 4번을 통한 간격 

        st.image(image_path, use_column_width=True, width=300)  # 이미지의 너비를 300으로 조절 및 중앙 정렬

    # 2. 프로젝트 개요와 팀의 세부 목표 간격 조정
    intro_text = """
    
    **'Steam 게임 추천 서비스 개발'을 목표로 하여 다양한 게임 데이터를 기반으로 한 게임 추천 시스템을 구축하고자한다.** 
    
    현재 게임 시장은 여러 플랫폼에서 다양한 장르의 게임이 출시되고 있으며, 다양한 플랫폼에서 
    
    사용자 맞춤 추천해주는 기능도 많이 발달되어 있는 상황이다.
    
    그러나 이 추천 메커니즘과 정확도에 의문을 갖게 되었고, 실제 Steam 유저인 팀원들도 공감할 정도이였다.

    따라서 플레이어 각각의 취향과 선호를 기반으로 유사한 게임을을 추천해주는 서비스는 필요하다고 보았으며,
    
    이는 가치있는 시스템이 될 것이라 예상합니다.
    """

    # 오른쪽에 프로젝트 개요 표시
    col2.markdown(intro_text)

    # 3. 간격 조정
    st.text("\n" * 4)  # 엔터 4번을 통한 간격 조정

    # 4. 컬러풀한 스타일 적용
    st.subheader("[팀의 세부 목표]")
    st.text("\n" * 2)  # 엔터 2번을 통한 간격 조정

    team_goals = """
    - **다양한 특성 분석:** 게임의 다양한 특성에 대한 분석을 통해 어떤 장르, 태그, 또는 기타 특성이 사용자들에게 더 많은 인기를 얻고 있는지 파악하기

    - **맞춤형 추천:** 사용자의 선호도를 고려하여 각 사용자에게 적합한 게임을 추천하는 시스템을 구축하기

    - **프로젝트 결과 활용:** TF-IDF를 활용하여 게임 간 유사성을 측정하고, 이를 기반으로 추천 시스템을 개발하여 추천된 게임 목록을 시각적으로 제공하여 사용자가 쉽게 새로운 게임을 찾을 수 있도록 하기
    """

    st.markdown(team_goals)