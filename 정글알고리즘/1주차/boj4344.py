c = int(input())

scores = []

for _ in range(c):
    a = list(map(int, input().split()))
    scores.append(a)

for score in scores:
    avgScore = sum(score[1:]) / score[0]
    count = 0
    for i in range(1, len(score)):
        if score[i] > avgScore:
            count += 1
    print("%0.3f%%" % (count / score[0] * 100))