t = int(input())

d = []
for i in range(t):
    s = input().split()
    d.append([int(s[0]), s[1]])

for j in range(t):
    for k in range(len(d[j][1])):
        print(d[j][0] * d[j][1][k], end="")
    print()