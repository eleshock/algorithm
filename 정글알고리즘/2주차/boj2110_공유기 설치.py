n, c = map(int, input().split())

array = [int(input()) for _ in range(n)]

array.sort()

start = 1 #최소 Gap 초기값은 1로 고정
end = array[-1] - array[0] #최대 Gap 초기값은 입력받는 배열에 따라 달라짐
answer = 0

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, n):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

binary_search(array, start, end)
print(answer)