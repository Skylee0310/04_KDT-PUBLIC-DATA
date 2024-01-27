'''
1. 동 이름을 입력하면 해당 동의 인구 분포를 그리는 함수 구현.


s = 문자열 string
d = 정수형 decimal
f = 실수형 float
'''
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def print_population(population) :
    for i in range(len(population)) :
        print(f'{i:3d}세 : {population[i]:6d}명', end =' ')
        if (i+1) % 10 == 0 :
            print()
def draw_population(district_name, population_list) :
    plt.style.use('ggplot')
    plt.title('{} 인구현황'.format(district_name))
    plt.xlabel('나이')
    plt.ylabel('인구수')

    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))

    plt.plot(population_list)
    plt.show()

def get_population(city) :
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)

    population_list = []
    district_name =''
    for row in data:
        if city in row[0] :
            district_name = row[0]
            for data in row[3:]:
                if ',' in data :
                    data = data.replace(',','')
                population_list.append(int(data))
    f.close()

    print_population(population_list)
    draw_population(district_name, population_list)

city = "대구광역시"
get_population(city)