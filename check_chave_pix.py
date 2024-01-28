import os
from validate_docbr import CPF, CNPJ
os.system('cls')

def chavePix(chave):
  chave = chave.strip()
  if '@' in chave:
    return('Tipo: E-mail')
  
  elif len(chave) == 36 and len(chave.split('-')) == 5:
    return('Tipo: Chave aleatória')
  
  elif len(chave) == 11 and chave.isdigit():
    if CPF().validate(chave):
      return('Tipo: CPF')
    else:
      return('Tipo: Celular')
  
  elif CNPJ().validate(chave):
      return('Tipo: CNPJ')
  
  else:
    return('O pix informado é inválido.')

while True:
  os.system('cls')
  chave = input('Chave pix: ')
  print(chavePix(chave))
  input('')
