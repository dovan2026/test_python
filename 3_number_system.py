import numpy as np

def solution(n):
    # 1. 10진법 -> 3진법 (이 과정은 루프가 필수)
    # 나머지를 구하는 순간 이미 '뒤집힌' 상태로 수집.
    digits = []
    while n > 0:
        digits.append(n % 3)
        n //= 3
    
    # 2. 배열 관점에서의 접근 (Numpy 활용)
    arr = np.array(digits) # 뒤집힌 3진법 숫자들을 배열로 변환
    
    # 3. 10진법 전환 (가중치 배열 생성 후 곱셈)
    # 각 자릿수에 맞는 3의 거듭제곱(3^k, ..., 3^0) 가중치를 만듭니다.
    powers = 3 ** np.arange(len(arr))[::-1]
    
    # 두 배열을 곱해서 다 더함 (내적 연산)
    answer = np.sum(arr * powers)
    
    return int(answer)

# 다른 답안

# def solution(n):
#     answer = []
#     while True:
#         if n < 3:
#             answer.append(n)
#             break
#         answer.append(n % 3)
#         n = n // 3
#     answer.reverse()
#     sum = 0
#     for i in range(len(answer)):
#         sum += (answer[i] * (3 ** i))
#     return sum