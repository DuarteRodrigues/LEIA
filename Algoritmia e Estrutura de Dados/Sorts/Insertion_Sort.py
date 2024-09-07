A=[1,5,86,32,12,43,2]
lA = len(A)

for i in range(1,lA):
    chave = A[i]
    j = i-1
    while j >= 0 and A[j] > chave:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = chave

print(A)