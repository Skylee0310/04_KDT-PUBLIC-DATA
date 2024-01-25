# 실습 : 유임 승차 비율이 50% 이하인 역
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
print(header)


min_rate = 100 #최저 유임승차비율
min_row = [] # 최저 유임 승차한 행
min_total_count= 0 # 최저 유임 승차한 인수

for row in data :
    for i in [4,6] : #인덱스 중에서 4, 6만 추출.
        row[i] = int(row[i])
    total_count = row[4] + row[6] # 총 승차 인수

    # 무임승차 인원이 없고 총 승차인원이 1만명 이상.

    if (row[6] != 0) and (total_count >= 10000) : # 행의 인덱스[6] 값이 0이 아니고 총 승차인수가 만명 이상일때
        rate = row[4] / total_count # 유임 승차 인수 / 총 승차 인수
        if rate <= 0.5: # 유임 승차 인수가 50%이하일 때
            print(row, round(rate, 2)) #행 출력, 비율을 소수점 두번째 자리까지 표기.
            if rate < min_rate : # rate가 min_rate 보다 작을 때
                min_rate = rate # min_rate 값을 업데이트
                min_row = row # 행 업뎃
                min_total_count = total_count # 총인원수 업뎃
f.close()

print()
print(f'유입 승차 비율이 가장 낮은 역 : {min_row[3]}')
print(f'전체 인원 : {min_total_count:,}명,'
      f'유임승차인원 : {min_row[4]:,}명'
      f'유임승차비율 : {round(min_rate*100, 1)}%')

if platform.system() == 'Windows' :
    plt.rc('font', family = "Malgun Gothic")
else :
    plt.rc('font', family = 'AppleGothic')

# 그래프 그리기.
plt.title(min_row[3]+"역 유, 무임 승차 비율")
label = ['유임승차', '무임승차']
values = [min_row[4], min_row[6]]
plt.pie(values, labels = label, autopct = '%.1f%%')
plt.legend(loc=2) # legend의 위치가 조정됨.
plt.show()