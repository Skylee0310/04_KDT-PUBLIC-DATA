# 승ㆍ하차 인원이 가장 많은 역은?
import csv
max = [0]*4 #[0, 0, 0, 0] #[0] 최대 유임승차 [1] 최대 유임하차 [2] 최대 무임승차 [3] 최대 무임하차
max_station = [''] * 4 #['', '', '', '']
label = ['유임승차', '유임하차', '무임승차', '무임하차']
#[0]사용월,[1]호선명,[2]역ID,[3]지하철역,[4]유임승차,[5]유임하차,[6]무임승차,[7]무임하차

#with 구문 : 자동으로 파일을 close() 시킴
with open('subwayfee.csv', encoding='utf-8-sig') as f :
    data = csv.reader(f)
    next(data)

    for row in data : #한 줄씩 출력.
        for i in range(4,8) :
            row[i] = int(row[i]) # 4번부터 8번 컬럼.
            if row[i]>max[i-4] : # row[4:8]을 max[0:4]의 요소와 각각 비교해서
                max[i-4] = row[i] # 값을 업데이트
                max_station[i-4] = row[3] +' '+row[1] # 역 이름 + (공백) + 호선 + (공백)

for i in range(4):
    print(f'{label[i]} : {max_station[i]} {max[i]:,}명')