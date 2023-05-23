num = int(input())
original = num
sum = 0
new = 0
notEqual = True
cycle = 0

while notEqual:
    if original < 10:
        sum = original
    else:
        sum = original//10 + original%10
    new = (original%10) * 10 + sum%10

    cycle += 1

    if new == num :
        notEqual = False

    original = new

print(cycle)

# 백준 맞았습니다.