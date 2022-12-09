# 알고리즘
'''
1. 테스트 케이스 개수(T) 입력받기
2. 각 테스트 개수의 반복 횟수( R ), 문자열( S ) 입력받기
3. 첫 문자열 1번째 문자가 R번 반복, 2번째 문자가 R번 반복 ... 문자열 마지막 문자까지 R번 반복
4. 두번째 문자열의 1번째 문자 R번 반복,...
-> 문자 R번 반복 - 반복 요인 : 문자열 S를 이루는 문자, 다음 문자로 넘어갈 때마다, 횟수 :문자열 길이만큼
    -> for i in S: i가 R번 찍히기
-> 문자 S의 반복 - 반복 요인: 테스트 케이스 개수만큼 
    -> for i in T : 하나의 테스트 케이스 하나씩 코드 돌리기?(3번 진행하기)
'''

#1st
'''
# 테스트 케이스 개수
T = int(input("테스트 케이스 수:"))

# 테스트 케이스 리스트
#strings = [[0,0]]
strings = [[0,0] for i in range(T)]

for i in range(T):
    #1 strings[i,0], strings[i,1] = input("문자열 입력").split()
    #2 a,b = input("문자열 입력").split()
    #3 strings[i] = list(input("문자열 입력").split()) 

#1,3 print("strings",strings)
#2 print('a',a)
#2 print('b',b)
'''

#2nd
'''
# 테스트 케이스 개수
T = int(input("테스트 케이스 수:"))

# 테스트 케이스 리스트
strings = [[]]

for i in range(T):
    strings.append(input("문자열 입력").split())

print("strings",strings) # [[],['2','sss'],['4','mmm']]

# 2nd 코드 문제점
1. [[]]로 이차원 리스트 선언하면 젤 첫행 리스트에 빈 값이 들어가고 그 뒤에
   append()로 값 넣으면 두번째 행 리스트부터 값이 추가됨.
'''


#3rd
'''
# 테스트 케이스 개수
T = int(input("테스트 케이스 수:"))

# 테스트 케이스 리스트
strings = list(list())

for i in range(T):
    strings.append(input("문자열 입력").split())

print("strings",strings) # [['2','sss'],['4','mmm']]
'''

#4th

# 테스트 케이스 수
T = int(input("테스트 케이스 수:"))
# 반복 횟수
r = list()
# 문자열
s = list()
# 반복된 문자열
answer = list()

for _ in range(T):
    # r[i], s[i] = tuple(input("반복 횟수, 문자열:").split())
    set = input("반복 횟수, 문자열:").split() # 2 abc,3 def
    # r[i] = set[0]
    # s[i] = set[1]
    r.append(set[0])
    print(set[1])
    s.append(set[1]) # print(s) -> [abc,def]
    # s.extend(set[1]) # print(s) -> [a,b,c,d,e,f]

print("r:",r,'s',s)
# 문자열 리스트 안에 문자마다 반복
# i: 문자열 개수
for i in range(T):
    strings = ''

    # 문자열에 문자마다 반복
    # s[i]: 문자열 리스트에 i번째 문자열
    # j: 문자열에 문자
    for j in s[i]:
        print('j',j)
        strings += j * int(r[i])
    
    answer.append(strings)

for i in range(T):
    print(answer[i])



