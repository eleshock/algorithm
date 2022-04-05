

a, b, v = map(int, input().split())

count = int((v-b) / (a-b))

print(count if (v-b)%(a-b) == 0 else count + 1)


# 또는 이렇게도 풀 수 있다
# import math
# print(math.ceil((v-a) / (a-b)) + 1)
# 변경사항이 풀리퀘에 반영되는지 확인해봅시다