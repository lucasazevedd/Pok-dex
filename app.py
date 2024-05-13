# Aluno: Lucas Israel de Azevedo

# Importa a biblioteca pandas
import pandas as pd

# Importa a biblioteca os
import os

# Importa a biblioteca PIL
from PIL import Image

# Importa a biblioteca rich para formatação de tabela
from rich.table import Table
from rich.console import Console

# Obtém o diretório atual do script em execução
diretorio_atual = os.path.dirname(os.path.realpath(__file__))

# Nome do arquivo Excel
arquivo_excel = "pokedex.xlsx"

# Caminho completo para o arquivo Excel
caminho_arquivo = os.path.join(diretorio_atual, arquivo_excel)

# Mensagem de boas-vindas
print('\nSeja bem vindo a Pokédex!\n')

# Loop principal do programa
while True:

    # Menu de opções
    print('O que deseja fazer agora?\n')
    print('(1) Digitar número de um pokemon;')
    print('(2) Digitar nome de um pokemon;')
    print('(3) Ver pokédex completa')
    print('(4) Sair')

    # Solicitação da escolha do usuário
    escolha = input("Escolha uma opção: ")
    
    # Opção 1: Busca por número do pokemon
    if escolha == "1":
            # Lê o arquivo
            dados_excel = pd.read_excel(caminho_arquivo, index_col=0)
            
            # Criar uma tabela Rich
            table = Table(show_header=True)

            # Adiciona cabeçalhos à tabela
            table.add_column("Número")
            table.add_column("Nome")
            table.add_column("Tipo")
            table.add_column("Nível")
            table.add_column("Atributo")
            table.add_column("Evolução")
            table.add_column("Descrição")

            # Solicita o número do Pokemon ao usuário
            numero = int(input("Digite o número do Pokémon desejado: "))

            # Verifica se o arquivo de imagem existe
            imagem_path = (f"pokemons/{numero}.png")

            # Verifica se o número está dentro intervalo 
            if numero < 1 or numero > 151:
                 print("\nPor favor, insira um número entre 1 e 151.\n")
                 continue
            
            # Preenche a tabela
            if numero in dados_excel.index:
                pokemon_data = dados_excel.loc[numero]
                # Adiciona linhas à tabela
                table.add_row(
                    str(pokemon_data.name),
                    str(pokemon_data['Nome']),
                    str(pokemon_data['Tipo']),
                    str(pokemon_data['Nivel']),
                    str(pokemon_data['Atributo']),
                    str(pokemon_data['Evolucao']),
                    str(pokemon_data['Descricao'])
                )
                try:
                    # Exibe a imagem
                    imagem = Image.open(imagem_path)
                    imagem_rgb = imagem.convert("RGB")
                    imagem_rgb.show()
                except ValueError:
                    print("Erro: A imagem não pode ser exibida.")

                # Exibir a tabela
                console = Console()
                console.print(table)

    # Opção 2: Busca por nome do pokemon
    elif escolha == "2":

            # Criar uma tabela Rich
            table = Table(show_header=True)

            # Adiciona cabeçalhos à tabela
            table.add_column("Número")
            table.add_column("Nome")
            table.add_column("Tipo")
            table.add_column("Nível")
            table.add_column("Atributo")
            table.add_column("Evolução")
            table.add_column("Descrição")

            # Localiza a coluna 'Nome' no arquivo
            dados_excel = pd.read_excel(caminho_arquivo, index_col='Nome')

            # Usuário insere o nome do pokemon procurado
            nome = input("Digite o nome do pokemon: ").strip()
            
            # Imprime o resultado na tela
            if nome in dados_excel.index:
                numero = dados_excel.loc[nome, 'Numero']
                dados_pokemon = dados_excel.loc[nome]

                # Adiciona linhas à tabela
                table.add_row(
                    str(numero),
                    str(dados_pokemon.name),
                    str(dados_pokemon['Tipo']),
                    str(dados_pokemon['Nivel']),
                    str(dados_pokemon['Atributo']),
                    str(dados_pokemon['Evolucao']),
                    str(dados_pokemon['Descricao'])
                )

                # Caminho da imagem
                imagem_path = f"pokemons/{numero}.png"

                try:
                    # Exibe a imagem
                    imagem = Image.open(imagem_path)
                    imagem_rgb = imagem.convert("RGB")
                    imagem_rgb.show()
                except ValueError:
                    print("Erro: A imagem não pode ser exibida.")

                # Exibir a tabela
                console = Console()
                console.print(table)
            
            else:
                 print("\nPokémon não encontrado.\n")

    # Opção 3: Pokédex Completa
    elif escolha == "3":
        print("Imprimindo Pokédex...")
        try:
            # Lê o arquivo
            dados_excel = pd.read_excel(caminho_arquivo, index_col=0)

            # Criar uma tabela Rich
            table = Table()

            # Adicionar cabeçalhos à tabela
            table.add_column("Número")
            table.add_column("Nome")
            table.add_column("Tipo")

            # Adicionar linhas à tabela
            for index, row in dados_excel.iterrows():
                table.add_row(
                    str(index),
                    str(row['Nome']),
                    str(row['Tipo']),
                )
                # Adicionar espaço vazio após cada linha de dados
                table.add_row(" ")

            # Exibe a tabela
            console = Console()
            console.print(table)

        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")

        print('\nPara informações mais detalhadas escolha as opções de pesquisa por nome ou número.\n')

    # Opção 4: Sair do programa
    elif escolha == "4":
        print("Saindo do programa.")
        break
    
    # Tratativa de Erro para inserção inválida
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")