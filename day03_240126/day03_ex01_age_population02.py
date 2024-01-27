#산격 3동 인구 분포 그래프 그리기.

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('age.csv', encoding= 'utf-8-sig')
data = csv.reader(f)

result = [] #0세부터 100세 이상까지의 데이터를 담을 리스트
city = '' # 행정 기관 입력.
for row in data :
    if '산격3동' in row[0] :
        city = row[0]
        for data in row[3:]:
            if ',' in data :
                data = data.replace(',', '')
            result.append(int(data))
f.close()
print(result)


plt.title(f'{city} 인구 현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()