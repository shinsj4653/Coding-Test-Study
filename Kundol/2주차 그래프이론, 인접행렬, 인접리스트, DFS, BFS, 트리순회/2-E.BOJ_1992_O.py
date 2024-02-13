# 왼위, 오위, 왼아래, 오아래
# 재귀

n = int(input())
g = [list(map(int, list(input()))) for _ in range(n)]

ret = ''

def dfs(y, x, n):

    global ret

    if n == 1 :
        return

    num = g[y][x]
    diff = False

    for i in range(y, y + n) :
        for j in range(x, x + n) :
            if num != g[i][j] :
                diff = True
                break

    if not diff :
        ret += str(num)
        return

    elif n == 2 :
        ret += '('
        for i in range(y, y + n):
            for j in range(x, x + n):
                ret += str(g[i][j])

        ret += ')'
        return

    ret += '('
    dfs(y, x, n // 2)
    dfs(y, x + n // 2, n // 2)
    dfs(y + n // 2, x, n // 2)
    dfs(y + n // 2, x + n // 2, n // 2)
    ret += ')'

if n == 1 :
    print(g[0][0])
else :
    dfs(0, 0, n)
    print(ret)