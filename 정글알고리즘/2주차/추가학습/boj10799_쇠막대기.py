# 10799
rod = input().strip()
stack = []
cnt = 0

for i in range(len(rod)):
	if rod[i] == '(':
		stack.append('(')
	
	else: # )
		if rod[i-1] == '(':
			stack.pop()
			cnt += len(stack)
		else:
			# )
			stack.pop()
			cnt += 1

print(cnt)