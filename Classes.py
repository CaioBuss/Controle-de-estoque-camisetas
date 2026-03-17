class Camiseta:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Venda:
    def __init__(self, id, cliente, camiseta, valor_total):
        self.id = id
        self.cliente = cliente
        self.camiseta = camiseta
        self.valor_total = valor_total