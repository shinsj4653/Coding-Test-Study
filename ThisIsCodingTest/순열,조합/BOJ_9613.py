import math
from itertools import combinations

t = int(input())
for _ in range(t) :
    answer = 0
    gcd_sum_set = set()

    n, *arr = map(int, input().rstrip().split())

    for comb in combinations(arr, 2) :
        answer += math.gcd(*comb)

    print(answer)

