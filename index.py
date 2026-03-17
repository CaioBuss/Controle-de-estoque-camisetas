from Classes import Camiseta, Cliente, Venda
from Estruturas import ListaEncadeada, Fila, Pilha
from funcoesMenu import cadastrar_cliente, cadastrar_produto, realizar_venda, desfazer

cliente = ListaEncadeada()
camiseta = ListaEncadeada()
venda = Fila()
pilha = Pilha()

def menu():
    print('''
===== MENU ESTOQUE =====
1 - Cadastrar cliente
2 - Listar clientes
3 - Cadastrar produto
4 - Listar produtos
5 - Pesquisar produto
6 - Realizar venda
7 - Ver fila de vendas
8 - Desfazer última operação
9 - Exibir valor total do estoque
10 - Exibir valor total de vendas
11 - Exibir clientes e valores gastos
12 - Sair
========================
          ''')

