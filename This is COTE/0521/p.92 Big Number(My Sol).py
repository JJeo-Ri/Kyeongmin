n, m, k = map(int, input().split())
# print(n, m, k)

num = list(map(int, input().split()))
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

print(answer)
