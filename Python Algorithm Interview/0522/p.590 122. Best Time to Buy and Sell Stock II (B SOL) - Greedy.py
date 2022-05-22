class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        
        # 값이 오르는 경우 매번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        
        return result

# 141ms, faster than 5.40%
# 15.2MB, less than 23.07%
