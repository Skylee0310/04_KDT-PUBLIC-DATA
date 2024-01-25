import csv

# encoding='utf-8-sig'로 '\ufeff' 제거
fin = open('daegu.csv', 'r', encoding='utf-8=sig')
data = csv.reader(fin, delimiter = ',')

# newline='': 한 라인씩 건너 뛰며 저장되는 현상 없앰
fout = open('daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig')
wr = csv.writer(fout)

for row in data :
    for i in range(len(row)) :
        row[i] = row[i].replace('\t', '')
    print(row)
    wr.writerow(row) # writerow(row): 한 행씩 파일로 저장

fin.close()
fout.close()
print('파일저장완료')

# 헤더 출력
f = open('daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f, delimiter=',') #delimiter 생략 가능.
header = next(data) #next = 첫 번째 데이터 행을 읽어오고 그 다음 행으로 이동.
print(header)
f.close()