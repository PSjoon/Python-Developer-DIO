menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
=>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limites_saques = 3

while True:
    opcao = input(menu)

    if (opcao == "d"):
        valor = float(input("Valor do depósito: "))

        if (valor > 0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor informado inválido!!!")

    elif (opcao == "s"):
        valor = float(input("Valor saque: "))

        if (valor > saldo):
            print("saldo insuficiente")

        elif (valor > limite):
            print("saque excede limite")

        elif (numero_saques >= limites_saques):
            print("limite de saques diario atingido")

        elif (valor > 0):
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor informado inválido!!!")

    elif (opcao == "e"):
        print("\n******************Extrato******************")
        print("\nnão foram realizadas operações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n*******************************************")

    elif (opcao == "q"):
        break

    else:
        print("ERROR, selecione novamente a operação desejada")
