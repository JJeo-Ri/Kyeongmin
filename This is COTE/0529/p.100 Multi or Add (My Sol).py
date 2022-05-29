import time

s = input()
start = time.time()
answer = 0
for num in s:
    if answer == 0:
        answer += int(num)
    else:
        answer *= int(num)

print(answer)
end = time.time()
print("걸린 시간 :", end - start)
# 걸린 시간 : 8.153915405273438e-05
