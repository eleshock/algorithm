import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


#지수 법칙 a**(m+n) = (a**m)*(a**n)
#나머지 분배 법칙 (a*b)%c = (a%c)*(b%c)%c
def division(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        answer = division(a, b // 2, c)
        return (answer * answer) % c
    else:
        answer = division(a, b // 2, c)
        return ((answer * answer % c) * a) % c

print(division(a, b, c))