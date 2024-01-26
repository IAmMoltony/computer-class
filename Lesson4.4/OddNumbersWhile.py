# OddNumbersFor
# OddNumbers but it uses a while loop

N,M=map(int,input().split())
N=N-1
while N <=M:
    N=N+1
    if N % 2==0:
        continue
    print(N,end=' ')
