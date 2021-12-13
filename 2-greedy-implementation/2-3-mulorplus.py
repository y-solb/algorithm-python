# 3. 곱하기 혹은 더하기

# 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '*' 혹은 '+'를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하시오.
# 단, +보다 *를 먼저 계산하는 일반적인 방식과 달리 모든 연산은 왼쪽에서 오른쪽 순서대로 이루어집니다.
# 예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0+2)*9)*8)*4)=576
# 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

# s=list(map(int, input()))
# print(s)

# result=0

# for i in s:
#     if i<=1 or result<=0:
#         result=+i
#     else:
#         result=result*i
        
# print(result)

data=input()
result=int(data[0])

for i in range(1,len(data)):
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
        
print(result)