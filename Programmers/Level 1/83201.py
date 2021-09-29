# 위클리 챌린지 2주차_상호평가

def solution(scores):
  answer = ''
  length = len(scores)
  reverse = [[0]*length for _ in range(length)]
  for i in range(length):
    for j in range(length):
      reverse[j][i] = scores[i][j]
  for idx, val in enumerate(reverse):
    if val.count(val[idx]) == 1:
      if val[idx] == max(val) or val[idx] == min(val):
        del val[idx]
    average = sum(val)/len(val)
    if average >= 90:
      answer += 'A'
    elif average >= 80:
      answer += 'B'
    elif average >= 70:
      answer += 'C'
    elif average >= 50:
      answer += 'D'
    elif average < 50:
      answer += 'F'                  
  return answer

# 다른 풀이
# def solution(scores):
#   reverse = [ [i[j] for i in scores] for j in range(len(scores))]
#   answer = []
#   for idx, val in enumerate(reverse):
#     if val[idx] == max(val) or val[idx] == min(val):
#       if val.count(val[idx]) == 1:
#         del val[idx]
#     average = sum(val)/len(val)
#     answer.append(average)
#   return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in answer ])