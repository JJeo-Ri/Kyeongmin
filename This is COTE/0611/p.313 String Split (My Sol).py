# 0과 1의 갯수를 체크 -> 작은 것을 큰 갯수로 replace
import time

s = input()
start = time.time()
s += 'x'
answer = 0

g = []
count_0 = 0
count_1 = 0

while s != 'x':
    for idx in range(len(s) - 1):
        if s[idx] == s[idx + 1]:
            # print(s)
            continue
        else:
            if s[idx] == '0':
                count_0 += 1
            else:
                count_1 += 1

            g.append(s[:idx + 1])
            # print(g)

            s = s[idx + 1:]
            # print(s)
            break
              
print(count_0 if count_0 < count_1 else count_1)
end = time.time()
print("걸린 시간: ", end - start)
# 걸린 시간:  8.7738037109375e-05
