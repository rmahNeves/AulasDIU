

VR_DEP = 0
VALOR = 0
SALDO_CC = 0
VR_SAQUE = 0
OPCAO = 0

while True:
            
    mensagem = """    
        [1] = Deposito
        [2] = Saque
        [3] = Extrato
        [4] = Sair
    """
    print("Opções :")
    print(mensagem)
    print()

    OPCAO = int(input("Digite uma opção : "))
    print()

    if OPCAO == 4:
        break
    if OPCAO == 1:
        VALOR = float(input("Digitar valor para depósito : "))      
        if VALOR == 0:
            print("Erro de processamento, valor zero ou negativo")
            continue
        else:
            VR_DEP  += VALOR 
            print(f"Valor do depósito R$ {VR_DEP}")
            VALOR = 0
            SALDO_CC += VR_DEP
            print(f"Saldo da conta R$ {SALDO_CC}")
            continue
    if OPCAO == 2:
        VR_SAQUE = float(input("Digitar valor para do saque : "))  
        if SALDO_CC < VR_SAQUE:
            print("Saldo insuficiente")
            break
        else:
             SALDO_CC -= VR_SAQUE
             print(f"Saldo da conta R$ {SALDO_CC}")
             continue
       
print(f"Saldo da conta R$ {SALDO_CC}")
                

            