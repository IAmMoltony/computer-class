# IndexOfZeroFor
# IndexOfZero but it uses a for loop

N=int(input ('N='))
p=0
for i in range(1,N+1):
    x=int(input(''))
    if x == 0:
        p=i;
        break
print('index=',p)
