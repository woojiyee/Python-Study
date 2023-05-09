# 1차 시도
#number1 = int(input(" 첫번쨰 자연수 입력 "))
#number2 = int(input(" 두 번쨰 자연수 입력 "))

# print(number1 + number2)
# print(number1 - number2)
# print(number1 * number2)
# print(number1 / number2)
# print(number1 % number2)

# * 위 코드에서의 잘못된 점 
# 1. 문제에서는 띄워쓰기를 기준으로 값을 구분하여 두 수를 한번에 다 받음 ex) 7 3
#    근데 input은 엔터를 기준으로 값을 받음
#    그래서 input 두 번으로 값 입력받으려면 입력값이 띄워쓰기(space)가 아니라 줄 바뀜(enter)로 되어 있어야함
#    ex) 7
#        3  이런 형태의 입력값일 때 input 두 번으로 값 받는 거임.
#    -> input 두번이 아니라 input 한번에 split으로 입력데이터에서 값 구분해서 받아야 함.
# 2. /는 실수 나누기임으로 원하는 자연수 형식의 몫이 아님

#2nd
'''number1,number2 = int(input("자연수 두개 입력").split())

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 // number2)
print(number1 % number2)

위 코드에서 잘못된 점
1. int(input("자연수 두개 입력").split())는 TypeError 발생
    -> input("자연수 두개 입력").split() 결과는 list
    그러나 input() 함수 안에는 list 형식 올 수 없음!'''

#3rd
'''number1, number2 = input(" 자연수 두개 입력").split()
number1 = int(number1)
number2 = int(number2)
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 // number2)
print(number1 % number2)'''



# 복습 풀기

a, b = map(int,input().split())

print(a+b)
print(a-b)
print(a*b)
# 1st print(a/b) # 백준 틀렸습니다.
print(a//b)
print(a%b)

# 백준 맞았습니다.
# 몫은 자연수 나누기s