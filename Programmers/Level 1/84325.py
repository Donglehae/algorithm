# 위클리 챌린지 4주차_직업군 추천하기

def solution(table, languages, preference):
  answer = ''
  table_dict = {}
  for value in table:
    job = value.split(' ')
    table_dict[job[0]] = job[1:]
  for index, value in table_dict.items():
    buffer = []
    for idx, val in enumerate(languages):
      if val in value:
        buffer.append(preference[idx]*(5-value.index(val)))
    table_dict[index] = sum(buffer)
  table_dict = dict(sorted(table_dict.items()))
  answer = max(table_dict, key=table_dict.get)
  return answer