def multiplica_por_dos(num):
    lista =[]
    for x in range(0,num):
        lista.append(x*2)
    return lista

def suma_y_resta(lista):
    suma = 0;
    resta = lista[0]
    c = 0
    for x in lista:
        suma+=x
        if(c>0):
            resta-=x
        c+=1
    return suma,resta

def sumatoria_menos_longitud(lista):
    suma = 0
    for x in lista:
        suma+=x
    return suma - len(lista)

def valores_multiplicados_segundo(lista):
    longitud = len(lista)
    nuevaLista = []
    print (longitud)
    if longitud< 2:
        return []
    for x in lista:
        nuevaLista.append(x*lista[1])
    return nuevaLista

def valor_multiplicado_longitud(valor,longitud):
    nuevaLista = []
    for x in range(longitud):
        nuevaLista.append(valor*longitud)
    return nuevaLista

print(multiplica_por_dos(5))
print(suma_y_resta([5, 4]))
print(valores_multiplicados_segundo([1, 3, 5, 7]))
print(valor_multiplicado_longitud(7, 5))
print( valor_multiplicado_longitud(7, 5))
