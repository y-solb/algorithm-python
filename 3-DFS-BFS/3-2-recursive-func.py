# 재귀 함수
# 자기 자신을 다시 호출하는 함수
# 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
# 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용한다.
def recursive_func(i):
    if i==100:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    recursive_func(i+1)
    print(i,'번째 재귀함수를 종료합니다.')
    
recursive_func(1)

# 팩토리얼 구현 예제
# n!=1*2*3* ... *(n-1)*n
# 수학적으로 0!와 1!의 값은 1이다.

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print('반복적으로 구현:',factorial_iterative(5))
print('재귀적으로 구현:',factorial_recursive(5))

# 최대공약수 계산 (유클리드 호제법)
# 두개의 자연수의 공통된 약수 중에서 가장 큰 값
# 두 자연수 a,b에 대하여 a를 b로 나눈 나머지를 r이다.
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
    
print(gcd(192,162))