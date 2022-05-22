class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        
        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx + 1]:
                answer += prices[idx + 1] - prices[idx]
                
        return answer

# 108ms, faster than 23.50%
# 15.1MB, less than 68.35%
