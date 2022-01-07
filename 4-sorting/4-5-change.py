# 두 배열의 원소 교체
# 두 개의 배열 A와 B를 가지고 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
# 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
# N,K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력해라.

# 입력
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

# 출력 
# 26

# n,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))

# a.sort()
# b.sort()

# for i in range(k):
#     a[i],b[-i]=b[-i],a[i] # a[i]와 b[-i]를 비교해 더 크다면 교체하는 것이 필요
#     print('hi')
    
# print(sum(a))


n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break
    
print(sum(a))