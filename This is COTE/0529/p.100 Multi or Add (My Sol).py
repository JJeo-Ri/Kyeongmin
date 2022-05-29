import time

s = input()
start = time.time()
answer = 0
for num in s:
    if answer == 0: # 이건 틀린거임.. 1인 경우에도 더하는 것이 곱하는 것보다 큼!
        answer += int(num)
    else:
        answer *= int(num)

print(answer)
end = time.time()
print("걸린 시간 :", end - start)
# 걸린 시간 : 8.153915405273438e-05
