def dobrar_valores(lista_valores):
    for i in range(len(lista_valores)):
        lista_valores[i] = lista_valores[i] * 2
    return lista_valores

def filtrar_pares(lista_valores):
    nova_lista = []
    for i in range(len(lista_valores)):
        if lista_valores[i] % 2 == 0:
            nova_lista.append(lista_valores[i])
    return nova_lista

def somar_elementos(lista_valores):
    soma = 0
    for i in range(len(lista_valores)):
        soma += lista_valores[i]
    return soma

            
def aplicar_operacao(lista_valores, funcao_operacao):
    return funcao_operacao(lista_valores)

lista = [2, 1, 9, 8, 11]
nova_lista = aplicar_operacao(lista, dobrar_valores)

print(nova_lista)
