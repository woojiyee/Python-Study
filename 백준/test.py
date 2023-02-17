# 한 줄 주석

'''
여러 줄 주석 : 블록 설정 후 한/영키 + ' 3번
'''


"""
여러 줄 주석
"""

# print()
# - 자동 개행 (기본값으로 end = "\n")
# - 마즈막 출력 문자 바꾸고 싶으면 end 매개변수 이용
#   ex) print 한 번하고 띄워쓰기만 하고 또 print를 원하면 print("출려할 내용", end = ' ')

# input

""" for문 안에 input()을 쓸 때 for문 반복 횟수가 많으면 시간초과가 날 수 있음
 -> 그런 경우 sys.stdin.readline()를 쓰면 시간초과가 나지 않음

sys.stdin.readline()를 쓰려면 import sys를 해야함
input("prompt message") : input()은 매개변수에 입력 시 띄울 안내문인 prompt message인 문자열 형식을 받음
sys.stdin.readline() 매개변수에는 한번에 읽을 수 있는 글자 수 크기로 정수 자료형을 받음"""

"""시스와 인풋 차이점"""

# 줄 바꿈(개행) : \n

#a = input("한자리 수 입력")
#print("a 자료형 :",type(a))s
# input으로 받은 데이터는 문자열 형식이다!

# input으로 받은 데이터 정수형으로 쓰고 싶으면 형변환해줘야 함
#b = int(input("한자리 수 입력"))

# print("split() 결과의 자료형 :",input("자연수 두개 입력").split())
# split() 결과는 list 형식
# print("split() 결과의 자료형 :",type(input("자연수 두개 입력").split()))
# split() 결과는 list 형식
'''list = [2,3]
a = int(list)
print("a:",a)'''

# 형변환 int() 함수
'''
b = 3.3
bb = int(b)
print(bb) # 3

c = "1"
cc = int(c)
print(cc) # 1

d = "2.3"
dd = int(d)
print(dd) # ValueError: invalid literal for int() with base 10: '2.3'

e = "3.4"
ee = float(e)
print(ee) # 3.4

# int() 매개변수 : int를 한 번만 거쳐서 정수로 변환 가능한 데이터( 숫자나 문자열 )
'''

# map( 적용할 함수, 반복 가능한 자료형)
# : 한 줄의 코드로 모든 자료형 각각에 함수를 적용할 수 있음

# range(stop) , range(start,stop), range(start,stop,step)
# : stop은 치지 않음 stop전까지 반환?함
# :원래 정수는 iterable하지 않으나 range 결과는 iterable하기 때문에 for문을 사용해 출력 가능
#  ,range의 매개변수는 정수! + 내장 함수라 별도의 import 필요 없음
'''
print(range(3)) # range(0,3)
print(type(range(3))) # <class 'range'>
for i in range(3):
    print(i,type(i)) # 0 <class 'int'>
                     # 1 <class 'int'>
                     # 2 <class 'int'>
             
for i in range(4,0,-1):
    print(i,end=' ') # 4 3 2 1 

for i in range(4,-1,-1):
    print(i,end=' ') # 4 3 2 1 0  

array = [[1,2,3,4]]
for i in range(len(array)):
    print(i) #0
    print(array[i][-1]) #4
'''
'''array = [[2]]
array.append(array[0]+[3])
print(array)'''
#tuple 튜플 () 
# 인덱싱 가능
# 리스트와 유사 (부분 수정 안 되는 것만 다른 듯)
# 부분 수정 불가능, 전체 대체 가능
# -> 관계가 중요한 느낌 에를 들어 커플 = (뿌까, 가루) 를 (뿌까, 뚱이)로 바꿀 순 없지만 (스펀지밥, 뚱이)로는 변경/덮어쓰기 가능
# 함수 return에 값 두개 적으면 함수 호출 시, 값 두개가 튜플 형식으로 넘어감
"""a = (1,2)
a[1] = 4
print(a) -> 에러
a=(5,4)
print(a)"""

##2차원 리스트
# list[행][열] = list[y][x]
'''
a = [[1,2,3],[4,5,6],[7,8,9]]

print("a[1][2] ",a[1][2]) # a[1][2]  6
print("a[2][1] ",a[2][1]) # a[2][1]  8
# 2차원에서 하나의 [] 인덱스로는 2차원 배열의 원소인 행만 추출 가능
# 열을 추출하려면 for문이나 다른 코드?가 필요

print("a[1]",a[1]) # a[1] [4, 5, 6]
print("a[:][1]:",a[:][1]) # a[:][1]: [4, 5, 6]
print("a[1][:] ", a[1][:]) # a[1][:]  [4, 5, 6]
'''
## 2차원 리스트 초기화 시 주의

'''
test0 = [0] * 3
print(test0) # [0, 0, 0]
test0 = [[0] * 3 for _ in range(5)]
print(test0) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

test1 = [[0] * 3] * 5
test1[0][0] = 1
test1[0][1] = 1
test1[0][2] = 1
print('test1', test1) # test1 [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

0행만 초기화했지만 리스트 * n을 했을 시 다른 행이 0행을 참조하기에
0행에 참조한 값이 다른행에도 할당됨.

test1 = [[0] * 3] * 3
test1[0][0] = 1 
print('test1', test1) # test1 [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

test1 = [[0] * 3] * 5
test1[0][0] = 1
test1[1][1] = 3
test1[2][2] = 5
print('test1[1][1] 수정 전', test1) # test1 [[1, 3, 5], [1, 3, 5], [1, 3, 5], [1, 3, 5], [1, 3, 5]]
test1[1][1] = 7
print('test1[1][1] 수정 후', test1) # test1 [[1, 7, 5], [1, 7, 5], [1, 7, 5], [1, 7, 5], [1, 7, 5]]

# = 결론(? 아마...) =>
같은 *(곱셈)이라도 
변수 [0]에 * n -> 리스트가 됨
리스트 [0] * n 에 * m = 리스트 * m -> 모든 행이 하나의 리스트를 참조함. 어떤 행을 수정해도, 다른 모든 행이 같이 수정됨(같은 값을 가짐) 

test = [0]*3
print(test)
test[1] =2
print(test)
'''
'''
test = [0]*3
a = [1,2,3]
test[1] = a
print(test)'''
# 빈 리스트 변수에 =을 이용해 값을 대입/할당하면 
# 빈 리스트 첫 요소로 값이 들어가는 게 아니라 덮어쓰기 되서
# 변수는 리스트가 아닌 요소의 자료형이 됨.
'''a = []
print(type(a)) # list
a = 3
print(type(a)) # int
a[0] = 3
print(type(a)) #IndexError: ist assignment index out of range'''
# -> 빈 리스트에 값을 추가하고 싶다면 append,insert,extend 함수를
#    이용해서 추가하기
# 리스트 요소 변경은 인덱싱을 활용해 =으로 변경 가능
# 이미 리스트에 값이 있는 인덱스의 요소를 바꿀 때
'''b = [1,3,5,7]
b[2]=6
print(b) #[1, 3, 6, 7]'''

# 문자열
'''
a = '3'
b = a*3
c= '2'
b += c
print("b",b)
한 문자 반복 : *
문자열 이어 붙이기 : +
'''
'''
s = 'string'
for i in s:
    print("문자열 s의 문자:",i)
'''

'''array = list(list())
array.append(['w'])
array.append(['y'])
print(array)
array[0].append('x')'''
'''
list = [1,2,3]
list2 = [456]
print("list, list2:", list, list2)
list3 = list+list2
print('list3:', list3)

list3 = [1,2,3]
list4 = [456]
list3.append(list4)
print("list3 (append):",list3)

list5 = [1,2,3]
list6 = [456]
list5.extend(list6)
print("list4 (extend):",list5)
'''
'''
array = [2,'def']
r = [1]
s = ['abc']
ss = ['abc']
sss = ['abc']

a = s + array[1]
print("+ 이용:",a)
'''
'''
ss.append(array[1])
print("append 이용:",ss)

sss.extend(array[0])
print("extend 이용:",sss)
'''
# a,b가 리스트일 때
# a.extend(내용1) -> 내용1이 리스트든 문자열이든 리스트로 인식하고 내용1을 찢어서 a에 요소로 추가해줄게!
#                   내용1이 문자열일 때 extend는 문자열을 리스트라고 주는 거지? 오키 문자열 찢어서 문자를 a의 요소로 넣어줄게 ( 가능 )
# a + b -> +는 문자열 + 문자열이거나 리스트 + 리스트여야 함! 리스트 + 문자열하면 에러 뜸 ( 불가능 )
'''
list = [1,2]
list.extend(['abc','def'])
print(list)
# [1,2,3]
list.extend([4,5])
print(list)
# [1,2,3,4,5]
'''
#12.9.금
# 이중 배열 count
'''
ar = [1,2,2,3,4,5,2,1,3]
arr = [[3,2,5],[1,2,0],[3,3,1]]

print(ar.count(2))
print(arr.count(2))
print(arr[0].count(2))
print(arr[0])'''
# print(arr[0][])
# count(매개변수) : 1차원 리스트에서만 매개변수가 리스트에 몇개 있는지 갯수를 세줌
# 주의!) 2차원 리스트.count(매개변수) 시 원하는 결과를 얻을 수 없음

# 논리 연산자
'''
다른 언어에서 && -> 파이썬에선 and
'''

# 요소가 문자열인 1차원 리스트
'''a = ['123','abc','DEF']
print("a[0]:",a[0])
print("a[1]:",a[1])
print("a[2]:",a[2])
print("a[1][1]:",a[1][1])'''
# 파이썬에선 일반적으로 문자열도 배열로 인식하기에
# 이차원 배열이 아님에도 리스트의 요소가 문자열이면
# 리스트 요소인 문자열의 문자는 리스트의 이차원 배열 list[][]로 호출 가능

'''b = [123,'abc','DEF']
print("b[0]:",b[0])
print("b[1]:",b[1])
print("b[2]:",b[2])
print("b[1][1]:",b[0][1])
    # TypeError: 'int' object is not subscriptable
print("b[1][1]:",b[2][1])'''
# 하나의 리스트에 문자열과 다른 자료형이 섞여있을 시,
# 문자열인 요소만 이차원 배열 list[][]을 통해 
# 문자열을 이루는 문자 호출 가능
# 참고) 리스트 요소 중 숫자형 요소를 이차원 배열로 호출하면 에러 뜸

# list() 함수
'''
for i in range(5):
    li = list(input("단어 입력:")) 
        #1 단어 입력:sbs
        #2 단어 입력:123
    print("li:",li) 
        #1 li: ['s', 'b', 's']
        #2 li: ['1', '2', '3']
'''
'''li = (input("단어 입력:").split()) # 단어 입력:sbs
print("li:",li) # li: ['sbs']'''

# 이차원 리스트 append
# 이차원 리스트라도 리스트[] 하면 알아서 행 인덱스의 리스트로 연산 됨.
'''
list = [[1,2],[1,3],[2,3]]
list[1].append(2)
print(list) # [[1,2],[1,3,2],[2,3]]
print(list[1][-1]) # 2
'''
'''
# 3차원 리스트
list = [[[0]*2 for _ in range(3)] for _ in range(5)]
print(list)
list[0][0][0] = 1
list[1][0][1] = 2
print("변경 후:" ,list)
for j in range(3):
    print(j)
'''

# n차원 리스트
'''
list = [[]*2]
print("[[]*2] : ", list) # [[]*2] :  [[]]
list2 = []* 5
print("list2 = []* 5",list2) # list2 = []* 5 []
for i in range(2):
    print(i,"번째 ") # 0 번째
                    # 1 번째
    list[i] = [] * 3
    print("list[i] = [] * 3 :",list) # list[i] = [] * 3 : [[]]
                                     # IndexError: list assignment index out of range
'''
# list2 = [] for _ in range(2) # SyntaxError: invalid syntax + 애초에 코드 for에 빨간 밑줄 뜸
'''
list = [[] for _ in range(2)]
print("[[]*2] : ", list)
for i in range(2):
    list[i] = [[] for _ in range(3)]
    print(i,"i번째 ","list[i] = [] * 3 :",list)
'''
# 원하는 개수로 빈 리스트 만들 땐 2차원([[],[],..]) 이상일 때만!
# 1차원에서는 [] * n해도 걍 []로 만들어지고 [] for _ in range(n)하면 에러 뜸
# => n차원의 빈 리스트를 원하는 갯수로 만들 때 그냥 * 쓰면 원하는데로 안 먹히고
#    for 쓰면 바깥 리스트 안에 리스트 갯수를 빈 리스트 상태로 만들 수 있음!
# => 리스트에 * 쓰는 건 빈 리스트에다 쓰는 게 아님 (위 설명 보면 1차원이든 2차원 이상이든 * 써서는 원하는대로 안 됨)
#    * 빈 리스트가 아니라 1차원 리스트 요소를 초기화 할 때 쓰는 거! (상단 필기 중 '초기화' 참고하기)

# in 함수? 리스트에 특정 요소가 있는지 찾는 함수
'''
list = [1,2,3,4,5]

if 1 in list:
    print("1. list1에 1 있음")
else:
    print("2. list1에 1 없음")

if 6 in list:
    print("3.list1에 6 있음")
else:
    print("4.list1에 6 없음")

list2 = [[0,0,0],[1,2,3]]

if 0 in list2:
    print("5.리스트2에 0 있음")
else:
    print("6.리스트2에 0 없음")

if 8 in list2:
    print("7.리스트2에 8 있음")
else:
    print("8.리스트2에 8 없음") # 이게 출력됨

for i in range(2):
    print(list2[i])
    if 0 in list2[i]:
        print("9.리스트2에 0 있음") # 이렇게해야 0 있다고 출력
'''
#요소 in  리스트 으로 1차원 리스트에 요소 하나는 원하는데로 작동하지만
# 요소 in 2차원 리스트에서는 원하는데로 작동 안 함.이차원의 큰 리스트의 요소는 리스트라서 그런가봄
# => 리스트에 요소 유무 확인 하는 in을 쓸 때는 요소 in 1차원 리스트 구조로 해줘야함!

'''
print("list1의 최대 요소:",max(list)) # 5 # 원하는 대로 최대 요소 1개 나옴
print("list2의 최대 요소:",max(list2)) # [1,2,3] # 원하는 거와는 달리 리스트형식이 나옴

check1 = [] * 3
print("check1:",check1) # [] # 걍 빈배열 나옴 # * 숫자했다고 숫자만큼의 요소를 가지는 리스트로 생성 안 됨

check2 = [False] * 3
print("check2:",check2) # [False, False, False] # 값이 있는 배열에다 * n을 해야 그게 n개의 요소가 있는 리스트로 생성 됨
'''
'''
n,m = map(int,input("n,m 입력:"))
print(n) # 1
print("m:",m) # 2
'''
'''
a,b = 3,5
c=7;d=9
print(a,b,c,d)
'''
# 딕셔너리
'''
d = {"과일":["사과,바나나"],"갯수":3}
print(d["갯수"])
print(d.get("갯수"))
print(d.get("동물"))
print(d["동물"])
'''
'''
list = [(3,1,5),(2,7,3),(6,5,11)]
print(list)
# 리스트의 원소는 튜플 (3,1,5)와 (2,7,3)과 (6,5,11)
# 튜플의 원소
# 튜플 (3,1,5)의 원소: 3과 1과 5
list.sort()
print(list)'''

'''answer = [[0 for _ in range(3)]  for i in range(4)]
print(answer)'''


