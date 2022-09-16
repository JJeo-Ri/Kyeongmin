# 그리디 알고리즘
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result

'''
bisect_left와 bisect_right의 차이

left는 찾아낸 값의 해당 위치 인덱스를 리턴
right는 찾아낸 값의 다음 인덱스를 리턴

>>> bisect.bisect_left([1, 2, 3, 4, 5], 3)
2

>>> bisect.bisect_right([1, 2, 3, 4, 5], 3)
3

'''
