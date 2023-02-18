T = int(input())

for i in range(T):
    N, K = input().strip().split(" ")
    N, K = int(N), int(K)
    if (K >= 1 and N <= 10000):
        garrafas = N // K + N % K
        print(garrafas)
