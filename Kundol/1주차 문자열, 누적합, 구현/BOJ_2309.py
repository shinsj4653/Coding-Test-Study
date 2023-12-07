# 키의 합이 100
# 누적합?
# 근데 그냥 무식하게 2중 for문 해도 되지 않나??

sum = 0
heights = []
answer = []

for i in range(9) :
    heights.append(int(input()))

heights.sort(reverse=True)

# 큰 거 부터 봐야, 만약 넘는 경우 바로 다음 꺼 부터 출력
# 일곱 난쟁이 찾을 수 없는 경우 없으니까, 만약 100 넘으면 바로 그 수 pass



