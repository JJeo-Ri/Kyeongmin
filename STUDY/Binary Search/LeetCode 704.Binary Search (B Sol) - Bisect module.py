from bisect import bisect_left, bisect_right

def search(nums, target):
    index = bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
