list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 3]

def intersect(list1, list2):
    resultado = []
    for num1 in list1:
        for num2 in list2:
            if num1 == num2 :
                resultado.append(num1)
    return resultado

print(intersect(list1, list2))