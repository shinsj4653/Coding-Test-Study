n = 4
a = ["사과", "딸기", "포도", "배"]

def go(num) :
    ret = ""
    for i in range(4) :
        if num & (1 << i) : # i 번째 비트가 켜져 있는지 확인
            ret += a[i] + " "

    print(ret)

for i in range(1, n) :
    go(1 | (1 << i)) # i번째 비트 켜기