vowel = ['a', 'e', 'i', 'o', 'u']
# 모음, 자음 연속 여부
# 모음 : lcnt, 자음 : vcnt
# -> 탐색하면서  if isVowel 이면 lcnt++, vcnt = 0, 아니면 lcnt = 0, vcnt++

# 같은 글자 두개 연속 여부
# -> prev 사용하면됨!


while True :
    p = input()
    if p == 'end' :
        break

    acceptable = True

    # a,e,i,o,u 중 하나를 반드시 포함해야한다.
    is_v = False
    for v in vowel :
        if v in p :
            is_v = True
            break

    if not is_v :
        acceptable = False

    # 모음 3개 혹은 자음 3개 연속으로 오면 안된다.
    for i in range(len(p) - 2) :
        if (p[i] in vowel and p[i + 1] in vowel and p[i + 2] in vowel) or \
                (p[i] not in vowel and p[i + 1] not in vowel and p[i + 2] not in vowel) :
            acceptable = False
            break

    # 같은 글자 연속적으로 두번 오면 안됨! 단, ee나 oo는 허용
    for i in range(len(p) - 1) :
        if p[i] == p[i + 1] :
            if p[i] != 'e' and p[i] != 'o' :
                acceptable = False
                break


    print('<' + p + '> is not acceptable.') if not acceptable else print('<' + p + '> is acceptable.')
