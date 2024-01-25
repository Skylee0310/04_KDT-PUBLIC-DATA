'''
전체 탑승 인원 대비 유임 승차 비율이 가장 높은 역은?
'''
import csv
# f = open('subwayfee.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# header = next(data)
# max_rate = 0 # max rate
# rate = 0

#pdf 2- 6페이지.
# for row in data : #row는 데이터 안의 행.
#     for i in range(4, 8) : #4부터 7까지 4번 반복할 것.
#         row[i] = int(row[i]) # 4, 5, 6, 7 컬럼값을 정수로 변환
#     rate = row[4] / row[6] # [6]컬럼(=무임승차) 값이 0인 행 확인 용도.
#     if rate > max_rate :
#         max_rate = rate
# print(max_rate)
# f.close()

# ▲ 위 for문은 에러 나야 정상임(ZeroDivisionError = 0으로 나눠서 생기는 Error 발생)



'''
무임승차 인원이 0인 역 찾기 #1
'''
# for row in data :
#     for i in range(4, 8) :
#         row[i] = int(row[i])
#     rate = row[4] / (row[4]+row[6]) # rate = 유임승차 인원/(유임승차 + 무임승차 인원)
#     if row[6] == 0 : # 무임승차 인원(row[6])이 없는 역 출력
#         print(row) # 디버깅 용도의 프린트문.(계산하는데 필요는 없지만 확인 용도.)

# f.close()

'''
최대 무임 승차 비율 확인
'''
f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0 # max rate (최댓값을 누적할 변수 설정)

for row in data :
    for i in range(4, 8) :
        row[i] = int(row[i]) # 줄(가로)의 인덱스 [4] ~ [7] 위치에 있는 값을 정수로 변환.
    if row[6] != 0 : # 해당 줄(가로)의 인덱스[6](무임승차 인원)가 0이 아닐 때,
        #무임승차(%) = (무임 승차 수 * 100) / (유임 승차 수 + 무임 승차 수 )
        rate = (row[6] * 100) / (row[4]+row[6])
        if rate > max_rate : # <무임승차 비율 rate>이 max_rate보다 클 때.
            max_rate = rate # rate를 max_rate에 넣어서 값을 업데이트.
            print(row, round(max_rate, 2), '%') #해당 행을 출력하고 max_rate 값을 소수점 두번째 자리까지 표기.
f.close()

