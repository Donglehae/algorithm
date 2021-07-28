# 블랙잭
from itertools import combinations
n, m = map(int, input().split())
group = list(map(int, input().split()))
regroup = list(combinations(group, 3))
result = 0
for g in regroup:
  if sum(g) <= m:
    if sum(g) > result:
      result = sum(g)
print(result)