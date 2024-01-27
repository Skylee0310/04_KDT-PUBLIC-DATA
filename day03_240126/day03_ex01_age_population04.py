'''
투표 가능
'''
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_piechart(city_name, city_population, voting_population) :
    non_voting_population = city_population-voting_population
    population = [non_voting_population, voting_population]

    color = ['tomato', 'royalblue']
    plt.pie(population, labels = ['18세 미만', '투표가능 인구'],
            autopct='%.1f%%', colors = color, startangle=90)

    plt.legend(loc=1)
    plt.title(city_name+' 투표가능 인구 비율')
    plt.show()

def get_voting_population(city):
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)

    voting_number_list = []
    city_name = ''
    city_population = 0
    voting_population =0
    for row in data :
        if city in row[0] :
            city_population = row[1]
            if ',' in city_population :
                city_population = city_population.replace(',', '')
            city_population = int(city_population)
            city_name = row[0]
            for data in row[21:] :
                if ',' in data :
                    data = data.replace(',', '')
                voting_num = int(data)
                voting_number_list.append(voting_num)

                voting_population +=voting_num
            break
    f.close()
    print(f'{city_name} 전체 인구수 : {city_population:,}명,'
          f'투표 가능 인구수 : {voting_population:,}명')
    draw_piechart(city_name, city_population, voting_population)

city = input('투표 가능 인구수를 확인할 도시 이름을 입력하시오. : ')
get_voting_population(city)