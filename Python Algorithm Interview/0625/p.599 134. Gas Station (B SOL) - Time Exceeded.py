# 내 풀이랑 비슷함. 결국 이것도 Time Exceeded
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]

            if can_travel:
                return start

        return -1
