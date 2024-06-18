class Conta():
  
    def __init__(self, saldo=0, limite=1500):
        self.saldo = float(saldo)
        self.limite = float(limite)
        self.add_correntista = {}

    def escolha(self) :  

            print("Escolha uma opção")

            print('''

                    1 - Extrato
                    2 - Depósito
                    3 - Sacar
                    4 - Adicionar Correntista
                    5 - Pesquisar Correntista
                    6 - Sair
                     

                    ''')
            print()

            self.opcao = int(input("Digite uma opção : "))
            print()

            # if self.opcao == 4:  
    def sair(self):
            print(f"Saldo conta corrente {self.saldo}")
            print(f"Limite para saque {self.limite}")
        

            # if self.opcao == 2:
    def depositar(self):
            self.dep = float(input("Qual o valor do depósito : "))
            self.saldo += self.dep
            print(f"Saldo conta corrente {self.saldo}")
            print(f"Limite para saque {self.limite}")

            # if self.opcao == 3:                
    def sacar(self):
            saque = float(input("Digite o valor do saque : "))
            self.limite -= saque
            print(f"Limite para saque {self.limite}")

            # if self.opcao == 1:      
    def extrato(self):
            print(f"Saldo conta corrente {self.saldo}")
            print(f"Limite para saque {self.limite}")
    
    def ad_correntista(self):
          self.nome = input("Digite nome do correntita : ")
          self.cpf = input("Digite o CPF do correntista : ")
          self.pesquisa_cpf()
  
    def pesquisa_cpf(self):
          self.existe = self.cpf in self.add_correntista.values()
          if self.existe :
                print(f"CPF nº {self.cpf} ,cadastrado")                
          else:
               self.add_correntista.update({'CPF':self.cpf,'Nome':self.nome})
               print(f"{self.nome}, cadastrado !!!")

    def pesquisa_correntista(self):
          self.cpf_pesquisa = input("Digitar CPF parar pesquisar : ")
          self.existe_cpf = self.cpf_pesquisa in self.add_correntista.values()
          if self.existe_cpf :
                print(self.add_correntista)                
          else:
               print(f"Não cadastrado !!!")
          
          

if __name__ == '__main__':
        
        b1 = Conta()
        while True:
            b1.escolha()
            if b1.opcao == 1:
                b1.extrato()
            if b1.opcao == 2:
                b1.depositar()
            if b1.opcao == 3:
                b1.sacar()
            if b1.opcao == 4:
                b1.ad_correntista()
            if b1.opcao == 5:
               b1.pesquisa_correntista()
            if b1.opcao == 6:
                b1.sair()
                break
