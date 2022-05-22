import time

n, m = map(int, input().split())
card = []

for _ in range(n):
    card.append(min(list(map(int, input().split()))))

start = time.time()
# print(card)
print(max(card))
end = time.time()
print("걸린 시간 :", end - start)
# 걸린 시간 : 4.696846008300781e-05
