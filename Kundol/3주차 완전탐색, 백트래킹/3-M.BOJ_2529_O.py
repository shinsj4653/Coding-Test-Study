# 오랜만에 실버 문제
# 1초

# k -> 2에서 9 : 8개
# 숫자 : 0 에서 9 : 10개

# 9 * 10 -> 완탐가능

# 최소 -> 0부터 9 순서로 탐색
# 최대 -> 9부터 0순서로 탐색

# < >
# 숫자들을 뺐다가 넣었다가 해야할듯?? 뒤의 괄호로 인해 바뀔수도 있
# visited 활용

# <
# 8 9
#  > < < > > > <
# 9 7

# 8

from itertools import permutations

n = int(input())
bigsmall = input().split()

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def compare(num) :

    for idx, m in enumerate(bigsmall) :
        if m == "<" :
            if num[idx] > num[idx + 1] :
                return False
        else :
            if num[idx] < num[idx + 1] :
                return False

    return True

def changeToNum(num) :
    ret = 0
    for i in range(n + 1):  # 0 1 2
        ret += num[i] * (10 ** (n - i))

    return ret

min_num, max_num = 0, 0
min_list, max_list = [], []

for i in range(n + 1) : # 0 1 2
    min_num += (9 - i) * (10 ** (n - i))
    max_num += i * (10 ** (n - i))

#print(min_num)
#print(max_num)

for num in permutations(nums, n + 1) :
    #print(num)

    if compare(num) :
        ret = changeToNum(num)
        #print('ret : ', ret)
        if ret > max_num :
            max_list = list(num)
            max_num = ret

        if ret < min_num :
            min_list = list(num)
            min_num = ret

for m in max_list :
    print(m, end="")

print()
for m in min_list :
    print(m, end="")

#print(10*9*8*7*6*5*4*3*2*1 * 10 * 9)  #3억..완탐 불가능