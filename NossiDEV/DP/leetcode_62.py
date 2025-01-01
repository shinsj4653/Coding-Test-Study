# https://leetcode.com/problems/unique-paths/

# 탑다운
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # ~를 하는 방법의 개수는?
        # -> | : 오른쪽과 다운
        # 2^(m * n)
        # 2^10000 -> 안됨..

        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dp(y, x):
            if y == 0 or x == 0:
                return 1

            if y - 1 < 0 or x - 1 < 0:
                return 0

            if memo[y][x] == 0:
                memo[y][x] = dp(y - 1, x) + dp(y, x - 1)

            return memo[y][x]

        for i in range(m):
            for j in range(n):
                print(memo[i][j], end=" ")
            print()

        return dp(m - 1, n - 1)

# 바텀업
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # ~를 하는 방법의 개수는?
        # -> | : 오른쪽과 다운
        # 2^(m * n)
        # 2^10000 -> 안됨..

        memo = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memo[i][j] = 1

                else:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]


# 정답
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # ~를 하는 방법의 개수는?
        # -> | : 오른쪽과 다운
        # 2^(m * n)
        # 2^10000 -> 안됨..

        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dp(y, x):
            if y == 0 and x == 0:
                memo[y][x] = 1
                return memo[y][x]

            unique_paths = 0

            if memo[y][x] == 0:
                if y - 1 >= 0:
                    unique_paths += dp(y - 1, x)

                if x - 1 >= 0:
                    unique_paths += dp(y, x - 1)

                memo[y][x] = unique_paths

            return memo[y][x]

        for i in range(m):
            for j in range(n):
                print(memo[i][j], end=" ")
            print()

        return dp(m - 1, n - 1)