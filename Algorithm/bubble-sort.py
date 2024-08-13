#BUBBLE SORT - OPTIMIZED


A = [7, 8, 9, 6, 5, 4, 3, 2, 1]

def bubble_optimized(A):
    iteration = 0
    for i in range(len(A)):
        iteration += 1
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iteration
print(bubble_optimized(A))


def reverse_bubble_optimized(A):
    iteration = 0
    for i in range(len(A)):
        iteration += 1
        for j in range(len(A)-i-1):
            if A[j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iteration
print(reverse_bubble_optimized(A))



