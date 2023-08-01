N = int(input())
record = list(map(int, input().split()))
line = []
ans = []

for idx, r in enumerate(record) :
    line.append((r, idx + 1))

line.sort()
# 우선 정렬하고 나서, 틀린 것들을 재정렬 하는 걸로?


# 0, 4
# 1, 2
# 1, 3
# 2, 1
# [(0, 6), (0, 7), (1, 2), (1, 3), (1, 4), (2, 5), (6, 1)]

# 답은
# 0, 4
# 1, 2
# 2, 1
# 1, 3
# [(0,6),(1,2),(1,3),(1,4),(0,7),(2,5),(6,1)]

for i in range(1, len(line)) :
    cur_num, cur_person = line[i]
    end = i

    while True :
        cnt = 0
        for j in range(i, end) :
            left_num, person = line[j]
            if cur_person < person :
                cnt += 1

        if cnt > cur_num :
            # 현재 요소를 한칸 전진
            pop_num, pop_person = line.pop(i)
            line.insert(i - 1, (pop_num, pop_person))
            end -= 1
        else :
            break

for idx, result in enumerate(line) :
    if idx < len(line) - 1 :
        print(result[1], end=" ")
    else :
        print(result[1], end="")

