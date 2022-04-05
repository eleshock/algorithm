d = []

for i in range(9):
    a = int(input())
    d.append(a)

print(max(d))
print(d.index(max(d))+1)