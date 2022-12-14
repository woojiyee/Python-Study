# 다시 스스로 풀어보기
# 수도코드
'''
- 다섯 단어 : 맨 앞에(첫번째) 문자 n1개-> 두번째 문자 n2개
   -> 한 단어의 길이가 몇개냐에 따라 세로로 읽을 시 5개 이하일 수 있음 ->최대 5개
1. 1차원 배열로 단어들을 입력받고 단어들은 다 문자열형이니 요소에 []로 문자 호출?
'''

#1st
'''
# 5개 단어 리스트
words = input("단어 5개 입력:").split()

#5개의 단어 중 가장 긴 단어의 길이
maxLength = 0

for i in words:
    if maxLength < len(i):
        maxLength = len(i)

for i in range(maxLength):
    for j in range(5):
        if i < len(words[i]):
            print(words[j][i],end='')

print("")

# 1st 잘못 된 코드
1. 단어 5개가 한 줄에 입력되는 것이 아닌 한 줄에 한 단어로 입력
   -> 근데 1st처럼 하게 되면 첫 줄 한단어만 입력받아짐
2. 두번째 for문 안에 if에 words[i]로 하게 되면 i는 열의 인덱스
   근데 확인하고자 하는건 한 단어씩의 길이기에 words 리스트의 행마다 길이가 필요함
   -> words[j]를 해야 words[0] ~ words[4]까지의 각 행의 단어마다의 길이를 구할 수 있음
'''

#2nd

words = list()

for _ in range(5):
    words.append(input("단어 5개 입력:"))

#5개의 단어 중 가장 긴 단어의 길이
maxLength = 0

for i in words:
    if maxLength < len(i):
        maxLength = len(i)

for i in range(maxLength):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i],end='')

print("")

        
