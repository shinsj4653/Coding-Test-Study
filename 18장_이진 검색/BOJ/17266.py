n = int(input())
m = int(input())
place = list(map(int, input().split()))
road = [0 for _ in range(n)]

height = 0

height = max(height, min(place), n - max(place))
print(height)
