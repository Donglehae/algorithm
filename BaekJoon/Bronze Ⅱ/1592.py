# 영식이와 친구들
a, b, c = map(int, input().split())
group = [0 for _ in range(a)]
group[0] += 1
index = 0
result = 0
while True:
    if group[index] % 2 == 0:
        group[(index-c)%a] += 1
        index = (index-c)%a
    else:
        group[(index+c)%a] += 1
        index = (index+c)%a
    result += 1
    if group[index] == b:
        print(result)
        break