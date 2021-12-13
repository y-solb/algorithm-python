# 리스트 자료형
# 인덱싱(Indexing) : 인덱스 값을 입력하여 리스트의 특정한 원소에 접근
# 슬라이싱(Slicing) : 연속적인 위치를 갖는 원소들을 가져와야 할 때
a=[1,2,3,4,5,6,7,8,9]

print(a[-1]) # 뒤에서 첫번째 원소 출력
print(a[1:4]) # 두번째 원소부터 네번째 원소까지

# 리스트 컴프리헨션
array=[i for i in range(10)]

print(array)

# 0부터 19까지 수 중에서 홀수만 포함하는 리스트
array2=[i for i in range(20) if i%2==1]
print(array2)

# N * M 크기의 2차원 리스트 초기화
n=4
m=3
array3=[[0]*m for _ in range(n)]
print(array3)

b=[1,4,3]
print("기본 리스트: ",b)

b.append(2)
print("삽입: ",b)

b.sort()
print("오름차순 정렬: ",b)

b.sort(reverse=True)
print("내림차순 정렬: ",b)

b.reverse()
print("원소 뒤집기: ",b)

b.insert(2,3)
print("인덱스 2에 3추가: ",b)

print("값이 3인 데이터 개수: ",b.count(3))

b.remove(1)
print("값이 1인 데이터 삭제: ",b)

# 특정 값을 가지는 원소를 모두 제거하기
c=[1,2,3,4,5,5,5]
remove_set={3,5}

result=[i for i in a if i not in remove_set]
print(result)
