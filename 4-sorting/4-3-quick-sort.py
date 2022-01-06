# 퀵 정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나이다.
# 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터로 설정한다.
# 퀵 정렬이 빠른 이유 : 이상적인 경우 분할이 절반씩 일어난다면 전체 연상 횟수로 O(NlogN)를 기대할 수 있다.
# 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다.
# 최악의 경우 O(N²)의 시간 복잡도를 가진다.

# array=[5,7,9,0,3,1,6,2,4,8]

# def quick_sort(array,start,end):
#     if start >= end:
#         return
#     pivot=start
#     left=start+1
#     right=end
#     while(left<=right):
#         while(left<=end and array[left]<=array[pivot]):
#             left+=1
#         while(right>start and array[right]>=array[pivot]):
#             right-=1
#         if(left>right):
#             array[right], array[pivot]=array[pivot],array[right]
#         else:
#             array[left], array[right]=array[right],array[left]
    
#     quick_sort(array, start, right -1)
#     quick_sort(array, right+1, end)

# quick_sort(array, 0, len(array)-1)
# print(len(array))
# print(array)

# 다른 방식
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:]
    print(tail)
    
    left_side=[x for x in tail if x <= pivot]
    right_side=[x for x in tail if x > pivot]
    
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))