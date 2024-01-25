'''

'''
import csv
import matplotlib.pyplot as plt

# 파일 열고 읽어오기
f = open('daegu-utf8.csv', encoding ='utf-8-sig') # utf-8-sig 생략가능.
data = csv.reader(f)


header = next(data) # 첫 줄 읽고 다음 행으로 넘어가서 바로 데이터에 접근
result = [] #빈 리스트에 접근

for row in data : # 행을 한 줄씩 읽어오기.
    if row[4] != '' : # 값이 있을 때
        result.append(float(row[4])) # 그 값을 result 리스트에 넣기.

print(len(result)) # 값의 개수 프린트.
f.close() # 값 닫기.
plt.figure(figsize=(10, 2)) # 그래프 크기 조절(가로 10인치 세로 2인치)
plt.plot(result, 'r') # result 리스트에 저장된 값을 빨간색 그래프로 출력.
plt.show()


# import random
# import matplotlib.pyplot as plt
#
# dice = []
# for i in range(10):
#     dice.append(random.randint(1, 6))
# print(dice)
#
# plt.hist(dice, bins = 6)
# plt.xticks([1, 2, 3, 4, 5, 6]) # x축 간격 값.
# plt.show()