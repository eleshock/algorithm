from itertools import permutations

n = int(input())
k = int(input())


# 카드를 받아서 문자형으로 리스트에 담음(합치기 편하게)
array = []
for i in range(n):
    array.append(str(input()))

# 모든 카드의 순열을 cards 리스트에 담음
cards = list(permutations(array, k))

# 중복방지를 위해 set(집합자료형) 사용
sangKeun = set()

# cards 리스트에 담긴 각 튜플 내 문자들을 join으로 합친 뒤 집합에 추가(중복은 걸러짐)
for card in cards:
    sangKeun.add("".join(card))

print(len(sangKeun))
