def solution(board, moves):
    # 각 열(Column)에서 0을 제외한 인형만 추출한 뒤, pop()하기 쉽게 역순 정렬
    cols = [list(filter(None, col))[::-1] for col in zip(*board)]
    stack = []
    result = 0

    for m in moves:
        col = cols[m - 1]
        if col:
            doll = col.pop()
            if stack and stack[-1] == doll:
                stack.pop()
                result += 2
            else:
                stack.append(doll)
                
    return result

#     def solution(board, moves):    
#         answer = []
#         stack = [[row[i] for row in board if row[i] != 0] for i in range(len(board[0]))]
#         result = 0
#         for l in moves:
#             index = l-1
#             if( stack[index] ):
#                 top = stack[index].pop(0)
#                 if answer and answer[-1] == top:
#                     answer.pop()
#                     result += 2
#                 else:
#                     answer.append(top)
#         answer = result

#         return answer