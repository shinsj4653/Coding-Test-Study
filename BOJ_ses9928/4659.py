# 영어에서 모음 -> 원래 5개... -> 데이터 범위에 대해서 한번씩 꼭 생각해보기
vowels = ['a', 'e', 'i', 'o', 'u']

while True :
    p = input()

    if p == 'end' :
        break

    flag = True

    if p.find('a') == -1 and p.find('e') == -1 and p.find('i') == -1 and p.find('o') == -1 and p.find('u') == -1:
        print(f'<{p}> is not acceptable.')
        continue
    else :
        for i in range(len(p) - 1) :
            if p[i] == p[i + 1] and p[i] != 'e' and p[i] != 'o' and p[i + 1] != 'e' and p[i + 1] != 'o'  :
                flag = False
                break

            if i > 0 :
                if (p[i - 1] in vowels and p[i] in vowels and p[i + 1] in vowels) \
                    or (p[i - 1] not in vowels and p[i] not in vowels and p[i + 1] not in vowels):
                        flag = False
                        break
    if flag :
        print(f'<{p}> is acceptable.')
    else :
        print(f'<{p}> is not acceptable.')


