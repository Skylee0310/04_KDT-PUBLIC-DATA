
import pandas as pd
import koreanize_matplotlib

# 행정구역별 인구수 데이터 준비 - 행정구역 이름 데이터 불러오기.
population = pd.read_excel('행정구역시군구별성별인구수.xlsx', sheet_name='데이터', header=[0])
print(population.head())

# 행정구역별 인구수 데이터 - 컬럼 이름 변경
population = population.rename(columns={'행정구역(시도)별1': '시도', '행정구역(시군구)별2':'군구'})
print(population.head())

row_count = population.shape[0]
for index in range(0, row_count) :
    population['군구'][index] = population['군구'][index].strip()

population['시도군구'] = population.apply(lambda r : r['시도']+' ' +r['군구'], axis = 1)
print(population.head())
print('-'*80)

population = population[population.군구!='소계'] #군구 컬럼에서 값이 '소계'가 아닌 것만 필터링 해서 추출 후 저장.
#population = population[population['군구'] !='소계']
print(population.head())

population = population.set_index('시도군구') #'시도군구' 컬럼을 병합에 사용할 인덱스로 설정.
print(population.head())

addr_population_merge= pd.merge(addr_group, population, how = 'inner', left_one = None, right_on = None, left_index = True, right_index = True)