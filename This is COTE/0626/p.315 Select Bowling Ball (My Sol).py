from itertools import combinations
import time

n, m = map(int, input().split())
ball = list(map(int, input().split()))

start = time.time()

U = list(combinations(ball, 2))
# print(U)
cnt = 0

for a, b in U:
    if a == b:
        cnt += 1

print(len(U) - cnt)

end = time.time()
print("걸린 시간: ", end - start)
# 걸린 시간: 5.650520324707031e-05
