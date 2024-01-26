# Palindrome
# Find palindrome numbers between 2 user-inputted numbers. If not found, print -1
# Unrunnable due to missing colon in the while loop.

A, B=map(int,input().split())
t=0
for i in range(A,B+1):
    n=i;   s=0
    while n >0
        k=n%10; n//=10
        s=s*10+k
    if s==i:
        t=1; print(s, end=' ')
else:
    if t==0:
        print(-1)
