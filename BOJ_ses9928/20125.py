N = int(input())
s = []
l_arm = 0
r_arm = 0
waist = 0
l_leg = 0
r_leg = 0

head_found = False
leg_found = False
h_x = 0
h_y = 0

for i in range(N) :
    row = []
    line = input()
    if not head_found :
        for j in range(N) :
            if not head_found and line[j] == '*' :
                print(i + 2, j + 1)
                head_found = True
                h_x = i + 1
                h_y = j

    if i == h_x  :
        # str 은 도중 변경 불가!
        # line[h_y] = 'h'
        # split_line = line.split('h')
        # l_arm = split_line[0].count('*')
        # r_arm = split_line[1].count('*')
        for r in range(len(line)) :
            if line[r] == '*' :
                if r < h_y :
                    l_arm += 1

                elif r > h_y :
                    r_arm += 1

    if i > h_x :

        if not leg_found and line.count("*") == 1:
            waist += 1

        if line.count("*") > 1 :
            leg_found = True

        if leg_found :
            if line[h_y - 1] == "*" :
                l_leg += 1

            if line[h_y + 1] == "*" :
                r_leg += 1

    s.append(row)

print(l_arm, r_arm, waist, l_leg,r_leg)






