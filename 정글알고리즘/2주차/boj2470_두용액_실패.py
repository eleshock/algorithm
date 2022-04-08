n = int(input())

array = list(map(int, input().split()))
array.sort()

target = float('inf')

pos = []
neg = []

for num in array:
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)

if not pos:
    print(array[-1], array[-2])
elif not neg:
    print(array[0], array[1])
else:
    for i in range(len(neg)):
        for j in range(len(pos)-1,-1,-1):
            if abs(neg[i]+pos[j]) < target:
                target = abs(neg[i] + pos[j])
                num1 = neg[i]
                num2 = pos[j]
    print(num1, num2)