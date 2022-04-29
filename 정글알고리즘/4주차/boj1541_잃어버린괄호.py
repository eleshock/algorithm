import sys
input = sys.stdin.readline

no_minus = list(map(str, input().rstrip().split('-')))

res = []
for no_plus in no_minus:
    res.append(sum(list(map(int, no_plus.split('+')))))
    
print(res[0] - sum(res[1:]))
