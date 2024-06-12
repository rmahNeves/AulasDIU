
numero = 10


def somar(x,y):
    return x + y

def exibendo_msg():
    print("Exibindo mensagem")

def exibir_numero(num):
    global numero
    print(f"O número é : {numero}")
    print(f"O número é : {num}")


print(somar(10,50))
exibendo_msg()
exibir_numero(5)

