def preProcess(mat, R, C):
    return mat[R][C] if len(mat) > len(mat[0]) else mat[C][R]

def query(a, b):
    return max((min(a//2, b) - 1) + (min(a, b//2)-1), 0)

def calc():
    R, C = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(R)]
    result = 0
    for direction in lambda x: x, reversed:
        dp = [0]*min(R, C)
        for i in direction(range(max(R, C))):
            for direction in lambda x:x, reversed:
                cur = 0
                for j in direction(range(min(R, C))):
                    if not preProcess(matrix, i, j):
                        dp[j] = 0
                        cur = 0
                        continue
                    dp[j] += 1
                    cur += 1
                    result += query(cur, (dp[j]+1)//2)
    return result
T = int(input())
for case in range(T):
    print("Case #{}: {}".format(case, calc()))