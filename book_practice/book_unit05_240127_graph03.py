'''
unit 05 - 내 생일의 기온 변화를 그래프로 그리기.

함수
내 생일을 입력하면(형식 12-11) 평균 기온, 최저 기온, 최고 기온 변화. 그래프를 출력.


'''

import csv

f = open('seoul_file.csv')
data = csv.reader(f)
next(data)
birthday = '12-11'
avglist = []
min_list = []
max_list = []

for row in data :
    if birthday in row[0] :
        if row[2] != '' :
            row[2] = float(row[2])
            avglist.append(row[2])

        if row[3] != '' :
            row[3] = float(row[3])
            min_list.append(row[3])

        if row[4] != '' :
            row[4] = float(row[4])
            max_list.append(row[4])

print('')