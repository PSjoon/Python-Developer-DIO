import textwrap


def Menu():

    menu = """\n

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Conta
    [nu]\tNovo Usuário
    [q]\tSair

    =>"""

    return input(textwrap.dedent(menu))


def Depositar(saldo, valor, extrato, /):
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso")
    else:
        print("\nERROR")

    return saldo, extrato


def Sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (valor > saldo):
        print("saldo insuficiente")

    elif (valor > limite):
        print("execeu limite saque")

    elif (numero_saques >= limite_saques):
        print("numero de saques excedido")

    elif (valor > 0):
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        print("\nSaque realizado com sucesso")

    else:
        print("ERROR")

    return saldo, extrato


def Exibir_extrato(saldo, /, *, extrato):
    print("\n******************Extrato******************")
    print("\nnão foram realizadas operações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n*******************************************")


def Criar_usuario(usuarios):
    cpf = input("Informe o cpf(somente números): ")
    usuario = Filtrar_user(cpf, usuarios)

    if usuario:
        print("\n CPF já cadastrado")
        return

    nome = input("Nome Completo: ")
    data_nascimento = input("Data Nascimento: ")
    endereco = input(
        "Endereço(logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("cadatro realizado com sucesso")


def Filtrar_user(cpf, usuarios):
    usuario_filtrados = [
        usuarios for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None


def Criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF usuário: ")
    usuario = Filtrar_user(cpf, usuarios)

    if usuario:
        print("Conta criado com sucesso")
        print(usuario)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n conta encerrada, user not-found")


def listar_contas(contas):
    for conta in contas:
        nome = contas['usuario']['nome']
        linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{nome}
            """

        print("=" * 100)
        print(textwrap.dedent(linha))


def Main():

    limite_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = Menu()

        if (opcao == "d"):
            valor = float(input("Valor do depósito: "))

            saldo, extrato = Depositar(saldo, valor, extrato)

        elif (opcao == "s"):
            valor = float(input("Valor saque: "))

            saldo, extrato = Sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif (opcao == "e"):
            Exibir_extrato(saldo, extrato=extrato)

        elif (opcao == "nu"):
            Criar_usuario(usuarios)

        elif (opcao == "nc"):
            numero_conta = len(contas) + 1
            conta = Criar_conta(agencia, numero_conta, usuarios)

            if (conta):
                contas.append(conta)

        elif (opcao == "lc"):
            listar_contas(contas)

        elif (opcao == "q"):
            break

        else:
            print("ERROR, selecione novamente a operação desejada")


Main()
