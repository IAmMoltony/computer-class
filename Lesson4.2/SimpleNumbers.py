# SimpleNumbers
# Input a sequence of numbers and display the "simple" ones.
# A "simple" number is a number that is only divisible by itself and by 1.
# Unrunnable due to incorrect indentation in last if-statement.

import math
N=int (input())
i=j=x=0
for i in range (1,N+1):
    x=int(input())
    z=0
    for j in range (2,round(math.sqrt(x))):
        if x%j==0:
            z=1
if z==0:
print(x)
