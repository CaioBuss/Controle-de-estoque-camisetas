#Separei para um arquivo diferente as funções do menu para deixa o index menos poluido e facilitar a compreensão do código.

from Classes import Cliente, Camiseta, Venda
from Estruturas import ListaEncadeada, Fila, Pilha

def cadastrar_cliente(clientes, pilha):
    nome= input("Insita o nome: ")
    if nome:
        cliente = Cliente(id(nome), nome)
        clientes.inserir(cliente)
        pilha.push(('cliente', cliente))
        print("Cliente cadastrado com sucesso!")

def cadastrar_produto(camisetas, pilha):
    nome = input("Insira o nome do produto: ")
    quantidade = int(input("Insira a quantidade: "))
    preco = float(input("Insira o preço: ")) 
    if nome and quantidade > 0 and preco > 0:
        camiseta = Camiseta(id(nome), nome, quantidade, preco)
        camisetas.inserir(camiseta)
        pilha.push(('camiseta', camiseta))
        print("Produto cadastrado com sucesso!")

def realizar_venda(clientes, camisetas, vendas, pilha):
    id_cliente = int(input("Insira o ID do cliente: "))
    id_camiseta = int(input("Insira o ID do produto: "))
    quantidade = int(input("Insira a quantidade: "))
    cliente_encontrado = clientes.buscar(id_cliente)
    produto_encontrado = camisetas.buscar(id_camiseta)
    if cliente_encontrado and produto_encontrado and produto_encontrado.quantidade >= quantidade:
        valor_total = produto_encontrado.preco * quantidade
        venda_atual = Venda(id(cliente_encontrado), cliente_encontrado, produto_encontrado, quantidade, valor_total)
        vendas.enqueue(venda_atual)
        pilha.push(('venda', venda_atual))
        produto_encontrado.quantidade -= quantidade
        print("Venda realizada com sucesso!")
    else:
        print("Cliente ou produto não encontrado, ou produto sem estoque.")

def desfazer():
    op = Pilha.pop()
    if op:
        print("Operaçao desfeita:", op)
    else:
        print("Nada para desfazer.")