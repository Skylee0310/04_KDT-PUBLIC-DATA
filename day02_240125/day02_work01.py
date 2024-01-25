'''
공공 데이터 과제 #2
-> 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력.

1. 하차 인원수 컬럼 모아서 총 하차 인원 컬럼 만들기.
2. 최댓값을 비교해서 업데이트하기.
3. 하차인원 출력.

'''

#1) 모듈 불러오기. -> csv, plt, ko-
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


# 지하철 호선을 입력하면 최다 하차역, 하차인원을 알려주는 함수.
def subway(subline) :
    with open('subwaytime.csv', encoding='utf-8-sig') as f :
        data = csv.reader(f)
        next(data)
        next(data)

        passengerlist = [] # 하차 인수 리스트
        global station_max, max_passenger
        station_max = '' # 최다 하차 역
        max_passenger = 0 # 최다 하차 인수
        #subline = '1호선' # 지하철 호선.

        for row in data :
            row[11] = int(row[11])
            row[13] = int(row[13])
            passenger = row[11]+row[13]
            if row[1] == subline :
                passengerlist.append(passenger)
                if passenger > max_passenger :
                    max_passenger=passenger
                    station_max = row[3]
        print(f'출근 시간대 {subline} 최대 하차역 : {station_max}, 하차인원 : {max_passenger:,}')


#지하철 호선을 입력하면 최다 하차역, 최다 인원수를 알려주는 subway 함수에 리스트 값을 집어 넣어 모두 출력.
def seven_line() :
    global xdata, ydata
    xdata=[]
    ydata=[]
    linelist = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']
    for i in linelist :
         subway(i)
         xdata.append(i +' ' + station_max)
         ydata.append(max_passenger)

#값 출력.
seven_line()

#그래프 그리기.
plt.figure(figsize=(10,8))
plt.bar(xdata, ydata)
plt.xticks(rotation = 20)
plt.title('출근 시간대 지하철 노선별 최다 하차 인원 및 하차역')
plt.show()