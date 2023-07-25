def sol() :
    # 문자열 : 조작 불가능
    # 새로운 변수 ans

    # pr request test
    s = input()
    ans = []
    for idx, letter in enumerate(s) :
        if letter == " " :
            ans.append(" ")
        elif letter.isdigit() :
            ans.append(str(letter))
        else :
            if chr(ord(letter) + 13).isalnum() :
                ans.append(chr(ord(letter) + 13))
            else :
                ans.append(chr(ord(letter) + 13 - 26))
    return "".join(ans)

if __name__ == '__main__':
    print(sol())
