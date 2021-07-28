# 줄 세우기
a = int(input())
group = list(map(int, input().split()))
result = []
for num in range(a):
  result.insert(group[num], str(num+1))
result.reverse()
print(' '.join(result))