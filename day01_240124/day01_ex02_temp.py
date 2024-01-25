import csv
#
f = open('daegu-utf8.csv', 'r', encoding='utf-8')
#open(파일, 'r') =====> 읽기용으로 파일 open # open(파일, 'w') ======> 쓰기용으로 파일 open
data = csv.reader(f, delimiter=',') # delimiter = ',' ----> 구분자가 ','임을 나타냄.
count=0

for row in data : # data 안에는 daegu.csv파일 전체의 객체  # 내부에서 1줄씩 읽어옴.
    if count>5 :            # *read() 함수 호출 없앰.
        break
    else :
        print(row) # 1 라인 출력
    count+=1

f.close() # 파일을 열면 다시 닫아야 함.
