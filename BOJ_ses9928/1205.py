import sys

N, score, P = map(int, input().split())
if N > 1 :
    s_list = list(map(int, sys.stdin.readline().split()))

if N == 0:
    print(1)

else :
    for i in range(len(s_list)) :
        if score >= s_list[i] :
            if i == 0 :
                print(1)
                break
            elif i > 0 and i < len(s_list) - 1 :
                print(i + 1)
                break

            else :
                if score > s_list[i]:
                    print(len(s_list))
                    break
                else:
                    if N == P :
                        print(-1)
                        break
                    else :
                        print(len(s_list))
                        break



