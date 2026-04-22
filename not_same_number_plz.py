def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        # 1. 첫 번째 원소는 무조건 넣음
        # 2. 그 다음부터는 '직전 원소(i-1)'와 다를 때만 넣음
        if i == 0 or arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer