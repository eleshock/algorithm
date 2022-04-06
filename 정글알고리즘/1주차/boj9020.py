import math

# 입력값 받아오기
n = int(input())

# 테스트 케이스를 list에 넣기
test_case = []
for _ in range(n):
    a = int(input())
    test_case.append(a)

# 소수판별 함수 정의
def isPrime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

# 골드바흐 파티션 중 조건을 만족하는 파티션을 출력시키고 break로 빠져나옴
for i in range(n):
    for j in range(test_case[i] // 2, 0, -1):
        if isPrime(j) and isPrime(test_case[i]-j):
            print(j, test_case[i]-j)
            break



# 2번째 풀이
# import math

# t = int(input())

# test_case = [int(input()) for _ in range(t)]

# d = [False] * 10001

# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# for i in range(10001):
#     if isPrime(i):
#         d[i] = True

# for case in test_case:
#     for i in range(int(case/2), 0, -1):
#         if d[i] and d[case-i]:
#             print(i, case-i)
#             break