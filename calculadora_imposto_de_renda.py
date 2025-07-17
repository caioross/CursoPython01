# Calculadora de Importo de Renda no modo Simples!
def calcular_ir(salario):
    # tabela de aliquotas e faixas de imposto de renda
    tabela_ir = [
    {"faixa":(0 , 1903.98), "aliquota": 0, "deducao": 0},
    {"faixa":(1903.99, 2826.65), "aliquota": 7.5, "deducao": 142.80},
    {"faixa":(2826.66, 3751.05), "aliquota": 15, "deducao": 354.80},
    {"faixa":(3751.06, 4664.68), "aliquota": 22.5, "deducao": 636.13},
    {"faixa":(4664.69, float("inf")), "aliquota": 27.5, "deducao": 869.36}
    ]
    # calcular o imposto de renda usando a tabela
    imposto = 0
    for categoria in tabela_ir :
        if salario > categoria['faixa'][0] and salario <= categoria['faixa'][1]:
            imposto = (salario * categoria['aliquota']) / 100 + categoria['deducao']
            break
    return imposto

salario_bruto = float(input('Qual o seu salario bruto? '))
imposto = calcular_ir(salario_bruto)
print(f'O imposto de renda devido é de R$ {imposto:.2f}')