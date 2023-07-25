# 삽입 정렬?
# 총 몇번 뒤로 물러서게

# remove()
# https://ooyoung.tistory.com/49
# array 안에서 삭제하고자 하는 값이 여러 개가 있다 하더라도 "첫 번째 값에 대해서만 삭제"한다.

# insert()
# https://ooyoung.tistory.com/117
# arr.insert(i, x) -> 원하는 위치 i에 원하는 요소 x를 삽입하는 형태.

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
