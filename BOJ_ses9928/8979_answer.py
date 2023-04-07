N, K = map(int, input().split())
place = 1

l = []

for i in range(N) :
    c, gold, silver, bronze = map(int, input().split())
    l.append((c, gold, silver, bronze))

l.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(N) :
    if l[i][0] == K :
        index = i

for i in range(N) :
    if l[index][1:] == l[i][1:] :
        print(i + 1)
        break