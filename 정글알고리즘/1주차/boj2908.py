a, b = map(str, input().split())

a_reverse = a[::-1]
b_reverse = b[::-1]

if a_reverse > b_reverse:
    print(int(a_reverse))
else:
    print(int(b_reverse))
