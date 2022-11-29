# 1차 시도
# # number1 = int(input(" 첫번쨰 자연수 입력 "))
# number2 = int(input(" 두 번쨰 자연수 입력 "))

# print(number1 + number2)
# print(number1 - number2)
# print(number1 * number2)
# print(number1 / number2)
# print(number1 % number2)

# * 위 코드에서의 잘못된 점 
# 1. 문제에서는 한 번에 두 수를 다 받음
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
number1, number2 = input(" 자연수 두개 입력").split()
number1 = int(number1)
number2 = int(number2)

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 // number2)
print(number1 % number2)