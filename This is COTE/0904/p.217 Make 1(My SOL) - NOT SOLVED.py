# DP는 이렇게 접근하는게 아닌거 같다..
num = int(input())
dp = [0] * ((num + 1) * 10)
start = 1

while dp[num] == 0:
    # 5를 곱한다.
    dp[start * 5] = dp[start] + 1 if dp[start * 5] == 0 else min(dp[start * 5], dp[start] + 1)

    # 3을 곱한다.
    dp[start * 3] = dp[start] + 1 if dp[start * 3] == 0 else min(dp[start * 3], dp[start] + 1)

    # 2를 곱한다.
    dp[start * 2] = dp[start] + 1 if dp[start * 2] == 0 else min(dp[start * 2], dp[start] + 1)

    # 1을 더한다.
    dp[start + 1] = dp[start] + 1 if dp[start + 1] == 0 else min(dp[start + 1], dp[start] + 1)

    print(dp)
    start += 1

print(dp[num])
