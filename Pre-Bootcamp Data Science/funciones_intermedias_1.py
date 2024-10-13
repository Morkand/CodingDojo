def iterarDiccionario(lista):
    for x in lista:
        keys = list(x.keys())
        values = list(x.values())
        cadena = ''
        for i, (k, v) in enumerate(zip(keys, values)):
            cadena += f"{k} - {v}"
            if i < len(keys) - 1:
                cadena += ', '
        print(cadena)
iterarDiccionario([
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
)