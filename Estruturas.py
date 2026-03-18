class Node: # to usando muito GDScript, me deixa >:(
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
    
    def inserir(self, valor):
        novo_node = Node(valor)
        novo_node.proximo = self.cabeca
        self.cabeca = novo_node

    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

def buscar(self, id):
    atual = self.cabeca
    while atual:
        if atual.valor.id == id:
            return atual.valor
        atual = atual.proximo
    return None

def somar_estoque(self):
    total = 0
    atuial = self.cabeca
    while atual:
        total += atual.valor.preco * atual.valor.quantidade
        atual = atual.proximo
    return total

class Fila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None