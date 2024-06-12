import re

telefone = '(11) 99402-2873'
padrao = "\([1-9]{2}\) (?:[2-8]|9[0-9])[0-9]{3}\-[0-9]{4}$"   
resposta = re.search(padrao, telefone, flags=0)
if resposta == None:
    print('Tefone inválido ')
else:
    print(f'Número de telefone {resposta} válido ')