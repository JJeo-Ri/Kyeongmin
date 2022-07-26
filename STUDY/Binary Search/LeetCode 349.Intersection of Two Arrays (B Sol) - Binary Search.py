def intersection(nums1, nums2):
    result = set()
    nums2.sort()

    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect_left(nums2, n1)
        print(nums2)
        print("위에서",n1,"이(가) 들어갈 위치는 ",i2)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
    
    return result
