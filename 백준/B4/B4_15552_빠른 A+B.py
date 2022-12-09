import sys

#1st

"""a = sys.stdin.readline()
print(a) 

for문 안에 input()을 쓸 때 for문 반복 횟수가 많으면 시간초과가 날 수 있음
 -> 그런 경우 sys.stdin.readline()를 쓰면 시간초과가 나지 않음

sys.stdin.readline()를 쓰려면 import sys를 해야함
input("prompt message") : input()은 매개변수에 입력 시 띄울 안내문인 prompt message인 문자열 형식을 받음
sys.stdin.readline() 매개변수에는 한번에 읽을 수 있는 글자 수 크기로 정수 자료형을 받음"""

#2nd

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
