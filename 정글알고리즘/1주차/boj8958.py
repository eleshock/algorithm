n = int(input())

d = []

for i in range(n):
    a = input()
    d.append(a)


for case in d:
    sum = 0
    count = 0
    for j in range(len(case)):
        if case[j] == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)
