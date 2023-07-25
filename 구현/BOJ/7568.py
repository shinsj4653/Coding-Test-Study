N = int(input())

l = []
sorted_l = []
place = []

for i in range(N) :
    w, h = map(int, input().split())
    l.append((i, w, h))

sorted_l = sorted(l, key=lambda x:(-x[1], -x[2]))
# print(sorted_l)
save_index = 1

for i in range(N) :
    index, w, h = sorted_l[i]
    if i == 0:
        place.append((index, i + 1))
    else :
        if sorted_l[i - 1][1] > w and sorted_l[i - 1][2] > h :
            place.append((index, i + 1))
            save_index = i + 1
        else :
            place.append((index, save_index))

#print(place)

for i in range(N) :
    for p in place :
        ans = p[1]
        if l[i][0] == p[0] :
            print(ans, end=" ")
            break