# 10. 함수와 람다 표현식

def addFun(a,b):
    return a+b

result=addFun(3,6)
print(result)

# global 지역변수를 만들지 않고, 함수 바깥에 선언된 변수를 참조
x=0

def func():
    global x
    x+=1
    
for i in range(10):
    func()

print(x)

# 여러 개의 반환 값
def operator(c,d):
    add_var=c+d
    subtract_var=c-d
    multiply_var=c*d
    divide_var=c/d
    return add_var,subtract_var,multiply_var,divide_var

add, sub, mul, div=operator(7,3)
print(add, sub, mul, div)

# 람다 표현식
print((lambda one, two : one+two)(3,7))

array=[('홍길동',50),('이순신',32),('아무개',80)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x:x[1]))

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

result=map(lambda a,b:a+b, list1, list2)
print(list(result))
