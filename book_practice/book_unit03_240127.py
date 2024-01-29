'''
unit 03 서울이 가장 더웠던 날은 언제였을까?

방법1 pandas
1) csv파일을 읽어오기
2) 최고기온 컬럼만 추출한 다음.
3) 열에서 최댓값 찾기.

방법2 import csv
1) 파일 읽어오기.

+ 숫자로 이루어진 값인지 검사.

2) 최댓값 임의로 설정해놓고 for 문으로 row[4] > 최댓값일 때 최댓값 = row[4]로 업뎃...!
3) 최댓값 출력

'''

import pandas as pd
import csv

# 방법 2
f = open('seoul_file.csv', encoding = 'cp949')
data = csv.reader(f)
next(data)

# 최댓값 지정.
max_tem = -999
max_date = ''
for row in data :
    if row[4] != '' :
        row[4] = float(row[4])
        if row[4] > max_tem :
            max_tem = row[4]
            max_date = row[0]
        if row[4] == '' :
            max_tem = -999 # 전혀 가능하지 않은 온도 입력.

print(f'서울의 가장 더운 날은{max_date} 기온은 {max_tem}입니다.')


