def partition(s):
    if not s:
        return []
    lists = []
    partitions = []

    def backtrack(s, start, partitions, lists):
        # ✅ 모든 부분문자열이 palindrome이라면 lists에 분할 결과를 추가한다.
        if start == len(s):
            lists.append(partitions[:])
            return
        # ✅ i를 증가시키며 부분문자열 길이를 늘려간다.
        for i in range(start + 1, len(s) + 1):
            # ✅ 부분문자열을 만든다.
            tmp_str = s[start:i]
            # ✅ 부분문자열이 palindrome이라면,
            if tmp_str == tmp_str[::-1]:
                # ✅ partitions에 현재 부분문자열을 추가한다.
                partitions.append(tmp_str)
                # ✅ 재귀 함수를 호출한다.
                backtrack(s, i, partitions, lists)
                # ✅ partitions에서 현재 부분문자열을 제거한다.
                partitions.pop()

    backtrack(s, 0, partitions, lists)
    # ✅ 가능한 모든 분할 방식의 결과를 반환한다.
    return lists

partition("aab")