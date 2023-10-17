# https://recordofwonseok.tistory.com/422

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    for _ in range(N - 1) :
        a, b = map(int, input().split())
        tree[b] = a

    A, B = map(int, input().split())
    parent_list = {}
    while A != 0 :
        parent_list.add(A)
        A = tree[A]

    while True :
        if B in parent_list :
            print(B)
            break
        B = tree[B]