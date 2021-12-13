# 9. 반복문

# while문
i=1
result=0

while i<=9:
    if i % 2 ==1:
        result+=i
    i+=1
print(result)

# 무한 루프를 조심하기! (반복문을 탈출할 수 있는지 확인)

# for문
array=[9,8,7,6,5]

for x in array:
    print(x)
    
# range(시작 값, 끝 값 + 1) : 연속적인 값을 차례대로 순회할 때
result2=0

# i는 1부터 9까지 모든 값을 순회
for i in range(1,10):
    result2+=i
print(result2)

# continue : 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때
result3=0

for i in range(1,10):
    if i%2==0:
        continue
    result3+=i # 홀수의 합만 더하기
print(result3)

# break : 즉시 탈출
i=1
while True:
    print('현재 i의 값:',i)
    if i==5:
        break
    i+=1

# 특정 번호의 학생은 제외하기
scores=[90,85,77,65,97]
cheating_student_list={2,4}

for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if scores[i]>=80:
        print(i+1,'번 학생은 합격입니다.')

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
    print()