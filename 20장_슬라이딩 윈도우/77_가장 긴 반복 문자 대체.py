import collections

def characterReplacement(s: str, k: int) -> int :
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s) + 1) :
        print('right', right)
        counts[s[right - 1]] += 1
        print('counts', counts)
        # 가장 흔하게 등장하는 문자 탐색
        max_char_n = counts.most_common(1)[0][1]
        print('max_char_n', max_char_n)

        # k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k :
            counts[s[left]] -= 1
            print('counts', counts)
            left += 1
            print('left', left)

    return right - left

if __name__ == '__main__':
    print(characterReplacement("AAABBC", 2))