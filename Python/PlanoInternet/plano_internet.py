# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
consumo = 0
plano = ""
def recomendar_plano(num):
    global consumo
    global plano

# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
    if consumo <= 10 :
        plano = ("Plano Essencial Fibra - 50Mbps")
    elif consumo > 10 and consumo <=20 :
        plano = ("Plano Prata Fibra - 100Mbps")
    else:
         plano = ("Plano Premium Fibra - 300Mbps")
# TODO: Retorne o plano de internet adequado:
    return plano
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)
print(recomendar_plano(plano))