import csv
from tabulate import tabulate
from util import *

try:
    carregar_csv(nome_arquivo)
    print('Caixa aberto com sucesso.')
except Exception as e:
    print(f"Erro ao abrir o caixa: {e}")

menu()



    

