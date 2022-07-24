nums, target = [-1, 0, 3, 5, 9, 12], 9

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        print("left & right :", left, right)
        print(nums)
        mid = (left + right) // 2
        print("mid : ", mid)

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1
