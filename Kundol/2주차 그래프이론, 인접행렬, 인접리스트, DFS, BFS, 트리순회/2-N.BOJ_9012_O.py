# 짝짓기, 폭발, 아름다운 괄호 -> 스택 떠올리기!

from collections import deque

t = int(input())


for i in range(t) :
    st = deque()
    data = input()

    for d in data :
        if st :
            if st[-1] == '(' and d == ')' :
                st.pop()
                continue

        st.append(d)

    print("YES") if len(st) == 0 else print("NO")