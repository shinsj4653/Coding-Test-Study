n = 4
a = ["사과", "딸기", "포도", "배"]
for i in range(1 << n) :
    ret = ""
    for j in range(n) :
        if i & (1 << j) : # j 비트가 켜져있는지
            ret += a[j] + " "

    print(ret)
