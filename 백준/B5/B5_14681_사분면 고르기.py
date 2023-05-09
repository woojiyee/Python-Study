# 1st
'''
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print("1")
    else:
        print("4")
else:
    if y > 0:
        print("2")
    else:
        print("3")
'''        
# 백준 맞았습니다.
        

# 23.4.28 복습

#1st

x = int(input())
y = int(input())
# Quadrant n는 제n사분면이라는 뜻
quadrant = 0

if x >0 and y >0:
    quadrant = 1
elif x<0 and y>0:
    quadrant =2
elif x<0 and y<0:
    quadrant = 3
else:
    quadrant = 4

print(quadrant)

# 백준 맞았습니다.