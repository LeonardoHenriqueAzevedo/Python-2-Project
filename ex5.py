"""5. Escreva um algoritmo que leia o código de um determinado
produto e mostre a sua classificação utilize a seguinte tabela
como referência. (escolha... caso)
Codigo - Classificação
1 - Alimento não – perecível
2,3 ou 4 - Alimento perecível
5 ou 6 - Vestuário
7 - Higiene pessoal
8 até 15 - Limpeza e utensílios domésticos
Qualquer outro código inválido
"""

cod = int(input("Informe o código do produto que você deseja (1 a 15): "))

if cod == 1:
    print("Esse produto tem uma classificação de Alimento não – perecível")
elif cod == 2 or cod == 3 or cod == 4:
    print("Esse produto tem uma classificação de Alimento perecível")
elif cod == 5 or cod == 6:
    print("Esse produto tem uma classificação de Vestuário")
elif cod == 7:
    print("Esse produto tem uma classificação de Higiene Pessoal")
elif cod >= 8 and cod <= 15:
    print("Essee produto tem uma classificação de Limpeza e utensílios domésticos")
else:
    print("Esse código informado é inválido, informe um número de 1 a 15.")
