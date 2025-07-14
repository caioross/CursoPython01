# Trabalhando com IF  e testes
tipoEscola = input("Tipo do Colegio: \n [1] - Publico \n [2] - Partiular \n Resposta: ")
freqAluno = input("Qual a frequência do aluno?")
nomeAluno = input("Qual o nome do Aluno: ")
mediaAluno = int(input("Qual a media do aluno: "))
#mediaEscola = input("Media de corte da Escola")
mediaEscola = 7
freqAluno = int(freqAluno)


if tipoEscola == "2": 
    print("----- Colégio Particular -----")
    if mediaAluno >= mediaEscola and freqAluno >= 70 :
        print("Aprovado")
    else :
        print('reprovado')

if tipoEscola == "1" :
    print("----- Colégio Particular -----")
    if mediaAluno >= mediaEscola or freqAluno >= 60 :
        print("Aprovado")
    else : 
        print("Reprovado")





    