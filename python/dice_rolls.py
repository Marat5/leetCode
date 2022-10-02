class Solution:
    # DFS tree. We hash the answers that were already calculated and it works very fast
    # def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    #     modulo = 10**9 + 7

    #     def helper(hashmap, dice_count: int, target: int) -> int:
    #         if target < 1 or target > dice_count * k:
    #             return 0

    #         if dice_count == 1:
    #             return 1

    #         if (dice_count, target) in hashmap:
    #             return hashmap[(dice_count, target)]

    #         total_for_dice_count = 0
    #         for i in range(1, k + 1):
    #             total_for_dice_count += helper(hashmap,
    #                                            dice_count - 1, target - i) % modulo
    #         hashmap[(dice_count, target)] = total_for_dice_count
    #         return hashmap[(dice_count, target)]

    #     return helper({}, n, target) % modulo

    # Dynamic programming
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10**9 + 7
        # Columns are dice count, rows are targets
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # We need this to populate row 1 with 1's for all possible k options of one dice
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(i, target + 1):
                total_for_ij = 0
                for last_dice in range(1, k + 1):
                    if j - last_dice < 0:
                        break
                    total_for_ij += dp[i - 1][j - last_dice]
                dp[i][j] = total_for_ij % modulo

        return dp[-1][-1]


print(Solution().numRollsToTarget(30, 30, 500))
