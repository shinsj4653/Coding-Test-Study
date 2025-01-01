# 문자열 대문자 소문자 화
# Counter, most_common
# Counter : sys.stdin.readline() -> "\n" 도 포함됨

# https://www.daleseo.com/python-collections-counter/
# collections.Counter() 안에 문자열 넣으면, 각 문자가 문자열에서 몇 번씩 나타나는지 알려주는 객체가 반환된다.

# 문자열 대문자, 소문자 화
# https://ponyozzang.tistory.com/694
# 문자열을 대문자, 소문자 화 시킬 수 있고, 문자열에 대문자, 소문자가 있는지 확인도 가능하다.

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