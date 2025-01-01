# 문자열 -> list 화 시키면 하나하나 요소들 담겨진 리스트됨
# 거기서 pop 사용하면 뺴짐..

li = list(input())
zero, one = li.count('0')//2, li.count('1')//2
for _ in range(zero):
    li.pop(-li[::-1].index('0')-1)
for _ in range(one):
    li.pop(li.index('1'))
print(''.join(li))

# 0 1 2 3
# -1 -2 -3 -4
