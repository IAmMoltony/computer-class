# OddEvenDigitSum
# Check if the sum of digits in the given number is even.
# If it's even, then print "2", otherwise "1".
# e.g. 1234 -> 1 + 2 + 3 + 4 = 10; 10 is even, so print 2

s=k=0
N=int(input())
while N!=0:
    k=N%10
    s+=k
    N//=10
if s% 2==1:
    print(1)
else:
    print(2)
