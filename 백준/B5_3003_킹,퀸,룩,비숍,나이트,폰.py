'''king, queen, rook, bishop, knight, pawn = input("킹, 퀸, 룩, 비숍, 나이트, 폰 순서로 개수 입력").split()

king = int(king)
queen = int(queen)
bishop = int(bishop)
rook = int(rook)S
knight = int(knight)
pawn = int(pawn)


print(1-king," ",1-queen," ",2-rook," ",2-bishop," ",2-knight," ",8-pawn)'''


king, queen, rook, bishop, knight, pawn = map(int,input("킹, 퀸, 룩, 비숍, 나이트, 폰 순서로 개수 입력").split())

print(1-king,1-queen,2-rook,2-bishop,2-knight,8-pawn)
