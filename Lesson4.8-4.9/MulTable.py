# MulTable
# Input the size and print multiplication table
# e.g. input 5 -> 5x5 mul table

N=int(input())
p=0
for i in range(1,N+1):
    for j in range(1,N+1):
        p+=1
        print(p,end="\t")
    print()
