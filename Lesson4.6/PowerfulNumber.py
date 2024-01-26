# PowerfulNumber
# Check if the inputted number is "powerful".
# A "powerful" number has no digits less than 5.
# e.g. 1234 is a "powerless" number, 6587 is a "powerful" number

N=int(input ('x='))
k=s=0
while x!=0:
    k=x%10
    x//=10
    if k < 5:
        print('No')
        break
else:
    print('Yes')
