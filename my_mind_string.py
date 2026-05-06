
def solution(strings, n):
    # 1. [s[n] + s] 형태로 변형: n번째 문자가 맨 앞으로 오도록 만듦
    # 예: "sun", n=1 -> "usun"
    prepared = [s[n] + s for s in strings]
    
    # 2. 정렬
    prepared.sort()
    
    # 3. [s[1:]] 슬라이싱으로 원래 문자열 복구: 맨 앞의 임시 문자 제거
    return [s[1:] for s in prepared]

# 튜플
#  def solution(strings, n):
#      keys = [(x[n], x) for x in strings]
#      sorted_key = sorted(keys)
#      result = [i[1] for i in sorted_key]
#      return result

# Gemini 답안
# def solution(strings, n):
    # 정렬 기준을 튜플 형태로 반환하여 다중 조건 정렬 수행
    # 1. x[n]: n번째 문자 (1차 기준)
    # 2. x: 문자열 전체 (2차 기준)
    # return sorted(strings, key=lambda x: (x[n], x))