def solution(relation):
    answer = []
    row, col = len(relation), len(relation[0])

    for i in range(1, 1 << col):

        flag = False

        for key in answer:
            if key & i == key:
                flag = True
                break

        if flag:
            continue

        s = set()

        for r in range(row):
            st = ''
            for c in range(col):
                if i & (1 << c):
                    st += relation[r][c]

            s.add(st)

        if s == row:
            answer.append(i)

    return len(answer)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])