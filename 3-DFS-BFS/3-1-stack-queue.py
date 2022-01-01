# DFS/BFS : 그래프 탐색 알고리즘
# 탐색은 많은 양의 데이터 중에 원하는 데이터를 찾는 과정을 말한다.

# 스택 자료구조
# 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)
stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

# 큐 자료구조
# 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)
from collections import deque

queue=deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력

