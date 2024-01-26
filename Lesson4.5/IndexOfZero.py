# IndexOfZero
# Given a set of numbers, find the index of the first 0.

N=int(input ('N='))
i=p=0
while i < N:
    i=i+1
    x=int(input())
    if x ==0:
        p=i;
        break
print('index=',p)
