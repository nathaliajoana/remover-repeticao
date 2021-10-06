import sys
from repeticao import busca_repeticao

# verificando versão
if sys.version_info.major == 2:
    entrada = str(raw_input())
elif sys.version_info.major == 3:
    entrada = str(input())

entrada_lista = entrada.split()

for palavra in entrada_lista:
  answer = busca_repeticao(palavra, entrada_lista)

print(' '.join(answer) + '.')