# ds :
# algo :

# 각 옷 종류 num : dnum * 각 종류에서 하나를 뽑을 경우의 수
# for i in 1 ... dnum + 1 :
#   for 각 옷 종류 :
        # sum += 각 옷 종류 len * dnum

# 각 케이스에 대한 combinations 써봤지만, 시간초과..
# 이건 조합에 대한 재귀로??
# 조합 재귀 사용해서 다시 해봐야겠다

# -> 조합 재귀 사용해도 시간 초과..
# 시간 줄일 수 있는 방법은?? -> 경우의 수 개념 활용!
# 3, 2일 때 -> 각각 아무것도 안입는 경우 +1 하여
# 4 * 3 한다음 아무것도 안 입는 경우를 1만큼 뺴주면 된다!


from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
clo_dict = defaultdict(str)
sum = 0

def combi(start, b, clo_arr, k) :
    global sum
    if len(b) == k :
        num = 1
        for bb in b :
            num *= bb
        sum += num
        return

    for i in range(start + 1, len(clo_arr)) :
        b.append(clo_arr[i])
        combi(i, b, clo_arr, k)
        b.pop()


for i in range(t) :
    n = int(input())
    if n == 0 :
        continue

    for j in range(n) :
        clo, style = input().split()
        if style in clo_dict :
            clo_dict[style] += 1
        else :
            clo_dict[style] = 1

    #print(clo_dict)
    #print(clo_dict.values())

    for k in range(1, len(clo_dict.keys()) + 1) :

        if k == 1 :
            for c in clo_dict.values() :
                sum += c
        else :
            b = []
            combi(-1, b, list(clo_dict.values()), k)

    print(sum)
    clo_dict = defaultdict(str)
    sum = 0
