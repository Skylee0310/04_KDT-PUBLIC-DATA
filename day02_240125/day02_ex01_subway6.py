# 전체 지하철 역 파이차트 분석.

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

label = ['유임승차', '유임하차', '무임승차', '무임하차']
color_list = ['#ff9999', '#ffc000', '#8fd9b6', '#d365d0']
pic_count =0 # 파이차트 개수 누적할 변수.
with open('subwayfee.csv', encoding='utf-8-sig') as f :
    data = csv.reader(f)
    next(data)

    # 한글 폰트 안 깨지도록 설정.
    if(platform.system() == 'Windows') :
        plt.rc('font', family = 'Malgun Gothic')
    else :
        plt.rc('font', family = 'AppleGothic')

    #
    for row in data : # 한 행씩 읽어오기.
        for i in range(4, 8) :
            row[i] = int(row[i]) # 열 인덱스 4~7번 정수로 변환

        print(row)
        plt.figure(dpi = 100) # 저장할 그림 파일의 dpi 설정.
        plt.title(row[3]+' ' +row[1]) #제목
        plt.pie(row[4:8], labels =label, colors = color_list, autopct = '%.1f%%', shadow = True)
        plt.savefig('img/'+row[3]+' '+row[1]+'.png') # 4개 항목에 대한 파이 차트 작성.
        plt.close()

        # 10개의 역만 저장.
        pic_count +=1
        if pic_count>=10 :
            break