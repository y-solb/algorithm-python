# 5. 상하좌우

# 여행가는 N*N크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1*1 크기의 정사각형으로 나누어져 있습니다.
# 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다. 
# 여행가는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)입니다. 
# L: 왼쪽으로 한 칸 이동 
# R: 오른쪽으로 한 칸 이동 
# U: 위로 한 칸 이동 
# D: 아래로 한 칸 이동

# 입력 예시
# 5
# R R R U D D
# 출력 예시
# 3 4

n=int(input())
plans=input().split()

x,y=1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n: # 공간을 벗어나는 경우 무시
        continue
    x,y=nx,ny
print(x,y)