import os

def salvar(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        for item in dados:
            linha = ','.join(str(x) for x in item)
            arquivo.write(linha + '\n')

def carregar(nome_arquivo):
    dados = []
    if not os.path.exists(nome_arquivo):
        open(nome_arquivo, 'w').close()
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            dados.append(linha.strip())
    return dados