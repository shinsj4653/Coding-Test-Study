from collections import deque

t = int(input())

def check(s) :
    st = deque()
    for d in s :
        if d == '(' :
            st.append(d)

        else :
            if not len(st) == 0 :
                st.pop()

            else :
                # 스택에서 맨 처음에 ")" 이 문자 들어오면 안됨!
                return False

    return len(st) == 0

for i in range(t) :
    data = input()
    print("YES") if check(data) else print("NO")