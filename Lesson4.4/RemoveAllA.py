# RemoveAllA
# Remove all A's from the string inputted by user.
# Unrunnable due to `S` being used in the for loop instead of a lowercase `s`, which is the name for the user-inputted string.

s=input('s=')
for i in S:
    if i=='A'    or i=='a':
        continue
    print(i,end=' ')
