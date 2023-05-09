a, b, c = map(int,input().split())
money = 0

if a == b and b == c:
    money = 10000 + a*1000
elif a == b or c == a:
    money = 1000 + a*100
elif b == c:
    money = 1000 + b*100
else:
    money = max(a,b,c) * 100

print(money)

# 파이썬에서는 &&,|| 연산자 대신 and,or 사용!
# 백준 맞았습니다
