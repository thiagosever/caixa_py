import csv
from tabulate import tabulate
from datetime import datetime

nome_arquivo = 'produtos.csv'  

def carregar_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        dados = [linha for linha in leitor]  
    return dados

def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

def mostrar_estoque_baixo():
    dados = carregar_csv(nome_arquivo)
    estoque_baixo = [linha for linha in dados if int(linha[3]) == 0]
    print("\n===== Itens com Estoque Zerado =====")
    if estoque_baixo:
        print(tabulate(estoque_baixo, headers=["ID", "Produto", "Preço", "Quantidade"], tablefmt="grid"))
    else:
        print("Todos os itens estão com estoque adequado.")

def atender_cliente(cliente_id, compras_diarias):
    dados = carregar_csv(nome_arquivo)
    cliente_nome = f"Cliente {cliente_id}"
    carrinho = []
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    print(f"\n===== Atendimento de  {cliente_nome} ({data_hora}) =====")
    while True:
        try:
            id_produto = input("Digite o ID do produto (ou 0 para finalizar): ")
            if id_produto == '0':
                break

            produto = next((linha for linha in dados if linha[0] == id_produto), None)
            if not produto:
                print("Erro: Produto não encontrado.")
                continue

            quantidade = int(input(f"Digite a quantidade desejada para '{produto[1]}': "))
            if quantidade <= 0:
                print("Erro: Quantidade deve ser maior que zero.")
                continue

            estoque_disponivel = int(produto[3])
            if quantidade > estoque_disponivel:
                print(f"Erro: Estoque insuficiente. Apenas {estoque_disponivel} disponíveis.")
                continue

            confirmacao = input(f"Confirma a compra de {quantidade} x {produto[1]}? (s/n): ").lower()
            if confirmacao != 's':
                print("Item não adicionado ao carrinho.")
                continue

            carrinho.append([produto[0], produto[1], quantidade, float(produto[2]), float(produto[2]) * quantidade])
            produto[3] = str(estoque_disponivel - quantidade)  
            print(f"{produto[1]} adicionado ao carrinho.")

        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")

    if carrinho:
        compras_diarias.append((cliente_nome, carrinho, data_hora))
        salvar_csv(nome_arquivo, dados) 
        print(f"\n===== Compra Finalizada para {cliente_nome} ({data_hora}) =====")
        print(tabulate(carrinho, headers=["ID", "Produto", "Quantidade", "Preço Unitário", "Preço Total"], tablefmt="grid"))
    else:
        print("Nenhum item foi comprado.")

def fechar_caixa(compras_diarias):
    data_hora_fechamento = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"\n===== Fechamento do Caixa ({data_hora_fechamento}) =====")
    total_diario = 0

    if not compras_diarias:
        print("Nenhuma compra foi realizada hoje.")
        return

    for cliente_nome, carrinho, data_hora in compras_diarias:
        print(f"\n{cliente_nome} - {data_hora}")
        print(tabulate(carrinho, headers=["ID", "Produto", "Quantidade", "Preço Unitário", "Preço Total"], tablefmt="grid"))
        total_cliente = sum(item[4] for item in carrinho)
        total_diario += total_cliente
        print(f"Total: R$ {total_cliente:.2f}")

    print(f"\nTotal de Vendas do Dia: R$ {total_diario:.2f}")

def menu():
    cliente_id = 1
    compras_diarias = []
    while True:
        print("\nMenu\n_____________________")
        print("1 - Atender Cliente")
        print("2 - Verificar itens com estoque zerado")
        print("3 - Fechar Caixa")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case '1':
                atender_cliente(cliente_id, compras_diarias)
                cliente_id += 1
            case '2': 
                mostrar_estoque_baixo()
            case '3':
                fechar_caixa(compras_diarias)
                print("Caixa fechado. Até mais!")
                break
            case _:
                print("Informe um valor válido do menu.")

