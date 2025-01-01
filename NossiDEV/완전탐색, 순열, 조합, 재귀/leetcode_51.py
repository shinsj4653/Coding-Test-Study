def solveNQueens(n) :

    answer = []
    def setMark(n, queens):
        mark = [[0 for _ in range(n)] for _ in range(n)]
        for y, x in queens :
            for i in range(n):
                for j in range(n):
                    if i == y or j == x:
                        mark[i][j] = 1

                    # 대각선 여부는 어떻게 체크?
                    if abs(i - y) == abs(j - x):
                        mark[i][j] = 1
        return mark

    def dfs(cur_row, mark, queens):
        if cur_row == n:
            if len(queens) == n:
            # 정답 배열에 추가
                board = []
                for y in range(n):
                    line = ""
                    for x in range(n):
                        if (y, x) in queens:
                            line += 'Q'
                        else:
                            line += '.'
                    board.append(line)
                answer.append(board)
            return

        for i in range(cur_row, n):
            for j in range(n):
                if mark[i][j] == 0 :
                    queens.append((i, j))
                    mark = setMark(n, queens)

                    dfs(cur_row + 1, mark, queens)

                    queens.pop()
                    mark = setMark(n, queens)
    if n == 1:
        return [["Q"]]

    if n == 2 or n == 3:
        return []

    answer = []

    for start_col in range(n):
        print('start_col : ', start_col)
        queens = []

        queens.append((0, start_col))
        mark = setMark(n, queens)
        #print('init mark : ', mark)

        dfs(1, mark, queens)

        #print('mark : ', mark)
        print('queens :', queens)
        print('---------------')

    return answer

print(solveNQueens(5))