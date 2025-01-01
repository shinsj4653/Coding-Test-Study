# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# 내 풀이
## 탑 다운
class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [-1 for _ in range(len(cost) + 1)]
        # dp -> 현재 칸까지 오는데 걸린 비용
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[0], cost[1])

        def minCost(idx):

            if idx == 0 or idx == 1:
                return dp[idx]

            if dp[idx] == -1:
                dp[idx] = min(cost[idx - 1] + minCost(idx - 1), cost[idx - 2] + minCost(idx - 2))

            return dp[idx]

        # 1 100 2 2 2 2
        # 최소 비용
        # 일일히 sum 구하면서 계속 돌면 오래걸릴듯.. -> DP!

        # n 3
        # c += min(f(2), f(1))
        # c += min(f(1), f(0))

        # n 10
        # min(9까지 최소 sum, 8까지 최소 sum)
        # min(7까지 최소 sum, 8까지 최소 sum)  min(6까지 최소, 5까지 최소)
        #
        minCost(len(cost))

        for idx, d in enumerate(dp):
            print('idx : ', idx)
            print('value: ', d)

        return dp[len(cost)]

# 바텀업
class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost) + 1)]
        # dp -> 현재 칸까지 오는데 걸린 비용
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[0], cost[1])

        for i in range(3, len(cost) + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])

        return dp[len(cost)]


# 정답

# 탑다운
class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def dp(n):
            if n == 0 or n == 1:
                return 0

            if n not in memo:
                memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])

            return memo[n]

        return dp(len(cost))

# 바텀업
