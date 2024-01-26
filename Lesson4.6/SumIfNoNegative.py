# SumIfNoNegative
# Input some numbers, if there are no negative numbers then print their sum, otherwise error.

N=int(input ('N='))
s=0
for i in range(1,N+1):
    x=int(input())
    s+=x
    if x <0:
        print('The sequence contains a negative number')
        break
else:
    print('s=',s)
