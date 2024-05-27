

VR_DEP = 0
VALOR = 0
SALDO_CC = 0

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
    opcao = int(input("Digite uma opção : "))

    if opcao == 4:
        break

    if opcao == 1:        
        if VALOR<= 0:
            print("Erro de processamento, valor zero ou negativo")
            continue
        elif VALOR > 0 :
            VR_DEP  += VALOR 
            print(f"Valor do depósito R$ {VR_DEP}")
            continue
                

            