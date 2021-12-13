# 8. 조건문

x=15
if x>=10:
    print("x>=10")
    
if x>=0:
    print("x>=0")
    
if x>=30:
    print("x>=30")
    
# if ~ elif ~ else
score=99

if score>=90:
    print('학점:A')
elif score>=80:
    print('학점:B')
elif score>=70:
    print('학점:C')    
else:
    print('학점:F')
    
# 비교 연산자
# ==,!=, >, <, >=, <=

# 논리 연산자
# X and Y, X or Y, not X

# 기타 연산자
# X in 리스트 : 리스트 안에 X가 있을 때 참
# X not in 문자열 : 문자열 안에 X가 들어 있지 않을 때 참
# pass : 이무것도 처리하고 싶지 않을 때

# 조건문의 간소화
score=85
if score>=80: result="success"
else: result='fail'
print(result)

score2=70
result2='success' if score2>=80 else 'fail'
print(result2)

# x>0 and x<20 , 0<x<20 둘 다 가능