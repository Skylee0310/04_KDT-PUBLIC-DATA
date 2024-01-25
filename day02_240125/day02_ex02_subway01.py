import csv
# 시간대별 지하철 이용 인원 수.
result = [] # 역 저장할 리스트
total_number = 0 # 새벽 4시 승차 인원
with open('subwaytime.csv', encoding= "utf-8-sig") as f : #encoding 빼먹지 않기. 한글 깨짐 문제를 해결하기 위해 utf-8-sig
    data = csv.reader(f)
    next(data)
    next(data)
    for row in data :
        row[4:] = map(int, row[4:]) # 인덱스 4부터 끝까지 int로 변경.
        total_number += row[4]
        result.append(row[4])

print(f'총 지하철 역의 수 : {len(result)}')
print(f'새벽 4시 승차인원 : {total_number:,}')