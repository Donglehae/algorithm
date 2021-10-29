# [1차] 비밀지도

def solution(n, arr1, arr2):
  answer = []
  map_1 = []
  map_2 = []
  for val in arr1:
    buffer = []
    for v in bin(val)[2:]:
      buffer.append(int(v))
    if len(buffer) < n:
      for _ in range(n-len(buffer)):
        buffer.insert(0, 0)
    map_1.append(buffer)
  for val in arr2:
    buffer = []
    for v in bin(val)[2:]:
      buffer.append(int(v))
    if len(buffer) < n:
      for _ in range(n-len(buffer)):
        buffer.insert(0, 0)
    map_2.append(buffer)
  for idx in range(n):
    buffer = ''
    for i in range(n):
      if map_1[idx][i]+map_2[idx][i] > 0:
        buffer += '#'
      else:
        buffer += ' '
    answer.append(buffer)
  return answer

# 다른 풀이
# def solution(n, arr1, arr2):
#   answer = []
#   for v in zip(arr1,arr2):
#     result = str(bin(v[0]|v[1])[2:])
#     result = result.rjust(n, '0')
#     result = result.replace('1', '#')
#     result = result.replace('0', ' ')
#     answer.append(result)
#   return answer