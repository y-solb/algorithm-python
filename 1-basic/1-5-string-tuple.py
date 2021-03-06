# 5. 문자열, 튜플 자료형
# 문자열 자료형
data='Hello'
print(data)

data2="Don't you know \"Python\"?"
print(data2)

a='Hello'
b='World'
print(a+" "+b)

s="string"
print(s*3)

x='ABCDEF'
print(x[2:4])

# 튜플 자료형
# - 한번 선언된 값을 변경할 수 없다.
# - 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용한다.
# - 리스트에 비해 상대적으로 공간 효율적이다.
y=(1,2,3,4,5,6,7,8,9)

# 네번째 원소만 출력
print(y[3])

# 두번째 원소부터 네번째 원소까지
print(y[1:4])

# 튜플을 사용하면 좋은 경우
# - 서로 다른 성질의 데이터를 묶어 관리해야 할 때 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용한다.
# - 데이터의 나열을 해싱의 키 값으로 사용해야 할 때 튜플은 변경이 불가능하므로 리스트와 다르게 키값으로 사용할 수 있다.
# - 리스트보다 메모리를 효율적으로 사용해야 할 때