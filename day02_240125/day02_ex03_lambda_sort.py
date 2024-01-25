# lambda를 이용한 정렬.
import operator

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

print('[lambda] dict 정렬 : key 기준 오름차순')
res = sorted(names.items(), key =(lambda x: x[0]))
print(res)
print()

print('[lambda] dict 정렬 : value 기준, 내림차순')
res = sorted(names.items(), key=(lambda x : x[1]), reverse = True)
print(res)
print()

# import operator
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

sorted_x = sorted(names.items(), key = operator.itemgetter(0))
print('[operator] dict 정렬 : key 기준, 오름차순')
print(sorted_x)
print()

sorted_x = sorted(names.items(), key = operator.itemgetter(1), reverse=True)
print('[operator] dict 정렬 : value 기준, 내림차순')
print(sorted_x)