#리스트에서 특정 숫자 위치 찾기
#input : 리스트, 찾는 값

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return i

    return -1

v=[17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))


#연습문제
#찾는 값이 나오는 모든 위치를 출력하는 탐색 알고리즘
#없으면 빈 리스트가 나오도록 출력

def search_list(a, x):
    i = 0
    q = []
    while i <len(a):
        if a[i] == x:
            q += [i]
        i += 1

    return q

v=[17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
