A = [1.1, 2, 3, 8, 9, 10]
print(sum(A))


def somma(lista):
    s=0
    for i in range(len(lista)):
        s=s+(lista[i])
    return s
print(somma(A))


def somma2(lista):
    s=0
    for item in lista:
        s +=item
    return s
print(somma2(A))