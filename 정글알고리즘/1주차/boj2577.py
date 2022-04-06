a = int(input())
b = int(input())
c = int(input())


x = str(a * b * c)

z = []
for i in range(10):
    y = x.count(str(i))
    z.append(y)
    
for i in range(10):
    print(z[i])

# 2번째 풀이
# a = int(input())
# b = int(input())
# c = int(input())

# mul = str(a*b*c)

# d = [0] * 10
# for i in mul:
#     d[int(i)] += 1

# for j in d:
#     print(j)