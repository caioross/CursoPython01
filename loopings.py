# Trabalhando com Loopings

palavra = "garrafinha"
contador = 9 
print("Palavra Escolhida: " , palavra)
for letra in palavra : 
    print(contador, " - " , letra)
    contador = contador + 1

cidades = ['São Paulo','Santa Fé do Sul','Londres','Campinas','Três Lagoas']

for cidade in cidades :
    print(cidade)

print(cidades[2])

print("--------------- While ----------------")

botaoExecutar = True #valor boolean
contador = 0
while botaoExecutar :
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False
print('fim da lista')


print('------------  Exercicio ------------')

listaDeCompras = ['Sabão em Pó','Leite Em Pó','Agua em Pó','Detergente','Amaciante','Desinfectante','Alvejnte','Biscoito']
contador = 1
for produto in listaDeCompras :
    # print('[',contador,']' , produto)
    print('[' + str(contador) + '] ' + produto + '\n')
    contador = contador + 1
