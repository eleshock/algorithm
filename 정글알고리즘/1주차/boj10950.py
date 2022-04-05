t = int(input())

t_list = []

for _ in range(t):
    a, b = map(int, input().split())
    t_list.append(a+b)

for i in range(t):
    print(t_list[i])