# 음료 얼려 먹기
# n*m 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시가 된다.
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 입력
# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 3

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1
        # 상하좌우 재귀적으로 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

result=0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
            
print(result)