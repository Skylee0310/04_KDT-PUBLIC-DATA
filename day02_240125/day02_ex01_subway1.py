'''
대중교통 데이터 읽어오기
'''

#모듈 불러오기
import csv

# subwayfee.csv 자료 불러와서 읽기.
f = open('subwayfee.csv')
data = csv.reader(f)

#헤더 정보 읽어오기.
header = next(data)
print(header)

# data에 있는 행을 한 줄씩 5줄까지 읽어오기

i = 1
for row in data :
    print(row) #한 줄씩 출력
    if i > 5 : #i가 5보다 크면 멈춤(=다섯줄 읽어옴.)
        break
    i += 1
    f.close() #파일 닫기.