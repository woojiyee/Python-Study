## deque ##

from collections import deque

# deque에는 매게변수로 최대 2개만 넣을 수 있다
# -> 요소?로 여러개 넣고 싶으면 여러개의 값을 요소로 가지는 리스트 하나를 deque()의 ()에 넣어서 대입해주기!
'''queue1 = deque(1,2,3)
print("1,2,3을 넣은 deque",queue1)

queue3 = deque([1],[2],[3])
print("[1],[2],[3]을 넣은 deque",queue3)
-> TypeError: deque() takes at most 2 arguments (3 given)
'''

queue2 = deque([1,2,3])
print("[1,2,3]을 넣은 deque:",queue2) # deque([1, 2, 3])

# 큐.pop / popleft 를 하면 원본 큐에서 마즈막 요소/ 첫번째 요소가 삭제된다
# 변수 x= 큐.pop / popleft를 하면 원본 큐도 변경될 뿐 아니라 + 삭제되는 마즈막 요소/ 첫번째 요소가 x에 대입된다
# ( list의 pop도 그냥 pop만 할 시 원본 변경, pop을 변수에 대입하면 원본 변경 + 삭제되는 마즈막 요소가 변수에 대입됨.)
queue2.popleft()
print("popleft 이후 queue2:",queue2)

x = queue2.popleft()
print("x = queue2.popleft() 실행 이후 x:",x)
print("x = queue2.popleft() 실행 이후 queue2:",queue2)

## 리스트 ##
# 리스트.pop / popleft 를 하면 원본 리스트에서 마즈막 요소/ 첫번째 요소가 삭제된다
# 변수 x= 리스트.pop / popleft를 하면 원본 리스트도 변경될 뿐 아니라 + 삭제되는 마즈막 요소/ 첫번째 요소가 x에 대입된다
list = ['a','b','c']
list.pop()
print("list.pop() 후 list",list)
y = list.pop()
print("y = list.pop() 실행 이후 y:",y)
print("y= list.pop() 실행 이후 list:",list)
