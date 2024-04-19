saldo = 3000.0
historico_saques = []

bemvindo = int(input("Bem-Vindo a Cooperativa Sicredi, digite por favor a sua solicitação \n [1] Realizar Saque \n [2] Realizar um depósito \n [3] Verificar Extrato \n [4] Verificar Histórico de Saques \n [0] Sair \n"))

while bemvindo != 0:

    if bemvindo == 1:
        saque = float(input("Quanto deseja sacar?"))
        if saque > saldo:
            print(f"Não possui saldo suficiente, seu saldo é de R$ {saldo:.2f}, Deseja efetuar uma nova operação?")
        else: 
            saldo -= saque
            historico_saques.append(saque)
            print(f"Saque Realizado com sucesso, seu saldo na conta agora é de R$ {saldo:.2f}") 

    elif bemvindo == 2:
        deposito = float(input("Qual valor que deseja Realizar o depósito?"))
        saldo += deposito
        print(f"Agora seu saldo é de R$ {saldo:.2f}")

    elif bemvindo == 3:
        print(f"Seu saldo conosco é de R$ {saldo:.2f}")

    elif bemvindo == 4:
        print("Histórico de Saques:")
        for i, saque in enumerate(historico_saques, 1):
            print(f"Saque {i}: R$ {saque:.2f}")

    else: 
        print("Sem Opções")

    bemvindo = int(input("O que deseja fazer agora? \n [1] Realizar Saque \n [2] Realizar um depósito \n [3] Verificar Extrato \n [4] Verificar Histórico de Saques \n [0] Sair \n"))

print("Tenha um bom dia")
