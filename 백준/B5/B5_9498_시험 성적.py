"""
- if,elif,esle
- 스위치문 (파이썬에 없음!)
"""

score = int(input("시험 점수 입력:"))

if(score >=90):
    print("A")
elif(score>=80):
    print("B")
elif(score>=70):
    print("C")
elif(score>=60):
    print("D")
else:
    print("F")

# if 뒤 (조건)의 ()는 생략 가능!