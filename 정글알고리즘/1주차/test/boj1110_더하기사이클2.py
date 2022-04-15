n = int(input())

count = 0

num = n

while True:
    if num < 10:
        a = str(0) + str(num)

    else:
        a = int(str(num)[0]) + int(str(num)[1])
    
    if num == n:
        print(count)
        break