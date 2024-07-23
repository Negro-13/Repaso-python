lista = []

print('Ingrese la cantidad de sublistas q desee en su lista')
cantsubls = int(input())

def createlist(cantsubls):
    for i in range(cantsubls):
        print('Agregue su numero en la sublista')
        sublist = []
        while True:
            num = int(input())
            if num == -1:
                break
            sublist.append(num)
        lista.append(sublist)
    return lista

lista = createlist(cantsubls)

print(f'La lista es{lista}')