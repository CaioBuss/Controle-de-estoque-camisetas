#Separei para um arquivo diferente as funções do menu para deixa o index menos poluido e facilitar a compreensão do código.

from Classes import Cliente, Camiseta, Venda
from Estruturas import ListaEncadeada, Fila, Pilha
from Registro import salvar, carregar


def cadastrar_cliente(clientes, pilha):
    nome = input("Nome: ").strip()
    # CAPIVARA
    if not nome:
        print("Nome inválido!")
        return

    cliente = Cliente(id(nome), nome)
    clientes.inserir(cliente)
    pilha.push(("cliente", cliente))
    print("Cliente cadastrado!")


def cadastrar_produto(produtos, pilha):
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome inválido!")
        return

    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            raise ValueError
    except:
        print("Quantidade inválida!")
        return

    try:
        preco = float(input("Preço: ").replace(',', '.'))
        if preco <= 0:
            raise ValueError
    except:
        print("Preço inválido!")
        return

    produto = Camiseta(id(nome), nome, quantidade, preco)
    produtos.inserir(produto)
    pilha.push(("produto", produto))
    salvar('produtos.txt', produtos.to_list())
    print("Produto cadastrado!")


def realizar_venda(clientes, produtos, vendas, pilha):
        id_cli = int(input("ID cliente: "))
        id_prod = int(input("ID produto: "))
        qtd = int(input("Quantidade: "))
        if qtd <= 0:
            raise ValueError
        print("Nada para desfazer")

def desfazer(pilha):
    op = pilha.pop()
    # CAPIVARA
    if op:
        print("Desfeito:", op)
    else:
        print("Nada para desfazer")