# sol1
# ds : dict -> array
# algo : 조회

# 만약 숫자면, 그 key에 해당하는 값 출력
# 만약 문자면, 그 문자의 key값 출력

# 사전이면, 값에 해당하는 index 출력이 힘듬
# 그래서, 배열이면 index() 함수 사용 가능하니 배열이 나을듯!

from collections import defaultdict

# 인덱스 값 1부터 시작하는 것이 편함
# -> 배열 초기화 : n + 1 크기 만큼!

# 헉 근데 n, m 둘다 최대 크기 10만..
# 그래서 사전 이용해야할듯??
# 사전 2개 이용하면 어떨까??

n, m = map(int, input().split())
dict_key_digit = defaultdict(int)
dict_key_str = defaultdict(str)

for i in range(n) :
    pok = input()
    dict_key_digit[i + 1] = pok
    dict_key_str[pok] = i + 1

# key : 숫자, value : 문자

for i in range(m) :
    val = input()
    print(dict_key_digit[int(val)]) if val.isdigit() else print(dict_key_str[val])

# answer
# 자료구조 2개 사용해야함

# str - int
# 배열 find() -> O(N)
# map 조회 -> O(logN)

# int - str
# 배열 find() -> O(1)
# map 조회 -> O(logN)