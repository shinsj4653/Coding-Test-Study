def isVowel(letter) :
    return letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u'

while True:
    s = input()
    if s == 'end' :
        break

    lcnt, vcnt = 0, 0
    flag = 0
    is_include_v = 0
    prev = ''

    for i in range(len(s)) :
        idx = s[i]
        if isVowel(idx) :
            lcnt += 1
            vcnt = 0
            is_include_v = 1

        else :
            lcnt = 0
            vcnt += 1

        if lcnt == 3 or vcnt == 3 :
            flag = 1

        if i >= 1 and prev == idx and (idx != 'e' and idx != 'o') :
            flag = 1

        prev = idx

    if is_include_v == 0 :
        flag = 1

    print('<' + s + '> is not acceptable.') if flag else print('<' + s + '> is acceptable.')


