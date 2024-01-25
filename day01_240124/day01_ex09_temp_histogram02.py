import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('daegu-utf8.csv', encoding ='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08' :
            aug.append(float(row[-1]))

        if month == '01' :
            jan.append(float(row[-1]))

f.close()
plt.hist(aug, bins = 100, color = '#FCD3DC', label ='Aug')
plt.hist(jan, bins = 100, color = '#B2C2E8', label = 'Jan')
plt.title('1월과 8월의 대구 최고 기온 히스토그램')
plt.xlabel('Temperature')
plt.rc('axes', unicode_minus = False) #레이블에 '-' 부호가 깨지는 현상 방지.
plt.legend()
plt.show()