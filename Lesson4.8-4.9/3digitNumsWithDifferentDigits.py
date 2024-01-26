# 3digitNumsWithDifferentDigits
# Display number of three-digit numbers with no repeating digits in a range that I don't really know

p=0
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i!=j and j!=k and i!=k:
                p+=1

print(p)
