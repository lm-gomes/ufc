def funcao_padrao(valor):
    def contador():
        return valor + 1
    return contador

for i in range(10):
    contador = funcao_padrao(i)
    print(contador())

