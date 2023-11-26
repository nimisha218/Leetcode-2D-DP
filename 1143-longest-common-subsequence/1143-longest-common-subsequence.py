class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        rows = len(text1)
        cols = len(text2)

        dp = [[0] * (rows+1) for _ in range(cols+1)]
      
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if text1[row-1] == text2[col-1]:
                    dp[col][row] = 1 + dp[col-1][row-1]
                else:
                    dp[col][row] = max(dp[col-1][row], dp[col][row-1])

        return dp[-1][-1]

        