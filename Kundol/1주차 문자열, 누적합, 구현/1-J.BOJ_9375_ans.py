from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
clo_dict = defaultdict(str)

for i in range(t) :

    ans = 1

    n = int(input())
    if n == 0 :
        print(0)
        continue

    for j in range(n) :
        clo, style = input().split()
        if style in clo_dict :
            clo_dict[style] += 1
        else :
            clo_dict[style] = 1

    for key in clo_dict :
        clo_dict[key] += 1

    for c in clo_dict.values() :
        ans *= c

    print(ans - 1)
    clo_dict = defaultdict(str)
    ans = 0