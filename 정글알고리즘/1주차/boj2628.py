x, y = map(int, input().split())
n = int(input())

rows = [0, y]
columns = [0, x]

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        rows.append(a[1])
    else:
        columns.append(a[1])
rows.sort()
columns.sort()

pieces = []
for i in range(len(rows)-1):
    for j in range(len(columns)-1):
        area = (rows[i+1]-rows[i]) * (columns[j+1]-columns[j])
        pieces.append(area)
        
print(max(pieces))