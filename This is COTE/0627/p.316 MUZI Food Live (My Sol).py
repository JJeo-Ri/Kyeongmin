from collections import Counter

def solution(food_times, k):
    cnt = Counter(food_times)
    
    target_num = 0 # 가장 작은 수
    
    while k >= 0: # while을 쓰면 시간 초과 뜸..
        k = k - len(food_times) + cnt[target_num]
        target_num += 1
    
    return len(food_times) + k


# 시간초과 및 실패 투성이임 (문제를 잘못이해한 듯 함)
