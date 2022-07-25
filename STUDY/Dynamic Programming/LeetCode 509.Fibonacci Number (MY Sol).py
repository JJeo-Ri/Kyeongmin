class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n + 1)
        # print(dp)
        
        if n < 2:
            return n
        
        dp[0] = 0
        dp[1] = 1
        
        for idx in range(2, n + 1):
            dp[idx] = dp[idx - 1] + dp[idx - 2]
            
        return dp[n]
