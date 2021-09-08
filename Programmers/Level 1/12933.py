# 정수 내림차순으로 배치하기

# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.

# 입력
# n	        return
# 118372	873211

def solution(n):
    answer = ''
    num = []
    for val in str(n):
        num.append(val)
    num.sort(reverse=True)
    for val in num:
        answer += val
    return int(answer)

# 다른 풀이
# def solution(n):
#     num = list(str(n))
#     num.sort(reverse=True)
#     return int(''.join(num))