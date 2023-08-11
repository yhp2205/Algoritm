#연속한 숫자의 곱을 구하는 알고리즘
#input : n

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

print(fact(1))
print(fact(5))
print(fact(10))

#연속한 숫자의 곱을 구하는 알고리즘 2

def fact(n):
    if n <=1:
        return 1
    return n*fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))
