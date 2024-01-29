'''
1. 인구를 입력하면 해당 동의 인구 분포를 그리는 함수 구현.(print_population(population_list))
    1) population 리스트의 길이 만큼 반복.
    2) 인덱스 0부터 시작 (프린트 {나이}세 : {리스트[i]}명,
    3) 10살 마다 한줄 띄움.

2. 인구분포 그래프 그리기 함수 (draw_population(district_name,population_list))
    1) 격자 넣기
    2) 제목 넣기
    3) xlabel
    4) ylabel
    5) 막대그래프. x = 0부터 100살 이상, y = 인구 리스트,
    6) x 간격.
    7) 그래프 만들긴
    8) 그래프 출력.


3.  도시 넣기
    1) 파일 열기
    2) 연령별 인수 요소를 담을 리스트 만들기
    3) 파일을 읽어오면서 city가 row[0]에 포함되어 있으면 district_name
    4) 행의 연령별 데이터 읽어와서 ','을 ''로 변환.
    5) 정수로 변환된 데이터를 population_list.append(int(data))
    6) break
    7) 파일 닫기
    8) 함수1(인구분포그리기.), 함수2(그래프)

4. 도시 입력받기
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def print_population(population) :
    # population = 연령별 인구 요소를 입력한 리스트.
    for i in range(len(population)) :
        print(f'{i:3d}세 : {population[i]:6d}명', end=' ')
        if (i+1)%10 == 0 :
            print()
def draw_population(district_name, population) :
    plt.style.use('ggplot') #격자
    plt.title(f'{district_name} 인구현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.bar(range(101), population)
    plt.xticks(range(0, 101, 10))
    plt.plot(population)
    plt.show()
def get_population(city) :
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)

    population = []
    district_name = ''
    for row in data :
        if city in row[0] :
            district_name =row[0]
            for age in row[3:] :
                if ',' in age :
                    age = age.replace(',', '')
                population.append(int(age))
            break
    f.close()
    print_population(population)
    draw_population(district_name, population)
city = input('지역 이름 입력 : ')
get_population(city)
