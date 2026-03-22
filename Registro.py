from Classes import Cliente, Camiseta, Venda
import os

pasta_dados = 'dados'
if not os.path.exists(pasta_dados):
    os.makedirs(pasta_dados)
arquivo_clientes = os.path.join(pasta_dados, 'clientes.txt')
arquivo_camisetas = os.path.join(pasta_dados, 'camisetas.txt')
arquivo_vendas = os.path.join(pasta_dados, 'vendas.txt')


def salvar(nome_arquivo, lista_objetos):
    with open(os.path.join(pasta_dados, nome_arquivo), 'w') as f:
        for obj in lista_objetos:
            linha = ','.join([str(v) for v in obj.__dict__.values()])
            f.write(linha + '\n')


def carregar(nome_arquivo, classe):
    objetos = []

    if not os.path.exists(os.path.join(pasta_dados, nome_arquivo)):
        open(os.path.join(pasta_dados, nome_arquivo), 'w').close()

    with open(os.path.join(pasta_dados, nome_arquivo), 'r') as f:
        for linha in f:
            partes = linha.strip().split(',')
            try:
                if classe == Cliente:
                    obj = Cliente(int(partes[0]), partes[1])
                elif classe == Camiseta:
                    obj = Camiseta(int(partes[0]), partes[1], int(partes[2]), float(partes[3]))
                else:
                    continue
                objetos.append(obj)
            except:
                pass

    return objetos

