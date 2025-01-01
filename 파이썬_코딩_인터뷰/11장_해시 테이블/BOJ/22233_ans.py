# 첫 풀이

import collections, sys

n, m = map(int, sys.stdin.readline().split())

# 메모장 단어들 모아둔 사전
w_dict = collections.defaultdict(int)

for i in range(n) :
    w_dict[sys.stdin.readline().strip()] = 1;

# res로 고정시켜둬도 됨
# 어차피 이 값은 점점 주니까 두 번째 for문에서 일일이 초기화할 필요 x
res = n

for i in range(m) :

    written = set(sys.stdin.readline().strip().split(','))

    # dict의 keys() 가 훨씬 많음..written으로 해야 시간 아끼지
    # for key in w_dict.keys() :
    #     if key in written :
    #         w_dict[key] = 0
    #     num += w_dict[key]

    for word in written :
        if w_dict[word] == 1:
            w_dict[word] -= 1
            res -= 1

    print(res)


# 시간 초과 발생..
# 리스트 말고 사전을 최대한으로 활용해야 O(1)로 최대한 변형 가능할 것 같다
# 근데 사전 최대한 활용한 것 같은데...왜 안되지
# 아..만약 많은 양 입력받으면..sys.stdin.readline 써보기