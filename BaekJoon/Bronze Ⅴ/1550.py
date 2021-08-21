# 16진수
# print(int(input(), 16))
a = input().strip()
hexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
result = 0
reverse = a[::-1]
for i in range(0, len(a)):
  result += hexadecimal.index(reverse[i]) * (16 ** i)
print(result)