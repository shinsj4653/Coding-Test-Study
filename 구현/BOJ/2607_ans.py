# 그 용어 뭐였더라..똑같은 문자들로 다른 단어 배열할 수 있는 조합
# -> 팰린드롬: 얘는 그냥 뒤집었을 때 똑같은 녀석임
# 문제와 연관 x

# https://corin-e.tistory.com/entry/%EB%B0%B1%EC%A4%80-2607-%EB%B9%84%EC%8A%B7%ED%95%9C-%EB%8B%A8%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys, collections
input = sys.stdin.readline

n = int(input())

ans = 0
first = list(map(str, input().strip()))

for i in range(n - 1) :
    compare = first[:]
    word = input().strip()
    cnt = 0

    for w in word :
        if w in compare :
            compare.remove(w)

        else :
            cnt += 1

    if len(compare) < 2 and cnt < 2 :
        ans += 1


print(ans)

