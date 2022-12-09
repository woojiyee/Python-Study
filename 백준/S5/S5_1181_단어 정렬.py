#1st
'''N = int(input())
word =[]
# box = ""

for i in range(N):
    word.append(input())
    
for i in range(N):    
    if len(word[i]) > len(word[i+1]):
        # word[i]의 길이가 word[i+1]의 길이보다 큰 경우
        # 순서 바꾸기
        box = word[i]
        word[i] = word[i+1]
        word[i+1] = box
    elif len(word[i]) == len(word[i+1]):
        # 길이가 같은 경우

    
for i in range(N):
    print(word(i))
#이렇게 하면 리스트에서 중복된 단어가 있어 중복 제거 됐을시,
#N과 단어 리스트의 갯수가 다름'''


#2nd
'''N = int(input("단어 개수 입력:"))
word =[]
extralist = []

for i in range(N):
    word.append(input("단어 입력:"))
    
#set 함수 이용: 중복 제거 -> 다시 리스트 형식으로 변환
word = list(set(word))
print("중복 제거 후 단어 리스트:",word)

setLen = len(word)

# 길이 함수를 기준으로 정렬
word.sort(key=len)
print("길이 정렬 후 단어 리스트:",word)

# 두 단어의 길이가 같을 떄
for i in range(setLen-1):
    if len(word[i]) == len(word[i+1]):
        extralist.append(word[i])
        extralist.append(word[i+1])
        print("길이가 같은 단어",word[i],word[i+1])
        # 사전순으로 정렬
        extralist.sort()
        print("extralist에 담고 정렬 후",word[i],word[i+1])        
        # 정렬된순으로 다시 대입
        word[i] = extralist[0]
        word[i+1] = extralist[1]
        print("길이가 같은 단어 사전순으로 대입 후",word[i],word[i+1])
        extralist =[0]

    
for i in word:
    print(i)'''

#3rd

'''
N = int(input("단어 개수 입력:"))
word =[]
extralist = []

for i in range(N):
    word.append(input("단어 입력:"))
    
#set 함수 이용: 중복 제거 -> 다시 리스트 형식으로 변환
word = list(set(word))
print("중복 제거 후 단어 리스트:",word)

setLen = len(word)

# 길이 함수를 기준으로 정렬
word.sort(key=len)
print("길이 정렬 후 단어 리스트:",word)

# 길이가 같은 단어들은 다 보조 리스트에 담고 사전순으로 정렬 후 원본 리스트에 대입
# 길이가 다른 단어가 나오기 직전까지 리스트에 담아야 하고 그 원본 함수의 index 몇부터 몇까진질 알아야함
while문 쓰려다 실패

    
for i in word:
    print(i)
'''       

 # 4th
 # (인터넷 찾아봄)

N = int(input("단어 개수 입력:"))
word =[]
extralist = []

for i in range(N):
    word.append(input("단어 입력:"))
    
#set 함수 이용: 중복 제거 -> 다시 리스트 형식으로 변환
word = list(set(word))
print("중복 제거 후 단어 리스트:",word)

# * 상위 조건 A와 하위 조건 B가 있으면
#   먼저 B로 정렬을 한 후에 A로 정렬을 해야 원하는 결과를 얻을 수 있음!
# 사전순 정렬
word.sort()

# 길이 함수를 기준으로 정렬
word.sort(key=len)
print("길이 정렬 후 단어 리스트:",word)

    
for i in word:
    print(i)