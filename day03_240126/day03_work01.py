


import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('gender.csv', encoding='utf-8-sig')
data = csv.reader(f)
population = []
citylist = ['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
        '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구',
        '대구광역시 달서구', '대구광역시 달성군']
i = 1
for city in citylist :
    male = 0
    female = 0
    for row in data :
        if city in row[0] :
            male = int(row[104].replace(',', ''))
            female = int(row[207].replace(',', ''))
            break
    population = [male, female]
    color = ['cornflowerblue', 'tomato']
    plt.subplot(3, 3, i)
    plt.pie(population, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
    plt.title(city)
    i +=1
plt.suptitle('대구광역시 구별 남녀 인구 비율', size='x-large')
plt.show()

