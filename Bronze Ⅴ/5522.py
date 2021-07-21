# 카드 게임
result = 0;
for cnt in range(5):
  a = int(input())
  if a >= 0 and a <= 100:
    result += a
print(result)