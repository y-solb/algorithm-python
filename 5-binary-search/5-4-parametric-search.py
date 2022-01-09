# 파라메트릭 서치: 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
# 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

# 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춘다.
# 절단기에 높이를 지정해주면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
# 손님이 왔을 떄 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성해라.

# 첫째 줄에 떡 개수 N과 요청한 떡의 길이 M이 주어진다.
# 둘째 줄에는 떡의 개별 높이가 주어진다. 

# 입력
# 4 6
# 19 15 10 17

# 출력
# 15

n,m=list(map(int,input().split(' ')))
array=list(map(int,input().split()))

start=0
end=max(array)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    print(mid,start,end)
    for i in array:
        if i>mid:
            total+=i-mid
    if total<m:
        end=mid-1
    else:
        result=mid
        start=mid+1
        
print(result)