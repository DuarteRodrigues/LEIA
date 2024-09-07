A=[1,5,86,32,12,43,2]
lA = len(A)

for i in range(lA):
    minimo=i
    for j in range(i+1, lA):
        if A[j] < A[minimo]:
            minimo = j
    A[i], A[minimo] = A[minimo], A[i]

print(A)