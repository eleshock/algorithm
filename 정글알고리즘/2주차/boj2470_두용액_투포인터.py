n = int(input())

arr = list(map(int, input().split()))
arr.sort()

target = float('inf')
ans = []

start = 0
end = n-1

while start < end:
    tot = arr[start] + arr[end]
    if abs(tot) < target:
        target = abs(tot)
        ans = [arr[start], arr[end]]
    
    if tot < 0:
        start += 1
    else:
        end -= 1

print(ans[0], ans[1])