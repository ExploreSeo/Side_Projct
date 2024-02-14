'''
import streamlit as st
from utils import utils_07 as ut7
import streamlit as st
import pandas as pd
import math
import requests

#games_df = ut7.games_df


# Streamlit 페이지 설정
st.set_page_config(page_title="Tag 기반 게임 추천 시스템", layout="wide")


def app():
        
    # CSV 파일 로드
    #@st.cache
    def load_data():
        #file_path = 'C:/Users/bawu9/Documents/games.csv' #실제 파일 경로에 맞게 조정해야 합니다.
        #data = pd.read_csv(file_path)
        data = ut7.games_df
        data['Tags'] = data['Tags'].apply(lambda x: x.split(',')[0] if isinstance(x, str) else x).head(20)
        return data[['Name','AppID', 'Genres', 'Developers', 'Publishers','Tags']].head(10)
    
    # 데이터 로드
    sample_games = load_data().to_dict('records')
    
    # 앱의 나머지 부분
    st.subheader("Tag를 활용한 차별화된 게임 추천 시스템")
    
    # 태그 선택 섹션
    st.subheader("선호하는 태그를 클릭해주세요")
    
    # 태그 리스트를 30개로 확장합니다.
    tags = ['액션', '어드벤처', '퍼즐', 'RPG', '시뮬레이션', '인디',
            '캐주얼', '멀티플레이어', '전략', '스포츠', '슈팅', '레이싱',
            '공포', 'MMO', 'MOBA', '카드 게임', '보드 게임', '아케이드',
            '음악', '플랫포머', '퀴즈', '로그라이크', '샌드박스', 'VR 게임',
            '생존', '소울라이크', '파이팅', '턴제 전략', '턴제 RPG', '시뮬레이션 RPG']
    
    # 사용자가 현재 보고 있는 화면의 너비에 따라 열의 개수를 조정합니다.
    # Streamlit은 현재 클라이언트 화면 크기를 직접 알아내는 기능을 지원하지 않으므로,
    # 사용자에게 입력 받거나, 적절한 디폴트 값을 사용해야 합니다.
    # 여기서는 예시로 5를 사용합니다. 실제로는 사용자의 화면 크기에 맞게 조정해야 합니다.
    columns_per_row = 5
    
    # 총 태그 수에 맞춰 행의 개수를 계산합니다.
    rows = math.ceil(len(tags) / columns_per_row)
    
    # 선택된 태그들을 저장할 리스트입니다.
    selected_tags = []
    
    # 그리드 형태로 체크박스를 배치합니다.
    for row in range(rows):
        cols = st.columns(columns_per_row)  # 동적으로 컬럼을 생성합니다.
        for col in range(columns_per_row):
            tag_index = row * columns_per_row + col
            if tag_index < len(tags):  # 태그 리스트의 범위를 벗어나지 않도록 합니다.
                with cols[col]:
                    # 체크박스를 생성하고 선택된 경우 selected_tags에 추가합니다.
                    if st.checkbox(tags[tag_index], key=tags[tag_index]):
                        selected_tags.append(tags[tag_index])
    
    # 선택된 태그를 출력합니다.
    st.write("선택된 태그:", selected_tags)
    
    
    
    # Steam API 키
    steam_api_key = "9AB34E09020B2C9AD9CC6A31408AFC65"
    
    # Steam API 키
    #steam_api_key = "YOUR_STEAM_API_KEY"
    
    def get_steam_game_image(app_id):
        base_url = "https://store.steampowered.com/api/appdetails"
        params = {
            "appids": app_id,
            "cc": "kr",  # 국가 코드 (예: 한국은 "kr")
        }
    
        response = requests.get(base_url, params=params)
        data = response.json()
    
        # 게임 이미지 URL 가져오기
        try:
            image_url = data[str(app_id)]["data"]["header_image"]
            return image_url
        except KeyError:
            return None
    
    # 확인 버튼
    if st.button("확인"):
        st.success("선택한 태그에 기반한 게임을 추천합니다!")
        # 추천된 게임 표시
        st.subheader("추천된 게임")
        for game in sample_games:
            st.text('---' * 15)
            # 스팀 사이트 접근 URL 생성
            steam_url = f"https://store.steampowered.com/app/{game['AppID']}"
            # 이미지 가져오기
            image_url = get_steam_game_image(game['AppID'])
            # 이미지 출력
            if image_url:
                st.image(image_url, caption=f"{game['Name']} 이미지", use_column_width=True)
            else:
                st.warning(f"{game['Name']}의 이미지를 가져올 수 없습니다.")
            # 게임 정보 출력
            st.text(f"게임 이름: {game['Name']}")
            st.text(f"게임 ID: {game['AppID']}")
            st.text(f"장르: {game['Genres']}")
            st.text(f"개발사: {game['Developers']}")
            st.text(f"출판사: {game['Publishers']}")
            st.text(f"태그: {game['Tags']}")
'''
import pandas as pd
import os
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

basic_path = os.path.dirname(__file__)
basic_file_path = os.path.join(basic_path, 'data')

# 게임 파일 경로
file_path = os.path.join(basic_file_path, 'final_dataset.csv')
games_df = pd.read_csv(file_path)

# 환경 변수에서 스팀 API 키 가져오기
STEAM_API_KEY = os.environ.get('9AB34E09020B2C9AD9CC6A31408AFC65')

def get_steam_game_image(app_id):
    base_url = "https://store.steampowered.com/api/appdetails"
    params = {
        "appids": app_id,
        "cc": "kr",  # 국가 코드 (예: 한국은 "kr")
        "key": STEAM_API_KEY  # 스팀 API 키 추가
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # 게임 이미지 URL 가져오기
    try:
        image_url = data[str(app_id)]["data"]["header_image"]
        return image_url
    except KeyError:
        return None
    
def calculate_tag_frequencies():
    all_tags = []
    for tags_list in games_df['Tags'].apply(lambda x: x.split(',')):
        all_tags.extend(tags_list)
    
    # 태그 빈도 계산
    tag_counts = {}
    for tag in all_tags:
        if tag in tag_counts:
            tag_counts[tag] += 1
        else:
            tag_counts[tag] = 1
    
    # 태그 빈도를 내림차순으로 정렬하여 반환
    sorted_tag_counts = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_tag_counts

# TF-IDF 벡터화
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(games_df['Tags'])

def recommend_games(selected_tags, num_recommendations=50, page_number=1):
    # 선택된 태그들을 공백으로 연결하여 새로운 문서를 만듭니다.
    selected_tags_text = ' '.join(selected_tags)
    # 선택된 태그들에 대한 TF-IDF 벡터를 구합니다.
    selected_tags_tfidf = tfidf_vectorizer.transform([selected_tags_text])
    # 선택된 태그들과 유사한 게임을 찾습니다.
    similarities = cosine_similarity(selected_tags_tfidf, tfidf_matrix)
    # 유사도를 기준으로 상위 n개의 게임을 추천합니다.
    start_index = (page_number - 1) * num_recommendations
    end_index = start_index + num_recommendations
    similar_indices = similarities.argsort()[0][start_index:end_index][::-1]
    recommended_games = games_df.iloc[similar_indices]
    return recommended_games
