# 4*4 n==4

# .... : 1, ..        ...        . . .    ..
#            .. : 2,    . : 3      .   4  .. 5

# 1 -> 형태 2개
# n * 2

# 2 -> 형태 2개
# 3*3일땐 2 * 2, 4*4일땐 6 * 2 5*5일땐 12 * 2, 6*6일땐, 20 * 2
# (n * (n - 3) + 2) * 2

# 3 -> 형태 4개
# 3*3 : 2 * 4, 4*4 : 6 * 4, 5*5: 12 * 4
# (n * (n - 3) + 2) * 4

# 4 -> 형태 4개
# 3과 동일
# 6n - >24
#(n * (n - 3) + 2) * 4

# 5 -> 형태 1개
# 3*3 : 4, 4*4 : 9, 5*5 : 16
# n * (n - 2) + 1

#O(n^2) -> 1만 -> 완탐 가능할 수도?

idx = 1

def blockForm(y, x, num, shape) :
    if num == 0 :
        if shape == 0 :
            return [(y, x), (y, x + 1), (y, x + 2), (y, x + 3)]
        else :
            return [(y, x), (y + 1, x), (y + 2, x), (y + 3, x)]

    elif num == 1 :
        if shape == 0:
            return [(y, x), (y, x + 1), (y + 1, x + 1), (y + 1, x + 2)]
        else:
            return [(y, x), (y + 1, x), (y + 1, x - 1), (y + 2, x - 1)]

    elif num == 2 :
        if shape == 0 :
            return [(y, x), (y, x + 1), (y, x + 2), (y + 1, x + 2)]
        elif shape == 1 :
            return [(y, x), (y + 1, x), (y + 2, x), (y + 2, x - 1)]
        elif shape == 2 :
            return [(y, x), (y + 1, x), (y + 1, x + 1), (y + 1, x + 2)]
        else :
            return [(y, x), (y, x - 1), (y + 1, x - 1), (y + 2, x - 1)]

    elif num == 3 :
        if shape == 0 :
            return [(y, x), (y, x + 1), (y + 1, x + 1), (y, x + 2)]
        elif shape == 1 :
            return [(y, x), (y + 1, x), (y + 1, x - 1), (y + 2, x)]
        elif shape == 2 :
            return [(y, x), (y,  x + 1), (y - 1, x + 1), (y, x + 2)]
        else:
            return [(y, x), (y + 1, x), (y + 1, x + 1), (y + 2, x)]

    else :
        return [(y, x), (y, x + 1), (y + 1, x), (y + 1, x + 1)]

idx = 1

while(True) :
    n = int(input())

    if n == 0 :
        break

    arr = []
    for i in range(n) :
        li = list(map(int, input().rstrip().split()))
        arr.append(li)

    #print(arr)

    answer = 10e9 * -1

    for num in range(5) :
        for shape in range(4) :
            if num == 0 and shape >= 2 :
                continue

            if num == 1 and shape >= 2 :
                continue

            if num == 4 and shape >= 1 :
                continue

            for i in range(n) :
                for j in range(n) :
                    b_li = blockForm(i, j, num, shape)
                    s_num = 0
                    isSum = True

                    for by, bx in b_li :
                        if 0 <= by < n and 0 <= bx < n :
                            s_num += arr[by][bx]

                        else :
                            isSum = False
                            break

                    if isSum :
                        answer = max(answer, s_num)

    print(str(idx) + '. ' + str(answer))

    idx += 1

