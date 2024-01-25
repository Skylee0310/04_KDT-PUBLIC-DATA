'''
과거 10년 동안의 대구 날씨 데이터에서 1년 중 일교차가 가장 큰 달은 각각 몇 월인지 그래프로 표시
기간 : 최근 10년 (2014년 ~ 2023년)
- 각 달의 일교차(최고기온 - 최저기온)를 비교하여 각 년도별 일교차가 가장 큰 달을 막대그래프로 표시
- pandas 또는 python 코딩

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

3) 특정 연도와 일교차 계산
 3-1)
 - 기간 내의 연도 별 달의 최고기온, 최저 기온 구한 다음 일교차(최고기온 - 최저기온) 구하기.
 - 가장 일교차가 큰 달을 막대그래프로 표시.

4) 그래프 그리기 (함수)



<방법1> 새 데이터프레임(일교차)을 하나 만들어서 계산.
어려우면->
1) 하나의 연도에 대해서 먼저 계산해보기.
2) 나머지는 반복문 돌리기.
+ concat
뽑아낸 것을 리스트 형태로 변환해서..

'''
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 읽어와서 컬럼명 확인.
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
print('-'*80)
# 파일 저장.
weather_df.to_csv('daegu_utf8_df.csv', index=False, mode = 'w', encoding='utf-8-sig')

# 해당 연도와 달의 DataFrame 가져오기

year1 = 2014
year2 = 2023
weather_df['일교차'] = weather_df['최고기온']-weather_df['최저기온'] #일교차 계산하는 열.

# 2014년에서 2023년까지의 행 데이터 출력.

#1) 일교차 평균 = []

#2) m = 0

#3)

tem_ran_max =[]

for y in range(year1, year2+1) :
    high_max = -999
    month_max = 0
    year_df = weather_df[weather_df['날짜'].dt.year ==y]

    for m in range(1, 13) :
        date_df = year_df[year_df['날짜'].dt.month == m]
        tem_ran = date_df['일교차'].mean()
        if tem_ran>high_max :
            high_max = tem_ran
            month_max = m
    tem_ran_max.append([y, month_max, round(high_max, 1)])
print(tem_ran_max)

plt.bar([i[0] for i in tem_ran_max], [i[2] for i in tem_ran_max], color ='skyblue')
plt.xticks([i[0] for i in tem_ran_max], [f'{i[0]}.{i[1]}' for i in tem_ran_max])
plt.xlabel('Year/Month')
plt.ylabel('일교차')
plt.title('지난 10년간 대구의 일교차가 가장 큰 달')
plt.show()




