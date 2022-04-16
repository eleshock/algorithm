import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postOrder(left,right):
    #순서 역전시 종료
    if left>right:
        return
    
    root = preOrder[left] #전위순회에서의 0번째 인덱스가 root노드
    div = left + 1 #루트노드 다음 인덱스(1번)를 div로 초기화

    # left와 right를 나누기 위한 div값 구하기
    while div <= right: #div를 1씩 증가시켜 right까지 가는 동안
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
preOrder =[]
while True:
    try:
        preOrder.append(int(input()))
    except:
        break
# preOrder = [50, 30, 24, 5, 28, 45, 98, 52, 60]

postOrder(0,len(preOrder)-1)
