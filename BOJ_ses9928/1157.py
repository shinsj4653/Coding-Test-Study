# 문자열 대문자 소문자 화
# Counter, most_common
# Counter : sys.stdin.readline() -> "\n" 도 포함됨

import sys, collections

word = input()
big_word = word.upper()

dict = collections.Counter(big_word)
#print(dict)

if len(dict.values()) == 1 :
    print(dict.most_common(1)[0][0])
else :
    if dict.most_common(2)[0][1] == dict.most_common(2)[1][1] :
        print("?")
    else :
        print(dict.most_common(1)[0][0])