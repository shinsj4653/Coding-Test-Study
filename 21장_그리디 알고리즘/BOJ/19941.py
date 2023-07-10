# https://dodomp0114.tistory.com/27
# find 함수: 리스트, 튜플, 딕셔너리에서 사용 불가능! 오직 문자열에서만..

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

line = input()
list_line = list(line.rstrip())
max_num = 0

if n == 1 :
    print(0)

else :
    for i in range(n) :
        if line[i] == 'P' :
            if i - k < 0 and not i + k > n - 1:
                start = 0
                end = i + k

            if not i - k < 0 and i + k > n - 1:
                start = i - k
                end = n - 1

            else :
                start = i - k
                end = i + k


            for j in range(start, end + 1) :
                if line[j] == 'H' :
                    line[j] = 'X'
                    max_num += 1
                    break

print(max_num)

