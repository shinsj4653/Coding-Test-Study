# O(N^2) 불가능

# ()(((()())(())()))(())


# ()
# ((()())

# ((()()))()  q (막대 카운트 0 laser_cnt 1)

# l_cnt + 1 +

from collections import deque
import sys
input = sys.stdin.readline

st = deque([])
l = list(input())
answer = 0

for i in range(len(l) - 1) :
    cur = l[i]

    if st :
        if st[-1] == '(' and cur == ')' :
            st.pop()
            st.append("1")

        else :
            st.append(cur)

    else :
        st.append(cur)


# ( ( ( 1 1 ) ( 1 ) 1 ) ) ( 1 )

# ( ( 2 ( 1 )

# 3 + 2 + 5 + 5 + 2

new_st = deque([])

for s in st :

    if s == ')' :
        num = 0
        while new_st :
            if new_st[-1] == '(' :
                new_st.pop()
                break

            elif new_st[-1].isdigit() :
                num += int(new_st.pop())

        new_st.append(str(num))
        answer += (num + 1)

    else :
        new_st.append(s)

print(answer)

