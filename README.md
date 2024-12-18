# Caixa de Petshop 🐾

Bem-vindo ao **Caixa de Petshop**, um projeto desenvolvido em **Python** para aprender e aplicar conceitos básicos da linguagem, bem como explorar a conexão com **planilhas** e **bancos de dados** para manipulação e registro de informações.

---

## 📝 Descrição do Projeto
Este projeto consiste na implementação de um sistema simples de caixa para um petshop. Ele permite que o operador:

1. **Abrir o caixa**: Inicia o controle do caixa, zerando os valores ou carregando dados existentes.
2. **Registrar Compras**: Adiciona uma ou mais compras ao sistema durante o dia.
3. **Fechar o caixa**: Finaliza o dia, calculando o total vendido e atualizando as informações de estoque da planilha própria.
4. **Imprimir o relatório**: Exibe o resumo de todas as vendas realizadas no dia, com o total vendido, ao fechamento do caixa.

---

## 🎯 Objetivo

Este projeto foi desenvolvido com os seguintes objetivos:

- Aprender e praticar **conceitos básicos de Python** como:
  - Estruturas condicionais e de repetição.
  - Manipulação de listas e dicionários.
  - Funções e organização do código.

---

## 🚀 Funcionalidades

### 🐕 Abrir o Caixa
- Configura o início do dia, carregando os dados existentes.

### 🛒 Registrar Compras
- Permite o registro de ** compras** com os seguintes dados:
  - Nome do cliente.
  - Produtos adquiridos.
  - Valor total da compra.

### 🏦 Fechar o Caixa
- Finaliza o controle do dia, atualizando os dados:
  - **Na planilha CSV**: Registra as vendas realizadas no dia.
  - **No banco de dados** (se configurado): Persiste os dados para consultas futuras.

### 📊 Imprimir Relatório
- Exibe todas as vendas realizadas no dia e o **total vendido**.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (linguagem principal).


---

## 📂 Estrutura do Projeto

```
caixa_petshop/
├── main.py         # Arquivo principal do projeto.
├── vendas.xlsx     # Planilha para armazenar os dados das vendas.
├── database.db     # Banco de dados SQLite (opcional).
└── README.md       # Documentação do projeto.
```

---


