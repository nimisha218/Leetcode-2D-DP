class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0] * (amount+1)] * len(coins)
        amounts = [i for i in range(amount, -1, -1)]

        # Assign base case values 
        for i in range(len(dp)):
            dp[i][-1] = 1

        for i in range(len(dp)-1, -1, -1):

            for j in range(len(dp[0])-2 , -1, -1):
                
                # Check if the right side is in bounds
                if j + coins[i] >= len(dp[0]):
                    right = 0
                else:
                    right = dp[i][j+coins[i]]

                # Check if the down side is in bounds
                if i + 1 >= len(dp):
                    down = 0
                else:
                    down = dp[i+1][j]
                dp[i][j] = right + down
        
        return dp[0][0]
                