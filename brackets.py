from collections import deque

def solution(s):
    def check(q):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in q:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack

    answer = 0
    # 문자열을 데크(deque) 객체로 변환
    q = deque(s)
    
    for _ in range(len(s)):
        if check(q):
            answer += 1
        # 덱 전체를 왼쪽으로 1칸 물리적 회전 (인덱스 계산 불필요)
        q.rotate(-1)
        
    return answer