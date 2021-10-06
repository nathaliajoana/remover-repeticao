resposta, changes = [], []

def busca_repeticao(entrada, entrada_lista):
    x = len(entrada)
    if x == 2:
        if entrada[0] == entrada[1]:
            resposta.append(entrada[0])
            changes.append(1)
    elif x % 2 != 0:
        if entrada[1:int(x/2 + 1)] == entrada[int(x/2 + 1):]:
            resposta.append(entrada[:int(x/2 + 1)])
            changes.append(1)
    elif x % 2 == 0:
        if entrada[-4:-2] == entrada [-2:]:
            resposta.append(entrada[:-2])
            changes.append(1)
    if len(changes) == len(entrada_lista):
        return resposta
    else:
        return entrada_lista