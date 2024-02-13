# 2-N과 동일한 문제다.
# 문제를 제대로 읽자.
# ([)] 는 안된다 -> 즉, 문자열 내 문자 순서도 잘 고려해야한다.

def check(s) :
    st = []

    for c in s :
        if c == '(' or c == '[':
            st.append(c)

        elif c == ')' :
            if st and st[-1] == '(' :
                st.pop()
                continue

            st.append(c)

        elif c == ']' :
            if st and st[-1] == '[':
                st.pop()
                continue

            st.append(c)
    return len(st) == 0

while True :
    s = input()
    if s == "." :
        break
    print('yes') if check(s) else print('no')