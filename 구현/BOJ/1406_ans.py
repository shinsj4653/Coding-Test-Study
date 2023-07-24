# https://velog.io/@crookid/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-7.-%EC%96%91%EB%B0%A9%ED%96%A5-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8-q
# https://seongonion.tistory.com/53
import sys
input = sys.stdin.readline

st1 = list(input().strip())
st2 = []
m = int(input())

for _ in range(m) :
    command = list(input().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D' :
        if st2:
            st1.append(st2.pop())

    elif command[0] =='B' :
        if st1:
            st1.pop()
    else :
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))

# insert() : 가운데 삽입이 빠른 자료구조
# 연결 리스트
# 삽입 삭제가 가운데에서 자유로운

# 아니면 스택 2개 활용..미쳤..