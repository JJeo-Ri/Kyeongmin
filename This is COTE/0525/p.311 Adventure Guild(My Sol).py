import time
n = int(input())
people = list(map(int, input().split()))
# print(people)

start = time.time()
people.sort(reverse=True)
answer = 0

while people:
    group = people[0]
    people = people[group:]
    answer += 1

print(answer)
end = time.time()
print("걸린 시간 :", end - start)
# 걸린 시간 : 4.076957702636719e-05
