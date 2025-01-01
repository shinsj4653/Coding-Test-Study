# set() 자료형의 사이즈 : len() 함수 사용하면 된다

N,game = input().split()
N = int(N)

players = set()

for i in range(N) :
    players.add(input())

if game == 'Y':  # 2
    print(len(players))

elif game == 'F' : #3
    print(len(players) // 2)

else: #4
    print(len(players) // 3)