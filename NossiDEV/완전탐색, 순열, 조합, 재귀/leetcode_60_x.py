def getPermutation(n, k) :
    count = 1  # Local to getPermutation
    arr = [str(i + 1) for i in range(n)]
    answer = ""

    def dfs(n, r, depth, arr):
        nonlocal count, answer  # Use nonlocal to refer to count and answer in the outer scope
        if count > k:
            return

        if r == depth:
            if count == k:
                answer = "".join(arr)
            count += 1
            return

        for i in range(depth, n):
            arr[i], arr[depth] = arr[depth], arr[i]
            dfs(n, r, depth + 1, arr)
            arr[i], arr[depth] = arr[depth], arr[i]

    dfs(n, n, 0, arr)
    return answer

getPermutation(3, 5)