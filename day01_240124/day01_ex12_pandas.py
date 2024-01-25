import pandas as pd
import matplotlib.pyplot as plt

# pandas에서 read_csv 함수 호출해서 읽어오기.
weather_df = pd.read_csv('daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)

# 데이터 타입 확인
print(weather_df['날짜'].dtype)

# 컬럼명 변경.
weather_df.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)

# 데이터타입으로 형 변환.
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format = '%Y-%m-%d') # 서식자 지정.
print(weather_df['날짜'].dtype)

# 누락값 개수 구하기.
print(weather_df.head(5)) # 위에서부터 1~5행 출력.
print(weather_df.shape) #튜플 형태로 출력. shape(row, col) ---- shape[0] : row의 개수.
num_rows = weather_df.shape[0] # 전체 값의 개수
num_missing = num_rows - weather_df.count() #count() 정상값의 개수.
print(num_missing) # 누락값 개수 출력.

weather_df = weather_df.dropna(axis = 0)
print(weather_df.count())
print(weather_df.head(5))

# 누락값을 제거한 최종 데이터를 csv 파일로 저장.
weather_df.to_csv('daefu-utf8-df.csv', index=False, mode = 'w', encoding='utf-8-sig')

# 특정 연도와 달의 최고, 최저 기온 평균값 계산.
# - 해당 연도와 달의 DataFrame 가져오기
# - datetime 객체 접근 (dt.year, dt.month, dt.day)
year_df = weather_df[weather_df['날짜'].dt.year == 2023] #필터링.
month_df = year_df[year_df['날짜'].dt.month == 8]
print(month_df.head())
print()
# 특정 연도와 달의 최저 기온 및 최고 기온의 평균 계산
max_temp_mean = round(month_df['최고기온'].mean(), 1) #소숫점 첫번째 자리.
min_temp_mean = round(month_df['최저기온'].mean(), 1)

print(f'2023년 8월 최저기온 평균 : {min_temp_mean}, 최고기온 평균 : {max_temp_mean}')

def draw_two_plots(title, x_data, max_temp_list1, label_y1, max_temp_list2, label_y2):

    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 4))
    plt.plot(x_data, max_temp_list1, marker='s', markersize = 6, color = '#6FB9D9')
