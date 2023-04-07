# 삽입 정렬?
# 총 몇번 뒤로 물러서게
import sys
import collections

P = int(input())
for index in range(1, P + 1) :
    cnt = 0

    stu = list(map(int, sys.stdin.readline().split()))
    stu = stu[1:]

    for i in range(1, 20) :
        for j in range(0, i) :
            if stu[j] > stu[i] :
                tmp = stu[i]
                stu.remove(stu[i])
                stu.insert(j, tmp)
                cnt += (i - j)
                break

    print(index, cnt)
