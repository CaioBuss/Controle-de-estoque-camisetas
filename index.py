from Classes import Camiseta, Cliente, Venda
from Estruturas import ListaEncadeada, Fila, Pilha, somar_estoque
from funcoesMenu import cadastrar_cliente, cadastrar_produto, realizar_venda, desfazer
from Registro import salvar, carregar

clientes = ListaEncadeada()
camisetas = ListaEncadeada()
vendas =Fila()
pilha = Pilha()

for c in carregar('clientes.txt', Cliente):
    clientes.inserir(c)

for p in carregar('produtos.txt', Camiseta):
    camisetas.inserir(p)

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

def main():
    while True:
        menu()
        op = input("Escolha uma opção: ")

        if op == '1':
            cadastrar_cliente(clientes, pilha)
        elif op == '2':
            clientes.imprimir()
        elif op == '3':
            cadastrar_produto(camisetas, pilha)
        elif op == '4':
            camisetas.imprimir()
        elif op == '5':
            id_camiseta = int(input("Insira o ID do produto: "))
            print(camisetas.buscar(id_camiseta))
        elif op == '6':
            realizar_venda(clientes, camisetas, vendas, pilha  )
        elif op == '7':
            vendas.listar()
        elif op == '8':
            desfazer(pilha)
        elif op == '9':
            print(f"Valor total do estoque: R${somar_estoque(camisetas):.2f}")
        elif op == '10':
            total_vendas = sum(v.valor_total for v in vendas)
            print(f"Valor total de vendas: R${total_vendas:.2f}")
        elif op == '11':
            clientes_gastos = {}
            for v in vendas:
                if v.cliente.nome not in clientes_gastos:
                    clientes_gastos[v.cliente.nome] = 0
                clientes_gastos[v.cliente.nome] += v.valor_total
            for nome, gasto in clientes_gastos.items():
                print(f"{nome}: R${gasto:.2f}")
        elif op == '12':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()