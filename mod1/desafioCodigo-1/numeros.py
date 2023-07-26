n = int(input())

while (n > 0):
    n -= 1
    numeros = input().strip().split(" ")
    if len(numeros) > 1:
        A, B = numeros[0], numeros[1]
        if (len(A) <= 1000 and len(B) <= 1000):
            if A[len(A) - len(B):] == B:
                print("encaixa")
            else:
                print("nao encaixa")
