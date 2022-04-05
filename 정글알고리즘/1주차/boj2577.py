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