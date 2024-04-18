import textwrap

# Sistema Bancário

# Menu completo
menu = """\n
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova conta
[5\tListar contas
[6]\tNovo usuário
[7]\tSair
=> """

# Menu com poucas opções
menu_simples = """\n
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tSair
=> """

# Definindo variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Condições das funções principais do programa
while True:
    opcao = input(menu_simples)

    # Condição ao selecionar a opção 1
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"

        else: 
            print("Operação falhou! O valor informado é inválido!") 

    # Condições ao selecionar a opção 2
    elif opcao == "2":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
         
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque ecede o limite!")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido!")
    
    # Condições ao selecionar a opção 3
    elif opcao == "3":
        print("\n====================EXTRATO ========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    # Condições ao selecionar a opção 4
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

# Fim do Programa
