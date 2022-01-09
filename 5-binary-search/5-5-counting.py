# n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이때 수열에서 x가 등장하는 횟수를 계산해라. 
# 예를 들어 수열 {1,1,2,2,2,2,3}이 있을 때 x=2라면 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다.
# 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다.
# 수열의 원소 중에서 값이 x인 원소의 개수를 출력한다. 값이 x인 원소가 하나도 없다면 -1을 출력한다.
# 입력
# 7 2
# 1 1 2 2 2 2 3
# 출력
# 4

# from bisect import bisect_left, bisect_right

# n,x=list(map(int,input().split()))
# array=list(map(int,input().split()))

# result=bisect_right(array,x)-bisect_left(array,x)

# if result<=0:
#     print(-1)
# else:
#     print(result)

from bisect import bisect_left, bisect_right

def count_by_range(array,left_value,right_value):
    right_index=bisect_right(array,right_value)
    left_index=bisect_left(array,left_value)
    return right_index-left_index

n,x=map(int,input().split())
array=list(map(int,input().split()))

count=count_by_range(array,x,x)

if count==0:
    print(-1)
else:
    print(count)