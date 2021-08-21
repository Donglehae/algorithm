# 비밀 이메일
msg = input()
div = 2
matrix = []
for i in range(1, len(msg)//2+1):
    if len(msg) % div == 0:
        if len(msg)//div <= div:
            matrix.append([len(msg)//div, div])
    div += 1
if len(matrix) > 0:
    idx = 0
    result = [[0 for i in range(max(matrix)[0])] for j in range(max(matrix)[1])]
    for row in range(max(matrix)[1]):
        for column in range(max(matrix)[0]):
            result[row][column] = msg[idx]
            idx += 1
    msg = ""
    for row in range(len(result[0])):
        for column in range(len(result)):
            msg += result[column][row]
    print(msg)
else:
    print(msg)