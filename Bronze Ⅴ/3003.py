# 킹, 퀸, 룩, 비숍, 나이트, 폰
a = str(input())
input = a.split()
compare = [1, 1, 2, 2, 2, 8]
result = []
for idx, val in enumerate(input):
  result.append(str(compare[idx] - int(val)))
print(' '.join(result))