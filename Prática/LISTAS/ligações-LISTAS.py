a = [2, 3, 4, 7]
b = a
b[2] = 8
# Apartir do momento que eu igualar duas listas se eu mudar um valor em uma delas, ele será alterado nas duas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# COMO CRIAR UMA CÓPIA DE UMA LISTA 
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
# Nesse caso o 8 só será adicionado em B:
print(f'Lista A: {a}')
print(f'Lista B: {b}')