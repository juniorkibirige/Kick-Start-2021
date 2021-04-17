# import sys
# def calc(file):
#     sys.stdin = open(file, 'r')
#     sys.stdout = open(file.split('/')[0]+"/"+file.split('/')[1]+".out", '+w')
T = int(input())
for i in range(T):
    X = 0
    N, K = map(int, input().split())
    S = list(input())
    for a in range(int(N/2)):
        if S[a] != S[N-a-1]:
            X += 1
    if X == K:
        minOp = 0
    elif X > K:
        minOp = X - K
    else:
        minOp = K - X
    print("Case #{}: {}".format(i+1, minOp))
#     sys.stdout = sys.__stdout__

# print("Sample")
# calc('sample_test_set_1/sample_ts1_input.txt')
# print("\ntest 1")
# calc('test_set_1/ts1_input.txt')
# print("\nTest 2")
# calc('test_set_2/ts2_input.txt')
