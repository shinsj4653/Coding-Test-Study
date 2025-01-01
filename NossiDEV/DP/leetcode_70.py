# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1혹은 2
        # 바텀업
        # 3 -> 1계단 + 2계단 or 2계단 + 1계단
        # 4 -> 1계단 + 3계단 or  2 2
        # 5 -> 1,4 2,3
        # 6 -> 1,5 2,4

        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0 for _ in range(n + 1)]  # n 계단 오르는 데 경우의 수
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        # 4
        # 1 3가지

        # 1, 1 1, 1
        # 1, 1, 2
        # 1, 2, 1

        # 2, 1 1
        # 2, 2

        # 5

        # 1, 4

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        for d in dp:
            print(d)

        return dp[n]
