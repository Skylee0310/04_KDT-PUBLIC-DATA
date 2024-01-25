'''
2. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현.
- daegu-utf8.csv 또는 daegu-utf8-df.csv 파일 이용
-데이터 구조 : ['날짜', '지점', '평균기온, '최저기온', '최고기온']

1) 모듈 불러오기
 - 판다스
 - 그래프 ----> matplotlib.pyplot
 - 한글 패치 --> koreanize_matplotlib

2) 데이터 전처리
 2-0) 데이터 불러오기.

 2-1) 데이터 타입 확인 ---> 필요 시(특수기호 포함) 컬럼명 변경
  - 날짜 데이터 데이터 타입으로 형 변환

 2-2) 누락값
 - 누락값 개수 구하기
 - 누락값 포함된 행 삭제 -----> 데이터프레임.dropna(axis = 0)

 2-3) 데이터 저장.
 - 최종 데이터를 csv 파일로 저장.

3) 측정할 달을 입력받아서 해당 기간 동안 최고기온 평균값 및 최저기온 평균값 계산
 3-1) 측정할 연도/달 입력 받기
 3-2) 최고기온 평균값
 3-3) 최저기온 평균값 계산하기


4) 그래프 그리기 (함수)


1) 값 읽어오기
2) period에 분석기간 지정.(end - start year) # 측정할길이.
3) maxlist =[0]
3) minlist =[0]


'''
#
import pandas as pd
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 파일 불러와서 열 읽기.
weather_df = pd.read_csv('daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)

# 특수기호 삭제
weather_df.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']
#print(weather_df.columns)

# 날짜 데이터 타입 확인 후 datetime 타입으로 변경. (pd.to_datetime(바꿀 열 시리즈, format = 지정))
# print(weather_df['날짜'].dtype)
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
# print(weather_df['날짜'].dtype)
print('-'*80)

# 누락값 확인
# print(weather_df.shape)
# num_row = weather_df.shape[0]
# num_missing = num_row - weather_df.count()
# #print(num_row)
# print(weather_df.count())
# print(num_missing)
# print('-'*80)

# 누락값이 있는 행 삭제.
weather_df = weather_df.dropna(axis=0)
#print(weather_df.count())
#print(weather_df.shape[0])

# 파일 저장.
weather_df.to_csv('daegu_utf8_df.csv', index=False, mode = 'w', encoding='utf-8-sig')
print('-'*80)

# 시작연도와 마지막 연도 입력 받기
year1 = int(input('시작 연도를 입력하세요 : '))
year2 = int(input('마지막 연도를 입력하세요 : '))
month1 = int(input('기온 변화를 측정할 달을 입력하세요 : '))

maxlist = []
minlist=[]
for i in range(year1, year2+1) :
    year_df= weather_df[weather_df['날짜'].dt.year == i]
    month_df=year_df[year_df['날짜'].dt.month == month1]
    max_temp_mean = round(month_df['최고기온'].mean(), 1)
    min_temp_mean = round(month_df['최저기온'].mean(), 1)
    maxlist.append(max_temp_mean)
    minlist.append(min_temp_mean)

print(f'{year1}년부터 {year2}년까지 {month1}월의 기온 변화\n',
      f'{month1}월 최저기온 평균 :\n',
      f'{minlist}\n\n',
      f'{month1}월 최고기온 평균 :\n',
      f'{maxlist}')



def draw_graph(year1, year2):
    f = open('daegu_utf8_df.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    yearlist = list(range(year1, year2+1))
    plt.figure(figsize=(20, 4))
    plt.plot(yearlist, maxlist, color = 'hotpink', marker = 'o', label = '최고기온')
    plt.plot(yearlist, minlist, color = 'royalblue', marker = 'o', label = '최저기온')
    plt.rcParams['axes.unicode_minus'] = False
    plt.show()

draw_graph(year1, year2)
