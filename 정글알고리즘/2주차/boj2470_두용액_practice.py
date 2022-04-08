n = int(input())
list_liquid = list(map(int, input().split()))
list_liquid = sorted(list_liquid)

def ps(x, y, ans_sum) -> bool:
    if abs(list_liquid[x] + list_liquid[y]) < abs(ans_sum):
        return True
    return False

def solve(x=0, y=len(list_liquid)-1):
    ans_x = x
    ans_y = y
    ans_sum = list_liquid[x] + list_liquid[y]
    while x < y:
        # 양수, 음수는 여기서 따지면 됨
        is_ans = ps(x, y, ans_sum)
        if is_ans:
            ans_x = x
            ans_y = y
            ans_sum = list_liquid[ans_x] + list_liquid[ans_y]
        if list_liquid[ans_x] + list_liquid[ans_y] > 0:
            y-=1
        else:
            x+=1
    print(f'{list_liquid[ans_x]} {list_liquid[ans_y]}')

solve()