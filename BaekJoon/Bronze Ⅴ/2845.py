# 파티가 끝나고 난 뒤
a, b = map(int, input().split())
news = str(input())
result = []
for val in news.split():
    result.append(str(int(val)-(a*b)))
print(' '.join(result))