# 좀 야매(?) 로 푼 것 같아서 풀이영상 보면서 제대로 풀어보고자 한다!
# 재귀를 제대로 이해하자
# 어떤 로직이 반복되고, 매개변수가 달라진다면? -> 재귀

n = int(input())
g = [list(map(int, list(input()))) for _ in range(n)]

def quard(y, x, size) :
    if size == 1 :
        return str(g[y][x])

    b = g[y][x]
    ret = ''

    for i in range(y, y + size) :
        for j in range(x, x + size) :
            if b != g[i][j] :
                ret += '('
                ret += quard(y, x, size // 2)
                ret += quard(y, x + size // 2, size // 2)
                ret += quard(y + size // 2, x, size // 2)
                ret += quard(y + size // 2, x + size // 2, size // 2)
                ret += ')'
                return ret

    return str(g[y][x])

print(quard(0, 0, n))