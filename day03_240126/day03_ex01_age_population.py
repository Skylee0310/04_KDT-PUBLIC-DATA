'''
(대구 산격동) 인구 현황.
1. 모듈 불러오기.
2. 파일 불러오기.
3. 헤더 읽기
4. 산격 3동이 포함된 자료만 출력 (for문)
5. 파일 닫기.
'''
import csv
f = open('age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
print(f'header :\n{header}')

for row in data : # 데이터 읽어오기.
    if '산격3동' in row[0] : #row[0] = 행정기관
        print(row)

f.close()
print('-'*80)

# 인구 수 출력.
import csv

f = open('age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)

result=[]
for row in data : # 데이터 읽어오기.
    if '산격3동' in row[0] : # 산격 3동 자료만 출력
        for data in row[3:] : # 0~100세 이상까지 자료를 리스트에 추가.
            result.append(data)
print(f'산격 3동 연령별(0세~ 100세 이상) 자료 : {result}')
f.close()