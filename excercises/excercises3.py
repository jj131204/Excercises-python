
lista = [-25, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        if x < menor:
            menor =  x

print('menor', menor)
