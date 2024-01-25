
# 최대 유임 승차 인원이 있는 역은?
import csv

f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)

next(data)

max_rate=0 #
max_row=[]
max_total_num=0

for row in data : # 한 줄씩 읽어옮
    for i in range(4,8): # i 는 4 ~ 7
        row[i] = int(row[i]) # 줄의 인덱스 [4] ~ [7] 자리의 값을 정수로 변환.
    total_count = row[4] + row[6] # 승차한 총 인원(= 유임 승차 인수 + 무임 승차 인수)
    if (row[6] != 0) and (total_count>100000) : # 무임 승차 인원이 0명이 아니고 승차한 총 인원이 10만명보다 많을 때,
        rate = row[4] / total_count # rate 유임 승차 비율 = 유임 승차 인수 / 총 승차 인수
        if rate> max_rate : # 유임 승차 비율 > max_rate 일때
            max_rate = rate # max_rate 값을 업데이트
            max_row = row # 행을 업데이트
            max_total_num = total_count # 총 승차 인수를 업데이트.
    #print(f'호선명 : {max_row[1]}, 역이름 : {max_row[3]}, 전체 인원 : {max_total_num:,}명,'
    #    f"유임승차 인원 : {max_row[4]:,}명, 유임승차 비율 : {round(max_rate*100, 2):,}%")

print(f'호선명 : {max_row[1]}, 역이름 : {max_row[3]}, 전체 인원 : {max_total_num:,}명,'
          f"유임승차 인원 : {max_row[4]:,}명, 유임승차 비율 : {round(max_rate*100, 2):,}%")

