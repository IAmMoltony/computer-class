# NumEven
# Input some numbers by the user and count how many of them are even
# Unrunnable due to incorrect indentation and incorrect spelling of the `+=` operator (I have no idea how they managed to misspell it)

n = int (input ())
s = 0
for i in range (0, n):
    t = int (input ())
    if t % 2== 0:
    s + =1
print (s)
