# 1st
'''
time, min = map(int,input().split())
cook = int(input())

print(time+cook//60,(min+cook)%60)
'''
# 백준 틀렸습니다.

#2nd
'''
time, min = map(int,input().split())
cook = int(input())

print((time+cook//60)%24,(min+cook)%60)
'''
# 백준 틀렸습니다

# 3rd
time, min = map(int,input().split())
cook = int(input())

print((time+(min+cook)//60)%24,(min+cook)%60)

# 출력하는 값 중 시간에서 (min+cook)//60 에서 min을 괄호안에 안 더해줘도 틀리고 
# (time + (min+cook)//60)%24에서 %24 를 안 해줘도 틀림  => 둘 다 해줘야함
# 백준 맞았습니다.