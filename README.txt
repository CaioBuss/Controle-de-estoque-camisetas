# 🧾 Sistema de Controle de Estoque em Python

## 📚 Disciplina

Organização e Abstração na Programação

## 📝 Trabalho

Trabalho G1 – Estrutura de Dados com Python

## 👨‍💻 Integrantes

* Caio Buss – RA 1138241

---

## 🎯 Descrição do Sistema

Este projeto consiste em um sistema de controle de estoque e vendas desenvolvido em Python, executado no terminal. O sistema permite o gerenciamento de clientes, produtos (camisetas) e vendas, utilizando conceitos de Programação Orientada a Objetos (POO) e estruturas de dados clássicas.

O sistema também implementa persistência de dados em arquivos `.txt`, garantindo que as informações sejam mantidas entre execuções.

---

## 🧠 Estruturas de Dados Utilizadas

### 🔗 Lista Encadeada

Utilizada para armazenar:

* Clientes
* Produtos

Permite:

* Inserção
* Busca por ID
* Listagem
* Cálculo do valor total do estoque

---

### 📥 Fila (FIFO)

Utilizada para armazenar:

* Vendas realizadas

As vendas são registradas na ordem em que acontecem.

---

### 📚 Pilha (LIFO)

Utilizada para:

* Armazenar o histórico de operações
* Permitir desfazer a última ação realizada

---

## 💾 Persistência de Dados

O sistema utiliza arquivos `.txt` para armazenar dados:

* `clientes.txt`
* `camisetas.txt`
* `vendas.txt`

### Funcionamento:

* Os arquivos são criados automaticamente na pasta `dados/`
* Ao iniciar o sistema, os dados são carregados automaticamente
* Sempre que ocorre uma alteração, os dados são salvos automaticamente

---

## ⚙️ Funcionalidades

1. Cadastrar cliente
2. Listar clientes
3. Cadastrar produto
4. Listar produtos
5. Pesquisar produto
6. Realizar venda
7. Visualizar fila de vendas
8. Desfazer última operação
9. Exibir valor total do estoque
10. Exibir valor total de vendas
11. Exibir clientes e valores gastos
12. Sair

---

## 🛡️ Tratamento de Erros

O sistema possui tratamento para:

* Entrada inválida de dados (letras em números, valores negativos, etc.)
* Campos obrigatórios vazios
* IDs inexistentes
* Estoque insuficiente
* Operações inválidas

O programa nunca encerra abruptamente e sempre retorna ao menu principal.

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado
2. Baixe ou clone o repositório
3. Execute o arquivo principal:

```bash
python index.py
```

---

## 📁 Estrutura do Projeto

```
Projeto/
│
├── index.py
├── Classes.py
├── Estruturas.py
├── funcoesMenu.py
├── Registro.py
├── README.md
│
└── dados/
    ├── clientes.txt
    ├── camisetas.txt
    └── vendas.txt
```

---

## 📌 Observações Finais

* O sistema foi desenvolvido totalmente em Python
* Execução via terminal
* Foco em aplicação prática de estruturas de dados
* Código organizado e modularizado para facilitar manutenção

---
