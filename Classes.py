class Camiseta:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        def __str__(self):
            return f"ID: {self.id}, Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}"

class Cliente:
    def __init__(self, nome, id):
        self.id = id
        self.nome = nome
        def __str__(self):
            return f"ID: {self.id}, Nome: {self.nome}"

class Venda:
    def __init__(self, id, cliente, camiseta, valor_total):
        self.id = id
        self.cliente = cliente
        self.camiseta = camiseta
        self.valor_total = valor_total
        def __str__(self):
            return f"ID: {self.id}, Cliente: {self.cliente.nome}, Produto: {self.camiseta.nome}, Valor Total: R${self.valor_total:.2f}"