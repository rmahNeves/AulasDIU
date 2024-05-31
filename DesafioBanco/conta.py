VR_DEP = 0
VALOR = 0
SALDO_CC = 2500
VR_SAQUE = 0
OPCAO = 0
VRLD_SAQUE = 1500 # limite de saque
VTL = 0
VTL_D = 1500

while True:
            
    mensagem = """    
        [1] = Deposito
        [2] = Saque
        [3] = Extrato
        [4] = Sair
    """
        
    # Sair do Sistema Bancário
    if OPCAO == 4:
        print(f"Saldo da conta R$ {SALDO_CC}")
        print(F"Limite para saque R$ {VTL_D}")
        break

    # print(f"Saldo da conta R$ {SALDO_CC}")
    # print(f"Limite para saque R$ {VTL_D}")
    print()
    print("Opções :")
    print(mensagem)
    print()

    OPCAO = int(input("Digite uma opção : "))
    print()
	
	# Depósito
    if OPCAO == 1:
        VALOR = float(input("Digitar valor para depósito : "))  
        # print()    
        if VALOR == 0: # Zero mensagem e continua
            print("Erro de processamento, valor zero ou negativo")
            continue
        else:
            # print(f"Valor do depósito R$ {VALOR}")
            SALDO_CC += VALOR # Inclementa a CONSTANTE SALDO_CC
            print()
            print(f"Saldo da conta R$ {SALDO_CC}")
            print()
            print(f"Limite para saque R$ {VTL_D}") 
            print() 
            VALOR = 0 # CONSTANTE VALOR, # volta para 0
    
    #  Saque
    elif OPCAO == 2:
       
       if  VTL_D == 0: # Valor do depósito ZERO, sai do PROGRAMA
           print(f"Saldo da conta R$ {SALDO_CC}") 
           print(F"Limite para saque R$ {VTL_D}")
           break
       else: # Valor do depósito MAIOR QUE ZERO
        print("***** Depósito *****")        
        print()
        print(f"Saldo da conta R$ {SALDO_CC}")
        print(f"Limite para saque R$ {VTL_D}") 
        print()
        VTL = float(input("Digitar valor do saque : "))
        
        if VTL <= 0 : 
            break
        print()        
    
        if VRLD_SAQUE < VTL: # Sem limite para SAQUE
            print(f"Sem limite para saque")
            print(f"Limite para saque R$ {VTL_D}") 
            print()
            break
        
        elif VRLD_SAQUE > VTL: # Com limite para SAQUE
            print("***** Saque *****")
            print()
            VTL_D -= VTL
            SALDO_CC -= VTL
            print(f"Saldo da conta R$ {SALDO_CC}")
            print(f"Limite para saque R$ {VTL_D}") 
            print()
            
    
    # Opção 3 - Extrato   
    elif OPCAO == 3:
        print("***** Extrato da conta *****")
        print()
        print(f"Saldo da conta R$ {SALDO_CC}")
        print(f"Limite para saque R$ {VTL_D}") 
        print() 
                

            