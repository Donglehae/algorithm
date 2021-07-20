# 검증수
a = str(input())
sum = 0;
for cnt in range(0, len(a.split())):
    sum += int(a.split()[cnt])**2
print(sum%10)