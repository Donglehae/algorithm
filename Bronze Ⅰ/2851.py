# 슈퍼 마리오
score = []
for i in range(10):
    a = int(input())
    score.append(a)
result = 0
for s in score:
    result += s
    if result >= 100:
        if (result - 100) > (100 - (result - s)):
            print(result-s)
        else:
            print(result)
        break
if result < 100:
    print(result)