# 시간 초과
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas >= cost 인 인덱스 Check!
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue             
            # 여기서부터 시작
            count = 0
            remain = 0
            
            for j in range(i, i + len(gas)):
                remain = remain + gas[j % len(gas)] - cost[j % len(gas)]
                if remain < 0:
                    break
                    
                count += 1
                
            if count == len(gas):
                return i
            
        return -1
