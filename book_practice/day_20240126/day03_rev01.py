# 대구 수성구 파동 연령별 인구 분포 그래프 그리기.
'''
<데이터 처리>
1) 모듈 불러오기
2) 파일 읽어오기
+ 각 연령별 데이터를 저장할 리스트 생성
+ 해당 행정 기관 정보를 저장할 변수 생성.
3) 한 줄씩 읽어오기.
4) if '찾는 도시'가 row[0](행정기관)에 있다면 data는 row[3]부터 끝까지.
5) if data에 쉼표가 있으면 쉼표를 ''로 replace하고 정수처리한다.
6) 정수로 변환한 값을 리스트에 담는다.
7) 파일 닫기.
8) 프린트.

<그래프 그리기>
1)
2)
'''


import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('age.csv', encoding="utf-8-sig") #encoding 빠트리지 않기.
data = csv.reader(f)

result = []
#search_city = input("연령별 정보를 알고 싶은 동을 입력하세요 : ")
search_city = '수성구 파동'
city = ''

for row in data :
    if search_city in row[0] :
        city = row[0]
        for i in row[3:] :
            #print(i, end=' ')
            if ',' in i :
                i.replace(',', '')
            i = int(i)
            result.append(i)
f.close()
print(result)

# 그래프 그리기
plt.title(f'{city}의 연령별 인구 분포')
plt.plot(result)
plt.xlabel('나이')
plt.ylabel('인구 수')
plt.show()