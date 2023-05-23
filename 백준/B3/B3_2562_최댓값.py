list = []

for i in range(9):
    list.append(int(input()))

max = max(list)

index = list.index(max)

print(max)
print(index+1)