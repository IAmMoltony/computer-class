# ShortStudents
# Input the height of each student, then display the number of students who are considered to be short (shorter than 140cm)
# Unrunnable due to mismatching quotes in the first line.

N=int (input("Number of students ='))
i=x=z=0
for i in range (1,N+1):
    print(str(i),end='')
    x=int(input('-Student height='))
    if x<140:
        z+=1
print ('Number of short students =',z)
