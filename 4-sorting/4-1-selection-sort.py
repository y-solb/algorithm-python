# 정렬(sorting) : 데이터를 특정한 기준애 따라 순서대로 나열하는 것

# 선택 정렬 : 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i] # 스와프
    
print(array)

# 선택 정렬의 시간 복잡도
# 선택 정렬은 n번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
# N+(N-1)+(N-2)+ ... +2
# 이는 (N²+N-2)/2로 표현할 수 있는데, 빅오 표기법에 따라서 O(N²)라고 작성한다.