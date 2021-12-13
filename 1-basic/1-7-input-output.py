# 7. 기본 입출력
# input() 한 줄의 문자열을 입력받는 함수
# map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 데이터의 개수 입력
n=int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data=list(map(int, input().split()))
print(data)

# a, b, c를 공백을 기준으로 구분하여 압력
a,b,c=map(int,input().split())
print(a,b,c)

# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# sys.stdin.readline()을 이용
# 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip()를 함께 사용

import sys

# 문자열 입력 받기
data2=sys.stdin.readline().rstrip()
print(data2)

# 출력할 변수들
x=1
y=2
print(x,y)
 
# 기본적으로 출력 이후에 줄바꿈을 수행 원치 않는 경우 end를 이용 
print(7,end=" ")
print(8,end=" ")

answer=7
print("정답은 "+ str(answer)+"입니다.")

# 파이썬 3.6부터 사용가능하며 문자열 앞에 접두사 f를 붙여 사용
eight=8
print(f"팔은 {eight}입니다.")