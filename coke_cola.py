def solution(a, b, n): # 정답은 아님. 중간 계산 과정에 문제가 있음.
    results = []
    
    while True:
        if n >= a and a > b and b >= 1:
            # a병 만큼 가져다 줘서 b병 만큼 나오면 
            current_coke = (n // a) * b
            results.append(current_coke)
            
            n = current_coke
        else:
            results.append(n)
            print(sum(results))
            return sum(results)
            
# def solution(a, b, n): 가장 짧은 식(정답)
#     return max(n - b, 0)//(a-b) * b
            