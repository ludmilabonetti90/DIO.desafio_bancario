menu = """
____MENU____
[1] deposito
[2] saque
[3] extrato
[0] sair
"""

saldo = 2000
limite = 500
extrato = list()
numero_saque = 0
limite_saque = 3 
opções = input(menu)

while opções != "0":
    
    if opções == "1":
        print("opção escolhida: Deposito")
        deposito = int(input("qual valor deseja depositar"))
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Deposito realizado: R${deposito:.2f}")
            print(f"seu novo saldo é R$ {saldo:.2f}")
        else:
            print("transação falhou! O valor do deposito é inválido")
    elif opções == "2":
        saque = int(input("qual valor deseja sacar"))
        if ((saque <= saldo) and (saque <= limite) and (saque > 0)):
            saldo -= saque
            limite_saque -= 1
            extrato.append(f"Saque realizado: R${saque:.2f}")
            print("saque realizado com sucesso")
            print(f"seu novo saldo é R$ {saldo:.2f}")
        elif saque <= 0:
            print("transação falhou! O valor do saque é inválido")
        elif saque > saldo:
            print("saldo excedido")
        elif saque > limite:
            print("limite excedido! Limite = R$ 500,00")
        if limite_saque == 0: 
            print("limite de saques diário excedido")
            break

    elif opções == "3":
        for item in extrato:
            print(item)
        print(f"seu saldo final é R${saldo:.2f}")
    opções = input(menu)

        
        
        