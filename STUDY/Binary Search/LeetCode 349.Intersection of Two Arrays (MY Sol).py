class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        # print(nums1, nums2)
        
        # 무조건 작은 크기를 nums1으로..
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        answer = []
        
        nums1, nums2 = list(nums1), list(nums2)
        for idx in range(len(nums1)):
            if nums1[idx] in nums2:
                answer.append(nums1[idx])
                
        return answer
