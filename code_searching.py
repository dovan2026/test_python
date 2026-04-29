def find_code_coordinates(board, code):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    result = []

    for char in code:
        found = False
        # 위 -> 아래 (r), 왼쪽 -> 오른쪽 (c) 순으로 탐색
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == char:
                    result.append([r, c])
                    found = True
                    break # 가장 먼저 찾은 좌표를 선택하고 내부 루프 탈출
            if found:
                break # 다음 문자로 넘어감
        
        # 문자를 찾지 못한 경우 [-1, -1] 추가
        if not found:
            result.append([-1, -1])
            
    return result