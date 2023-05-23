# https://www.acmicpc.net/problem/15552

#1st

"""a = sys.stdin.readline()
print(a) 

for문 안에 input()을 쓸 때 for문 반복 횟수가 많으면 시간초과가 날 수 있음
 -> 그런 경우 sys.stdin.readline()를 쓰면 시간초과가 나지 않음

sys.stdin.readline()를 쓰려면 import sys를 해야함
input("prompt message") : input()은 매개변수에 입력 시 띄울 안내문인 prompt message인 문자열 형식을 받음
sys.stdin.readline() 매개변수에는 한번에 읽을 수 있는 글자 수 크기로 정수 자료형을 받음"""

#2nd
'''
# testcase 수만큼 입력을 받을 거니까 테스트케이스는 for문에서 숫자로 쓰임
#->정수형으로 변환
T = int(input("테스트케이스의 개수 입력:"))
# A,B를 각각 받고 그 때 그 때 합을 출력시키는 것이 아니고
# A,B가 여러개고 한번에 여러개의 A,B를 입력받은 후 각각의 합을 출력시켜야함
#-> 리스트 이용
sum = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    #출력할 건 합이니까 반복문으로 a,b를 받아서 합만 리스트에 저장
    sum.append(A + B) 

for i in range(T):
    print(sum[i])
'''

# 12.23.금 다시 풀어보기

#1st
'''
import sys

t = int(input())

for i in range(t):
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)
'''
# 알게된 점!
# 무조건 입력을 다 하고 그 입력값을 저장 후, 출력을 안 해도 된다!
# 코드에 따라 입력 받자마자 출력하여 따로 저장 없이 코드를 짤 수도 있다.


# 5개월 가량 후 복습

# 1st
'''
t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(a+b)
'''
# testcase 다 입력 받은 후 출력하는 게 아니라 
# 하나 입력 받고 하나 출력해도
# 백준 "시간 초과" 뜸 

# 2nd
'''
import sys
input = sys.stdin.readline.rstrip # AttributeError: 'builtin_function_or_method' object has no attribute 'rstrip'
t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(a+b)
'''
# 3rd
'''
import sys
input = sys.stdin.readline.rstrip # AttributeError: 'builtin_function_or_method' object has no attribute 'rstrip'
t = int(input())

for i in range(t):
    a, b = map(int,input())
'''
# 4th
'''
import sys
input = sys.stdin.readline.rstrip() # AttributeError: 'builtin_function_or_method' object has no attribute 'rstrip'
t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(a+b)
'''
# 5th 
'''
import sys
input = sys.stdin.readline().rstrip
t = int(input())

for i in range(t):
    a, b = map(int,input.split()) # AttributeError: 'builtin_function_or_method' object has no attribute 'split'
    print(a+b)
'''
# 2nd,3rd,4th,5th 백준 런타임 에러(AttributeError)

# 6th
'''
import sys
input = sys.stdin.readline().rstrip # 109줄 (추후 수정시 줄 위치가 바뀔 수 있지만 109줄이라 말하겠음)
t = int(input())

print("input:",input(),"띄어쓰기")

for i in range(t):
    # print(sys.stdin.readline().rstrip()) # 113줄 #109줄 주석처리하고 114줄 주석처리하고 113줄 주석안하고 돌리면 젤 첨 t 3입력 받고 이후에 포문안에서 입력하는데로 출력 잘됨(정상 작동)
    # print(input())  # (113줄 주석 처리한 상태) 109줄을 주석 처리하고 기본 input()으로 t로 3을 입력받으면 포문에 114줄 인풋으로 넘어가서 1을 입력하면 1이 한번더 print됨(정상 작동)
                    # (113줄 주석 처리한 상태) 109줄을 주석 안하고 input에 다른 명령어를 대입해서 돌리면 t로 3을 입력받으면 다음 포문 인풋받기도 전에 333이 알아서 출력됨(작동 이상 발생)
                    # -> (113 주석 처리하고 109 주석 처리 안 한 상태 ) 젤 첨엔 t에서는 input이 입력을 받으면서 이후에 input()에서는 제대로 입력을 안 받고 t 대입문에서 받은 값이 input()에 들어가있는 거 같음
                    # t 대입문 아래 for문 위에 input()을 출력하면 t에 입력했던 3(int 형변환 되기 전의 문자형)이 출력됨
    a, b = map(int,input().split()) # ValueError: not enough values to unpack (expected 2, got 1)
                                    # (109줄 주석 안 하고 113줄 주석 한 상태) input()이 정상적으로 입력받아지지 않고 input()이 t에 입력했던 3이어서 3을 split 해도 3임 
                                    # 근데 코드는 a,b에 대입한다고 써있음 즉 a,b = 하려면 우측에도 값이 2개여야하는데 현재는 1개인 상태
                                    # -> 변수 2개에 대입한다 했으니 우변도 값이 2개여야하는데 정작 1나여서 해당 에러가 발생!
                                    # 언팩킹: 여러 개의 객체를 포함하고 있는 하나의 객체를 풀어준다.
    print(a+b)
'''
# 7th
'''
import sys
input = sys.stdin.readline().rstrip
t = int(input())

for i in range(t):
    a, b = map(int,input()) # ValueError: not enough values to unpack (expected 2, got 1)
    print(a+b)
'''
# 8th
'''
import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    print("input:",input().rstrip())
    a, b = map(int,input().rstrip()) # ValueError: invalid literal for int() with base 10: ' ' <=> 10진수 int()로 변환할 수 없는 문자열
                                     # 첫 입력인 t도 잘 받아지고 포문에서도 입력이 잘 받아짐
                                     # 근데 input().rstrip()는 rstrip만 해서 마즈막 개행문자만 사라지고 3 3으로 입력시 3,3으로 안 나뉘어지고 "3 3"임 그래서 int 함수 사용 불가
    print(a+b)
'''
# 6th, 7th, 8th 백준 런타임에러(ValueError)

# 9th
'''
import sys
input = sys.stdin.readline().rstrip()
t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(a+b)
'''
# 9th 백준 런타임 에러(TypeError)

# 10th
'''
import sys
input() = sys.stdin.readline().rstrip()
t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(a+b)
'''
# 11th
'''
import sys
input() = sys.stdin.readline.rstrip()
t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(a+b)
'''
# 10th,11th 백준 컴파일 에러