def solution(ingredient):
    answer = 0
    stack_list = []
    hamburger = [1, 2, 3, 1]
    
    for v in ingredient:
        stack_list.append(v)
        
        # 스택의 맨 위(가장 최근에 추가된 4개의 재료)를 확인
        if stack_list[-4:] == hamburger:
            answer += 1
            # 햄버거가 완성되었다면 해당 재료 4개를 스택에서 제거
            del stack_list[-4:]
            
    return answer