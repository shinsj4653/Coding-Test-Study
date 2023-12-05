# 진짜 나눠야하나 일일이?
# 일일이 해야한다

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, input().split())
answer = ""

while n != 0 :
    answer = num_list[n % b] + answer
    n //= b

print(answer)