import csv

f = open('seoul_file.csv', encoding='cp949')
data = csv.reader(f, delimiter=',') #delimiter 생략 가능.
header = next(data)
print(header)
n = 1
for row in data :
    print(row)
    n+=1
    if n > 5 :
        break

f.close()

# 각 행의 데이터는 대괄호로 둘러싸인 리스트의 형태로 출력됨.
