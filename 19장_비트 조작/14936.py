import sys
input = sys.stdin.readline

answer = 0

n, m = map(int, input().split())

total_result = []
btn = [0] * n
count_arr = [] # 각 동작이 걸리는 횟수 저장

for i in range(4) :
    if i == 0 : # 동작1
        count_arr.append(n)
        continue

    elif i == 3 : # 동작4
        cnt = 1
        for i in range(n + 1) :
            if 3 * i + 1 >= n :
                break
            cnt += 1
        count_arr.append(cnt)

    else :
        if n % 2 == 0 :
            count_arr.append(n // 2)
        else :
            if i == 1 :
                count_arr.append(n // 2 + 1)
            else :
                count_arr.append(n // 2)

#print(count_arr)
end_num = 1 << len(count_arr)


for i in range(1, end_num) :

    m_num = m

    temp_str = str(bin(i)).split("0b")[1]
    zero_num = len(count_arr) - len(temp_str)
    bit_str = '0' * zero_num + temp_str

    for k in range(len(count_arr)) :
        if bit_str[k] == '1' :
            m_num -= count_arr[k]

    if m_num >= 0 :
        answer += 1

print(answer)


