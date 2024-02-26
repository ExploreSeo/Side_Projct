# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:54:58 2024

@author: goldg
"""
# 메타크리틱 점수 와 가격, 긍정 비율 및 총 리뷰 수 시각화

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib import font_manager, rc

basic_path = os.path.dirname(__file__)
basic_file_path = os.path.join(basic_path, 'data')

# 한글 폰트 설정
font_path = basic_file_path + '\\NanumGothic.ttf'  # 폰트 파일의 경로
fontprop = font_manager.FontProperties(fname=font_path)
rc('font', family=fontprop.get_name())

# 게임 파일 경로
file_paths = os.path.join(basic_file_path, 'final_dataset.csv')
df = pd.read_csv(file_paths)

def data_EDA(df):
    df = df[df['Metacritic score'] != 0]
    df['Total_Reviews'] = df['Positive'] + df['Negative']
    df['Log_Total_Reviews'] = np.log1p(df['Total_Reviews'])
    df['Positive_ratio'] = df['Positive'] / (df['Positive'] + df['Negative'])
    
    return df

# Metacritic score vs. Positive ratio 시각화
def plot_metacritic_vs_positive(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Metacritic score', y='Positive_ratio', alpha=0.5, ax=ax)
    ax.set_title('Metacritic score vs. Positive ratio')
    ax.set_xlabel('Metacritic score')
    ax.set_ylabel('Positive ratio')
    ax.grid(True)
    
    return fig

# Metacritic score vs. Price 시각화
def plot_metacritic_vs_price(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Metacritic score', y='Price', alpha=0.5, ax=ax)
    ax.set_title('Metacritic score vs. Price')
    ax.set_xlabel('Metacritic score')
    ax.set_ylabel('Price')
    ax.grid(True)
    
    return fig

# Total reviews vs Metacritic score 시각화
def plot_totalreviews_vs_metacritic(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Log_Total_Reviews', y='Metacritic score', alpha=0.5, ax=ax)
    ax.set_title('Total reviews count vs Metacritic score')
    ax.set_xlabel('Total reviews count')
    ax.set_ylabel('Metacritic score')
    ax.grid(True)
    
    return fig
