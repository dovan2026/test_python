def solution(s):
    answer = []
    
    # s가 이미 문자열이므로 len(s)만으로 충분.
    for n in range(len(s)):
        # 현재 인덱스 n 이전까지의 문자열에서 s[n]을 뒤에서부터 찾음
        prev_index = s[:n].rfind(s[n])
        
        if prev_index == -1:
            # 앞에 똑같은 문자가 없는 경우
            answer.append(-1)
        else:
            # 앞에 똑같은 문자가 있는 경우 (거리 계산)
            answer.append(n - prev_index)
            
    return answer # 최종 결과 반환

# 다른 방법
# def solution(s):
#     answer = []
#     last = {}

#     for i, ch in enumerate(s):
#         if ch in last:
#             answer.append(i - last[ch])
#         else:
#             answer.append(-1)
#         last[ch] = i

#     return answer

# 모범 답안(배운 것들 바탕)
# def solution(s):
#     answer = []
#     dic = dict()
#     for i in range(len(s)):
#         if s[i] not in dic:
#             answer.append(-1)
#         else:
#             answer.append(i - dic[s[i]])
#         dic[s[i]] = i

#     return answer