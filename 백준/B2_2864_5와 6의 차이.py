# 문제 이해하기
'''
1. 5가 5일 수도 있고 6일 수도 있음,
   6이 5일 수도 6일 수도 있음
2. 두 수의 합 중 최소값과 최대값은?
=> 최소값은 입력 받은 수 중 5,6이 다 5인 경우
   최대값은 입력 받은 수 중 5,6이 다 6인 경우
'''

# 수도 코드
'''
1. 두 수를 입력받는다.
2. 최소 합은 두 수 중 6을 5로 바꾼 뒤 두 수 합하기
   최대 합은 두 수 중 5를 6으로 바꾼 뒤 두 수 합하기
3. 합의 최솟값, 최댓값 출력
'''

#1st

'''# 수 2개 입력받기
a, b = input(" 두 수 입력: ").split()

# 최소 합
min = 0
# 최대 합
max = 0

# a 중 6을 5로 바꾸기
for i in a:
    if i=="6":
        i = "5"
print("6->5로 바꾼 a",a)

# b 중 6을 5로 바꾸기
for i in b:
    if i=="6":
        i = "5"

print("6->5로 바꾼 b",b)

min = int(a)+int(b)

# a 중 5를 6으로 바꾸기
for i in a:
    if i=="5":
        i = "6"
print("5->6로 바꾼 a",a)

# b 중 5를 6으로 바꾸기
for i in b:
    if i=="6":
        i = "5"

print("5->6로 바꾼 b",b)

max = int(a)+int(b)

print("합 최솟값, 최댓값:",min,max)
'''

#2nd
'''
# 수 2개 입력받기
중간에 숫자만 편하게 바꾸기 위해 문자열로 받아서 바꾸기
a, b = input(" 두 수 입력: ").split()

# for문 돌릴용으로 문자용 길이
alen = len(a)
blen = len(b)
# 최소 합
min = 0
# 최대 합
max = 0

# a 중 6을 5로 바꾸기
for i in range(alen) :
    if a[i]=="6":
        a[i] = "5"
print("6->5로 바꾼 a",a)

# b 중 6을 5로 바꾸기
for i in range(blen):
    if b[i]=="6":
        b[i] = "5"

print("6->5로 바꾼 b",b)

min = int(a)+int(b)

a = str(a)
b = str(b)

# a 중 5를 6으로 바꾸기
for i in range(alen):
    if a[i]=="5":
        a[i] = "6"
print("5->6로 바꾼 a",a)

# b 중 5를 6으로 바꾸기
for i in range(blen):
    if b[i]== "5":
        b[i] = "6"

print("5->6로 바꾼 b",b)

max = int(a)+int(b)

print("합 최솟값, 최댓값:",min,max)

# 위 코드에서 잘 못된 점
1. 문자열이 인덱싱은 가능하나 문자열[]에 값 재할당은 불가능
-> replace()를 이용하거나 리스트 이용
'''



# 3rd


# 수 2개 입력받기
'''중간에 숫자만 편하게 바꾸기 위해 문자열로 받아서 바꾸기'''
a, b = input(" 두 수 입력: ").split()

# 최소 합
min = 0
# 최대 합
max = 0

# a 중 6을 5로 바꾸기
a = a.replace('6','5')
print("6->5로 바꾼 a",a)

# b 중 6을 5로 바꾸기
b = b.replace('6','5')

print("6->5로 바꾼 b",b)

min = int(a)+int(b)

a = str(a)
b = str(b)

# a 중 5를 6으로 바꾸기
a = a.replace('5','6')
print("5->6로 바꾼 a",a)

# b 중 5를 6으로 바꾸기

b= b.replace('5','6')

print("5->6로 바꾼 b",b)

max = int(a)+int(b)

print("합 최솟값, 최댓값:",min,max)