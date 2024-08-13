#BASIC: MERGE SORT

# 1. SORTING ITERATIVELY WITHOUT USING PYTHON'S BUILT IN SORTED FEATURE
A = [-5, -23, 5, 0, 23, -6, 23, 67]
c = []
while A:
    minimum = A[0]
    for x in A:
        if x < minimum:
            minimum = x

    c.append(minimum)
    A.remove(minimum)
print(c)

A = [-5, -23, 5, 0, 123, -6, 23, 67]

d = []
while A:
    maximum = A[0]
    for x in A:
        if x > maximum:
            maximum = x

    d.append(maximum)
    A.remove(maximum)
print(d)
