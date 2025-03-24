menu = """
Escolha uma opção:
[1] Extrato
[2] Saque
[3] Depósito
[4] Encerrar
=> """

saldo_conta = 0
limite_saque = 500
historico = ""
qtd_saques = 0
MAX_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        # Exibe o extrato
        print("\n************ EXTRATO ************")
        if not historico:
            print("Nenhuma movimentação registrada.")
        else:
            print(historico)
        print(f"\nSaldo disponível: R$ {saldo_conta:.2f}")
        print("***********************************")

    elif opcao == "2":
        # Realiza o saque
        if qtd_saques >= MAX_SAQUES:
            print("Falha no saque! Limite de saques atingido.")
        else:
            saque = float(input("Informe o valor do saque: R$ "))

            if saque <= 0:
                print("Falha no saque! O valor precisa ser maior que zero.")
            elif saque > saldo_conta:
                print("Falha no saque! Saldo insuficiente.")
            elif saque > limite_saque:
                print("Falha no saque! O valor excede o limite permitido.")
            else:
                saldo_conta -= saque
                historico += f"Saque de R$ {saque:.2f}\n"
                qtd_saques += 1
                print(f"Saque de R$ {saque:.2f} realizado com sucesso!")

    elif opcao == "3":
        # Realiza o depósito
        deposito = float(input("Qual valor deseja depositar? R$ "))

        if deposito <= 0:
            print("Erro! O valor do depósito deve ser maior que zero.")
        else:
            saldo_conta += deposito
            historico += f"Depósito de R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")

    elif opcao == "4":
        # Finaliza o programa
        print("Sessão encerrada!")
        break

    else:
        # Caso a opção seja inválida
        print("Opção inválida! Por favor, tente novamente.")