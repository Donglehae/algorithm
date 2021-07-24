# 일곱 난쟁이
group = []
for _ in range(9):
    a = int(input())
    group.append(a)
groupSum = sum(group)
stop = False
index = []
while True:
    for a in range(0, len(group)-1):
        for b in range(a+1, len(group)):
            if groupSum - group[a] - group[b] == 100:
                index.append(group[a])
                index.append(group[b])
                stop = True
                break
        if stop:
            break
    if stop:
        break
group.remove(index[0])
group.remove(index[1])
group.sort()   
for val in group:
    print(val)