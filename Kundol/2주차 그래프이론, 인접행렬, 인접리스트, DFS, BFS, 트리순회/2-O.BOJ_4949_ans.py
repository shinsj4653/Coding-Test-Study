# 오른쪽 괄호 -> 스택이 비어있을때는 무조건 안됨!

def check(s) :
    st = []
    check = True

    for c in s :
        if c == '(' or c == '[':
            st.append(c)

        if c == ')' :
            if len(st) == 0 or st[-1] == '[' :
                check = False
                break
            else:
                st.pop()

        if c == ']' :
            if len(st) == 0 or st[-1] == '(':
                check = False
                break
            else :
                st.pop()

    return check and len(st) == 0

while True :
    s = input()
    if s == "." :
        break
    print('yes') if check(s) else print('no')