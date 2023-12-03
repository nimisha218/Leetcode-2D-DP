class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # 1
        dp = {}

        # 2
        def dfs(i, j):

            # 2a
            if (i, j) in dp:
                return dp[(i, j)]
            
            # 2b
            if i >= len(s) and j >= len(p):
                return True
            
            # 2c 
            if j >= len(p):
                return False
            
            # 2d
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # 2e
            if (j+1) < len(p) and p[j+1] == "*":
                # We have two options
                # Choose p[j] or skip p[j]
                dp[(i, j)] = (dfs(i, j + 2) or (match and dfs(i+1, j)))
                return dp[(i, j)]
            
            # 2f
            if match:
                dp[(i, j)] = dfs(i+1, j+1)
                return dp[(i, j)]
            
            # 2g
            dp[(i, j)] = False

            # 2h
            return False
        
        # 3
        return dfs(0, 0)
