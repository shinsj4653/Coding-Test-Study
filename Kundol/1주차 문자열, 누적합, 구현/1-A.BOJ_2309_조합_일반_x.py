sum = 0
hts = []
ans = []

# 9C7 == 9C2
# 2개 고르는 것 -> r이 작으므로 중첩 for문 가능!

ret = []

def solve() :
      for i in range(9) :
          for j in range(i + 1, 9) :
              if sum - hts[i] - hts[j] == 100 :
                  ret.append(i)
                  ret.append(j)

for i in range(9) :
    num = int(input())
    hts.append(num)
    sum += num

solve()

for i in range(9) :
    if i != ret[0] and i != ret[1] :
        ans.append(hts[i])

ans.sort()
for a in ans :
    print(a)