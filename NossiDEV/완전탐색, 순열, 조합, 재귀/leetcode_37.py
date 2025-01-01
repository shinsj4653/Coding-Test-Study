
def check_empty(board, r, c):
    if board[r][c] != ".":
        return False
    return True

def check_valid(board, num, r, c):
    for i in range(9):
        # 행 확인
        if board[r][i] == num:
            return False
        # 열 확인
        if board[i][c] == num:
            return False
        # 3x3 sub-box 확인
        if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == num:
            return False
    return True

def backtracking(board, index):
    # ✅ 모든 칸에 올바르게 숫자를 부여했다면 True/true를 반환한다.
    if index == 81:
        return True
    i, j = index // 9, index % 9
    # ✅ 현재 위치(i, j)가 비어있는지 검사한다.
    if check_empty(board, i, j):
        # ✅ 현재 위치에 1 ~ 9 사이의 정수를 부여해본다.
        for num in map(str, range(1, 10)):
            # ✅ 현재 위치에 선택한 정수의 유효성을 검사한다.
            if check_valid(board, num, i, j):
                # ✅ board[i][j]에 유효한 정수를 부여한다.
                board[i][j] = num
                # ✅ 백트래킹을 수행한다. (재귀 함수 호출)
                if backtracking(board, index + 1):
                    return True
                # ✅ False가 반환되면, board[i][j]를 빈 칸으로 되돌린다.
                board[i][j] = "."
        return False
    # ✅ 현재 위치(i, j)가 비어있지 않다면, 다음 위치로 넘어간다. (재귀 함수 호출)
    else:
        return backtracking(board, index + 1)

backtracking([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], 0)