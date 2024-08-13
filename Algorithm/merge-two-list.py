# 2. EXPLAINING THE CONCEPT - BASIC (MERGING TWO LISTS - DIVIDING INTO TWO, CONQUERING EACH, MERGING BACK)
def merging(left, right):
    c=[]
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            c.append(right.pop(0))
        elif left[0] <= right[0]:
            c.append(left.pop(0))
    
    if len(left) > 0:
        for i in left:
            c.append(i)
    if len(right) > 0 :
        for i in right:
            c.append(i)
    return c



left = [2, 5, 6, 10]
right = [3, 4, 12, 20]
print(merging(left, right))


# 3. SORTING RECURSIVELY - TOP DOWN

A = [-5, -23, 5, 0, 23, -6, 23, 67]

def sortArray(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = sortArray(A[:middle])
    right = sortArray(A[middle:])
    merged = []
    while left and right:
        if left[0] <= right [0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged
print(sortArray(A))


# 5. SORTING ITERATIVELY USING PYTHON'S BUILT IN SORTED FEATURE
def merging(A):
    mid = len(A)//2
    left = sorted(A[:mid])
    right = sorted(A[mid:])
    C = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C
print(merging(A))