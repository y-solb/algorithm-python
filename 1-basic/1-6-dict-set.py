# 6. 사전, 집합 자료형
# 사전 자료형
# - 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형 (리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됨)
# - 원하는 '변경 불가능한 자료형'을 키로 사용할 수 있다.
# - 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

data=dict()
data['사과']='Apple'
data['바나나']='Banana'
data['코코넛']='Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
   
 
# keys() 키 데이터만 뽑아서 리스트로 이용할 때
# values() 값 데이터만 뽑아서 리스트로 이용할 때
data2={
    '홍길동':97,
    '이순신':80,
    '세종대왕':100
}
# 키 데이터만 담은 리스트
key_list=data2.keys()

# 값 데이터만 담은 리스트
value_list=data2.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data2[key])

# 집합 자료형
# 중복을 허용하지 않고 순서가 없다.
# 집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있다. (set()함수 이용)
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

# 집합 자료형 초기화 방법 1
data3=set([1,1,2,3,4,4,5])
print(data3)

# 집합 자료형 초기화 방법 2
data4={1,1,2,3,4,4,5}
print(data4)

# 집합 자료형 연산(합집합, 교집합, 차집합)
a=set([1,2,3,4,5])
b=set([3,4,5,6,7])

# 합집합
print(a|b)

# 교집합
print(a&b)

# 차집합
print(a-b)

data5=set([1,2,3])
print("data5")
print(data5)

# 새로운 원소 추가
data5.add(4)
print(data5)

# 새로운 원소 여러개 추가
data5.update([5,6])
print(data5)

# 특정한 값을 갖는 원소 삭제
data5.remove(3)
print(data5)

