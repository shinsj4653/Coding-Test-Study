import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0
space = []
for i in range(n) :
    space.append(list(map(int, input().split())))


for i in range(1, n) :
    for j in range(m) :
        if i == 1 :
            if j == 0:
                s = space[i][j] + space[i - 1][j]
                l = space[i][j] + space[i - 1][j + 1]

                if s < l :
                    space[i][j] = (s, 's')
                else :
                    space[i][j] = (l, 'l')

            elif j == m - 1 :

                s = space[i][j] + space[i - 1][j]
                r = space[i][j] + space[i - 1][j - 1]

                if s < r:
                    space[i][j] = (s, 's')
                else:
                    space[i][j] = (r, 'r')
            else :
                s = space[i][j] + space[i - 1][j]
                l = space[i][j] + space[i - 1][j + 1]
                r = space[i][j] + space[i - 1][j - 1]

                if min(s, l, r) == s:
                    space[i][j] = (s, 's')
                elif min(s, l, r) == l:
                    space[i][j] = (l, 'l')
                else:
                    space[i][j] = (r, 'r')

        else :
            if j == 0:
                s = space[i][j] + space[i - 1][j][0]
                l = space[i][j] + space[i - 1][j + 1][0]

                if s < l :
                    if space[i - 1][j][1] != 's':
                        space[i][j] = (s, 's')
                    else :
                        space[i][j] = (l, 'l')

                elif s > l :
                    if space[i - 1][j + 1][1] != 'l':
                        space[i][j] = (l, 'l')

                    else :
                        space[i][j] = (s, 's')

            elif j == m - 1:

                s = space[i][j] + space[i - 1][j][0]
                r = space[i][j] + space[i - 1][j - 1][0]

                if s < r:
                    if space[i - 1][j][1] != 's' :
                        space[i][j] = (s, 's')
                    else :
                        space[i][j] = (r, 'r')


                else:
                    if space[i - 1][j - 1][1] != 'r':
                        space[i][j] = (r, 'r')
                    else:
                        space[i][j] = (s, 's')
            else:

                s = space[i][j] + space[i - 1][j][0]
                l = space[i][j] + space[i - 1][j + 1][0]
                r = space[i][j] + space[i - 1][j - 1][0]

                if min(s, l, r) == s :
                    if space[i - 1][j][1] != 's' :
                        space[i][j] = (s, 's')
                    else :
                        if space[i - 1][j + 1][1] != 'l' :
                            space[i][j] = (l, 'l')

                        else :
                            space[i][j] = (r, 'r')

                elif min(s, l, r) == l:
                    if space[i - 1][j + 1][1] != 'l':
                        space[i][j] = (l, 'l')
                    else:
                        if space[i - 1][j][1] != 's':
                            space[i][j] = (s, 's')
                        else:
                            space[i][j] = (r, 'r')

                else:
                    if space[i - 1][j - 1][1] != 'r':
                        space[i][j] = (r, 'r')
                    else:
                        if space[i - 1][j][1] != 's':
                            space[i][j] = (s, 's')
                        else:
                            space[i][j] = (l, 'l')

min_num = float('inf')

for num, way in space[n - 1] :
    if min_num > num :
        min_num = num

print(min_num)
