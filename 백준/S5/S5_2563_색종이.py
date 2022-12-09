'''
1. 색종이 수 입력 받기
2. 색종이 수만큼 반복문
    색종이 시작점 x,y 좌표 받기
    '''

li = ["bcad","abc","aabef","cab","abc"]
li= list(set(li))
#print("set 후",set(li))
#li.set()
print("set 후",li)
li.sort()
print("사전순 sort 후",li)
li.sort(key=len)
print("길이 순 sort 후",li)
