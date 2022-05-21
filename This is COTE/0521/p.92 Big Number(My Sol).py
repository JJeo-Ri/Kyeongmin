import time

n, m, k = map(int, input().split())
# print(n, m, k)

num = list(map(int, input().split()))
start = time.time()
num.sort(reverse=True)
# print(num)

answer = 0
idx = 0
limit = 0

for i in range(m):
    # print(answer)
    if limit == k:
      answer += num[idx + 1]
      limit = 0
      continue

    answer += num[idx]
    limit += 1
    # continue

end = time.time()
print(answer)
print("걸린 시간 :", end - start)
# 걸린 시간 : 6.771087646484375e-05
# reverse = True 하는 곳에서 시간을 더 잡아먹는 듯.
