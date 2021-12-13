# 11. 표준 라이브러리

# sum()
result=sum([1,2,3,4,5])
print(result)

# min(), max()
min_result=min(7,3,5,2)
max_result=max(7,3,5,2)
print(min_result,max_result)

# eval()
result2=eval("(3+5)*7")
print(result2)

# sorted()
result3=sorted([9,1,8,5,4])
reverse_result=sorted([9,1,8,5,4],reverse=True)
print(result3)
print(reverse_result)

# sorted() with key
array=[('홍길동',35),('이순신',75),('아무개',50)]
result4=sorted(array,key=lambda x:x[1],reverse=True)
print(result4)

# 순열
# 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
from itertools import permutations

data=['A','B','C']

result5=list(permutations(data,3))
print(result5)

# 조합
# 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
from itertools import combinations

data2=['A','B','C']

result6=list(combinations(data2,2))
print(result6)

# 중복 순열
from itertools import product

data3=['A','B','C']

result7=list(product(data3,repeat=2)) # 중복을 허용하여 2개를 뽑는 순열 구하기
print(result7)

# 중복 조합
from itertools import combinations_with_replacement

data4=['A','B','C']

result8=list(combinations_with_replacement(data4,2)) # 중복을 허용하여 2개를 뽑는 조합 구하기
print(result8)

# Counter
# 등장 횟수를 세는 기능, 내부 원소가 몇 번씩 등장했는지

from collections import Counter

counter=Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 변환

# 최대 공약수와 최소 공배수
import math

# 최소 공배수를 구하는 함수
def lcm(a,b):
    return a*b // math.gcd(a,b)

a=21
b=14

print(math.gcd(21,14)) # 최대 공약수 계산
print(lcm(21,14)) # 최소 공배수 계산