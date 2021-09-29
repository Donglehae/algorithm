# 위클리 챌린지: 1주차_부족한 금액 계산하기

# def solution(price, money, count):
#   answer = 0
#   sum = 0
#   for i in range(count):
#     sum += price+(price*i)
#   if sum-money > 0:
#     answer = sum-money
#   return answer

# 다른 풀이
# def solution(price, money, count):
#   sum = count*(price+(price*count))/2
#   answer = int(sum-money)
#   return max(0, answer)