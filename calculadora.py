# Calculadora Básica em Python


# função que gera o texto de introdução
def intro():
    return '''
  _                                  
 /   _. |  _     |  _.  _|  _  ._ _. 
 \_ (_| | (_ |_| | (_| (_| (_) | (_| 
                                     
 --- Feito por: Seu nome com Amor ---
    '''
# função quera o menu inicial
def mostrar_menu() : 
    return '''
        [1] ou [+] para Somar
        [2] ou [-] para Subtrair
        [3] ou [*] para Multiplicar
        [4] ou [/] para Dividir
        [5] para Sair
        (ou digite sua opção: Somar / Subtrair / Multiplicar / Dividir /Sair)
    '''
#função que le os valores
def ler_valores() :
    valor01 = int(input('Insira o primeiro valor: '))
    valor02 = int(input('Insira o segundo valor: '))
    return valor01, valor02

# funções de calculo
def somar(a ,b) :
    return a + b
def subtrair(a ,b) :
    return a - b
def dividir(a ,b) : # teremos um bug quando divisilvel por 0
    return a / b
def multiplicar(a ,b) :
    return a * b

# função para permanecer ou sair do programa
def desejacontinuar() :
    print('''
        [1] Não, desejo sair!
        [2] Sim, desejo reaizar outro calculo
    ''')
    opcao = input('Deseja realizar outra conta? ')
    return opcao != '1'

# Looping Principal
executar = True
print(intro())
while executar :
    print(mostrar_menu())
    operador = input('Qual a sua opção?: ').strip().lower()

    if operador in ['5','sair']:
        print('Obrigado por usar a melhor calculadora')
        break

    v01, v02 = ler_valores()

    if operador in ['1','+','somar'] :
        resultado = somar(v01, v02)
    elif operador in ['2','-','subtrair'] :
        resultado = subtrair(v01, v02)
    elif operador in ['3','*','multiplicar'] :
        resultado = multiplicar(v01, v02)
    elif operador in ['4','/','dividir'] :
        resultado = dividir(v01, v02)
    else: 
        print('Opção invalida. Tente novamente.')
        continue

    print('Resultado é: ' + str(resultado))
    executar = desejacontinuar()







