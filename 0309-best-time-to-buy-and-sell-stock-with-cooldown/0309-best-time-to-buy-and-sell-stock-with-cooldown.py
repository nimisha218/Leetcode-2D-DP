class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 1
        dp = {}

        # Key -> (i, buying) -> i is the index we are at, buying is a boolean value 
        # representing the state we are at (buying for True and selling for False)

        # Value -> maximum profit at ith index and buying state

        # 2
        def dfs(i, buying):
            
            # 2a
            if i >= len(prices):
                return 0
            
            # 2b
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # 2c
            cooldown = dfs(i+1, buying)

            # 2di
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            # 2dii
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            
            # 2e
            return dp[(i, buying)]
        
        # 3
        return dfs(0, True)

        