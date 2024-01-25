import pandas as pd

df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0, 1]) #멀티인덱스
print(df.head())
print(df.columns)
print('-'*80)

print(df[('지하철역', 'Unnamed: 3_level_1')])
print('-'*80)
commute_time_df = df.iloc[:, [1, 3, 10, 12, 14]]
print(commute_time_df.head())
print(commute_time_df.dtypes)

# 천 단위 콤마 제거.
commute_time_df[('07:00:00~07:59:59', '승차')] = commute_time_df[('07:00:00~07:59:59', '승차')].apply(lambda x : x.replace(',', ''))
commute_time_df[('08:00:00~08:59:59', '승차')] = commute_time_df[('08:00:00~08:59:59', '승차')].apply(lambda x : x.replace(',', ''))
commute_time_df[('09:00:00~09:59:59', '승차')] = commute_time_df[('09:00:00~09:59:59', '승차')].apply(lambda x : x.replace(',', ''))
print(commute_time_df)
print('-'*80)

commute_time_df = commute_time_df.astype({('07:00:00~07:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59', '승차'):'int64'})
print(commute_time_df.dtypes)
print('-'*80)

row_sum_df = commute_time_df.sum(axis=1, numeric_only=True) # 행의 합, 숫자만.
passenger_number_list = row_sum_df.to_list() # row_sum_df를 리스트로 형 변환.
print(row_sum_df)

max_number = row_sum_df.max(axis=0) #해당 열에서 최댓값 찾기.
print(max_number)

max_index = row_sum_df.idxmax()
max_line, max_station = df.iloc[max_index, [1, 3]]
print('출근 시간대 최대 승차 인원역 : {0} {1} {2:,}명'.format(max_line, max_station, max_number))

# 그래프 그리기

import matplotlib.pyplot as plt

passenger_number_list.sort(reverse = True)
plt.figure(dpi=100)
plt.bar(range(len(passenger_number_list)), passenger_number_list, color="#98A658")
plt.show()

