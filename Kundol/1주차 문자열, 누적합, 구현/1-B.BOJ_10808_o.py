# ds: hash table
# algo: iteration
# o(n) -> 사전에 없다면 새로 추가, 있다면 += 1

# https://dongdongfather.tistory.com/69

from collections import defaultdict

s = input()
d = defaultdict(int)

for i in range(97, 123) :
    d[chr(i)] = 0

for ss in s :
    d[ss] += 1

for i in range(97, 123) :
    print(d[chr(i)], end=" ")

