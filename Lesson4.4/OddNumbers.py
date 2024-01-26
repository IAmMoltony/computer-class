# OddNumbers
# Print all odd numbers between two user-specified numbers.

N,M=map(int,input().split())
for i in range (N,M+1):
    if i % 2==0:
        continue
    print(i,end=' ')
