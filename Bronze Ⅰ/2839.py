# 설탕배달
weight = int(input())
result = []
for a in range(weight//5+1):  
  for b in range(weight//3+1):
    if(5*a + 3*b == weight):
      result.append(a+b)
if len(result) > 0:
  print(min(result))
else:
  print(-1)