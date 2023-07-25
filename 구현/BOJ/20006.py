# 출력 조건 한줄한줄 모두 다 읽기
# 사전 순 정렬 -> 이거 못봐서 틀렸었음

p, m = map(int, input().split())
room_list = []


for i in range(p) :
    l, n = input().split()
    l = int(l)

    if len(room_list) == 0: # 맨처음일때
        room = [(l, n)]
        room_list.append(room)

    else :
        isEntered = False
        for room in room_list :
            if len(room) < m and room[0][0] - 10 <= l <= room[0][0] + 10 :
                room.append((l, n))
                isEntered = True
                break

        if not isEntered :
            room = [(l, n)]
            room_list.append(room)

for room in room_list :
    if len(room) == m :
        print("Started!")

    else :
        print("Waiting!")
    room.sort(key=lambda x:x[1])
    for l, n in room :
        print(l, n)

