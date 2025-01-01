# 최대경우의수 : 2^15 -> 3만

n = int(input())
mp, mf, ms, mv = map(int, input().split())

min_price = 10e9

ingre = []
for i in range(n) :
    # p f s v price
    p, f, s, v, price = map(int, input().split())
    ingre.append((p, f, s, v, price))

ret = []

def check(p, f, s, v) :
    if p >= mp and f >= mf and s >= ms and v >= mv :
        return True
    return False

for i in range(1 << n) :
    sum_p, sum_f, sum_s, sum_v, price, sum_j = 0, 0, 0, 0, 0, 0
    jj = []

    for j in range(n) :
        if i & (1 << j) :
            sum_p += ingre[j][0]
            sum_f += ingre[j][1]
            sum_s += ingre[j][2]
            sum_v += ingre[j][3]
            price += ingre[j][4]
            jj.append(j)

    if check(sum_p, sum_f, sum_s, sum_v) and min_price >= price : # 최소 영양소 값 맞췄다면
        #print('sum_j : ', sum_j)
        # min_price = min(min_price, price)
        min_price = price # 어차피 조건에 min_price >= price 있기 때문에 이렇게 적어도 무관
        ret.append((price, jj))



# 사전 순으로 가장 빠른 것 -> 비트 숫자상 적은것
if len(ret) == 0 :
    print(-1)
else :
    ret.sort(key=lambda x:(x[0], x[1]))
    #print(ret)
    print(ret[0][0])

    for j in ret[0][1]:
        print(j + 1, end=" ")




