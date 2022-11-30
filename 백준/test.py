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

# 줄 바꿈(개행) : \n

#a = input("한자리 수 입력")
#print("a 자료형 :",type(a))s
# input으로 받은 데이터는 문자열 형식이다!

# input으로 받은 데이터 정수형으로 쓰고 싶으면 형변환해줘야 함
#b = int(input("한자리 수 입력"))

#print("split() 결과의 자료형 :",input("자연수 두개 입력").split())
#split() 결과는 list 형식

# map( 적용할 함수, 반복 가능한 자료형)
# : 한 줄의 코드로 모든 자료형 각각에 함수를 적용할 수 있음

# range(stop) , range(start,stop), range(start,stop,step)
# :원래 정수는 iterable하지 않으나 range 결과는 iterable하기 때문에 for문을 사용해 출력 가능
#  ,range의 매개변수는 정수! + 내장 함수라 별도의 import 필요 없음