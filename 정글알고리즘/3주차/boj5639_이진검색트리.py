import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def postOrder(left,right):
    #순서 역전시 종료
    if left>right:
        return
    
    root = preOrder[left] #전위순회에서의 0번째 인덱스가 root노드
    div = left + 1 #루트노드 다음 인덱스(1번)를 div로 초기화

    # left와 right를 나누기 위한 div값 구하기
    while div <= right: #div를 right(끝값)까지 1씩 증가시키며 // 참고)right라는 제한을 안두고 True로 하면 오른쪽 서브트리가 없을 경우 div가 계속 증가하기 때문에 right라는 제한 필요
        if preOrder[div] > root: # 루트보다 큰 값이 나오면 break
            break
        div += 1
    
    #왼쪽 서브트리
    postOrder(left+1, div-1)
    #오른쪽 서브트리
    postOrder(div, right)
    #후위순회이므로 마지막에 root노드를 print
    print(root)

#입력받을 원소 리스트
# 몇 개를 받을지 주어지지 않기 때문에 for문 사용불가
preOrder =[]
while True:
    try:
        preOrder.append(int(input()))
    except:
        break
# preOrder = [50, 30, 24, 5, 28, 45, 98, 52, 60]

postOrder(0,len(preOrder)-1)
