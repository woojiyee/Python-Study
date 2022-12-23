'''king, queen, rook, bishop, knight, pawn = input("킹, 퀸, 룩, 비숍, 나이트, 폰 순서로 개수 입력").split()

king = int(king)
queen = int(queen)
bishop = int(bishop)
rook = int(rook)S
knight = int(knight)
pawn = int(pawn)


print(1-king," ",1-queen," ",2-rook," ",2-bishop," ",2-knight," ",8-pawn)'''

#2nd
'''
king, queen, rook, bishop, knight, pawn = map(int,input("킹, 퀸, 룩, 비숍, 나이트, 폰 순서로 개수 입력").split())

print(1-king,1-queen,2-rook,2-bishop,2-knight,8-pawn)
'''

# 12.22 다시 풀어봄
#1st

chess = list(map(int,input().split()))
print(chess)
original = [1,1,2,2,2,8]

for i in range(6):
    print(original[i]-chess[i],end = ' ')

# 입력값이 한 줄에 있음 -> 한번의 input으로 입력받을 수 있음 -> input을 for 안 돌려도 됨
# 입력값이 한 줄에 띄워쓰기로 데이터를 구분해서 받음 -> split()이용