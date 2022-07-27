def maxSubArray(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

    return max(nums)

# 문제에서 주어진 nums 배열을 활용하여 공간 복잡도도 없앤 코드
