#Nada é executado nessa parte. É como se estivéssemos passando para uma variavel os próximos resultados resultantes da operação. Funciona como um stream.
lazy_gen = (x**2 for x in range(1000000))


#Print dos 10 próximos valores (next)
for i in range(10):
    print(next(lazy_gen))