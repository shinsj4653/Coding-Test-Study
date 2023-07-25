import sys

while True:

    # 정렬 -> Invalid 빠르게 파악하기 위해
    t = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    if t[0] == 0 and t[1] == 0 and t[2] == 0 :
        break

    if t[0] == t[1] == t[2] :
        print("Equilateral")

    elif t[0] >= t[1] + t[2] :
        print("Invalid")

    elif t[0] == t[1] or t[1] == t[2] :
        print("Isosceles")

    else :
        print("Scalene")


