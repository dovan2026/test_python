def solution(schedules, timelogs, startday):
    answer = 0
    sl = schedules
    tl = timelogs
    
    for i in range(0, len(sl)):
        result = 0
        # 출근 인정 시간 계산 (55분 + 10분 = 65분이 아닌 05분이 되어야 함)
        limit_m = (sl[i] % 100) + 10
        limit_h = (sl[i] // 100) + (limit_m // 60)
        limit_m %= 60
        limit_time = limit_h * 100 + limit_m
        
        for j in range(0, 7):
            # [핵심] 현재 요일 계산 (startday가 시작일)
            # 1:월, 2:화, 3:수, 4:목, 5:금, 6:토, 7:일
            day = (startday + j - 1) % 7 + 1
            
            # 주말(토, 일)이면 출근 여부를 따지지 않고 무조건 성공으로 처리
            if day >= 6:
                result += 1
                continue
                
            # 평일일 때만 지각 여부 체크
            if limit_time >= tl[i][j]:
                result += 1
            else:
                break
                
        if result == 7:
            answer += 1
            
    return answer

# 틀린 답안
# def solution(schedules, timelogs, startday):
#     answer = 0
#     sl = schedules
#     tl = timelogs
#     sd = startday
    
    
#     for i in range(0, len(sl)):
#         result = 0
#         for j in range(0, 7):
#             if sl[i] + 10 >= tl[i][j]:
#                 result += 1
#             else:
#                 break
#         if result == 7:
#             answer += 1
#         else:
#             continue 
    
    
         
#     return answer