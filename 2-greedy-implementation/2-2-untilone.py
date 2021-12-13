# 2. 1이 될 때까지

# 어떠한 수 1이 될 때 까지 두 과정 중 하나를 반복적으로 선택하여 수행
# (1) N에서 1을 뺍니다.
# (2) N을 K로 나눕니다.
# 예를 들어 N이 17 K가 4라면 최소 횟수는 3입니다.
# N,K가 주어질때 N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야 하는 최소 횟수를 구하세요.

# 내 소스
# n,k=map(int,input().split())

# count=0

# while True:
#     if n%k !=0:
#         n=n-1
#         count+=1
#         continue
#     n=n//k
#     count+=1
#     if n==1:
#         break
# print(count)

n,k=map(int,input().split())

result=0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target=(n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k
    
result+=(n-1)
print(result)