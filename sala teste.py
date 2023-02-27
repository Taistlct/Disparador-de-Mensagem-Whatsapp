mensagem = "Esta é a primeira linha.\nEsta é a segunda linha.\nEsta é a terceira linha."

linhas = mensagem.split('\n')
variaveis = []

for linha in linhas:
    variaveis.append(linha)
    
print(len(variaveis))
print(variaveis[0])
print(variaveis[1])
print(variaveis[2])
