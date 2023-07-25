n = int(input())
# 최대 높이일 때 까지는 max 높이보다 높아지면 지붕 변화
# max 높이면, 이제 내려가면서 제일 끝 높이보다 높은거 있으면 높이변화, 아니면 쭈욱

storage = []
max_h = 0

for i in range(n) :
    l, h = map(int, input().split())
    if h > max_h :
        max_h = h
    storage.append((l, h))

storage.sort()

# 2 4
# 4 6
# 5 3
# 8 10
# 11 4
# 13 6
# 15 8

#140 - 12 - 16 - 14

last_h = storage[0][1]
last_l = storage[0][0]
end_h = storage[len(storage) - 1][1]
square = (storage[len(storage) - 1][0] - last_l + 1) * max_h
is_going_up = True

for l, h in storage :

    if is_going_up :
        if last_h < h :
            square -= ((l - last_l) * (max_h - last_h))
            last_h = h
            last_l = l

            if h == max_h :
                is_going_up = False

    else :
        if end_h < h < max_h or h == end_h:
            square -= ((l - last_l) * (max_h - h))
            last_l = l
print(square)






