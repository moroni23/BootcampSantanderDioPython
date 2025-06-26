menu = """

***** Bem vindo ao DIO's Bank*****

O que deseja fazer hoje? Escolha uma opção abaixo

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

Powered By Python

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato+= f"Depósito: R$ {valor:.2f}\n"
            print(f"O valor de R$ {valor:.2f} foi deposaitado com sucesso.")
        else:
            print("Operação não realizada! O valor fornecido é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada!! Saldo Insuficiente.")
        elif excedeu_limite:
            print("OPeração não realziada! O valor do saque excede o limite!")
        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação não realziada! O valor informado é inválido")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
    
    elif opcao == "q":
        print("Voce saiu do sistema, até breve!")
        break
        
    else:
        print("Operação Inválida, por favor infome novamente a operação desejada!")