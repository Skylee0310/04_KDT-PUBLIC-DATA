import csv

# 최고 기온 및 최고 기온의 날짜 구하기
# [0]날짜 , [1]지점 ,[2] 평균기온, [3] 최저기온, [4] 최고기온
def get_minmax_temp(data) :
    header = next(data) #첫 행을 읽고 다음 행으로 지정함으로서 실데이터에 바로 접근.

    min_temp = 100 # 최소 기온을 저장할 변수 초기화(가장 큰 값) --> 절대 나올 수 없는 수치
    min_date = '' # 최소 기온의 날짜를 저장할 문자열 변수 초기화

    max_temp = -999 # 최고 기온을 저장할 변수 초기화(가장 작은 값) ---> 절대 나올 수 없는 수치
    max_date = '' # 최고 기온의 날짜를 저장할 문자열 변수 초기화

    for row in data : # 함수에 입력한 데이터를 for문으로 차례차례 읽어옴.
        if row[3] == '': # 최소기온 값이 없으면
            row[3] = 100 # 값을 100으로 지정.
        row[3] = float(row[3]) # csv 파일 데이터는 문자열로 취급. 산술연산을 위해 변환.(최댓값/최소값)

        if row[4] == '': # 마지막 데이터가 없는 경우.
            row[4] = -999 #값을 -999로 지정.
        row[4] = float(row[4]) # 산술연산을 위해 문자열을 실수로 변환.

        if row[3] < min_temp: # 정상 값일때
            min_temp = row[3] # 값 계속 업데이트
            min_date = row[0]
        if row[4] > max_temp :
            max_temp = row[4]
            max_date = row[0]

    print('-', 50)
    print(f'대구 최저 기온 날짜 : {min_date}, 온도 : {min_temp}')
    print(f'대구 최고 기온 날짜 : {max_date}, 온도 : {max_temp}')

def main() :
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    get_minmax_temp(data)
    f.close()

main()
