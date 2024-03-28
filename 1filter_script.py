import csv

def remover_duplicatas_e_imagens(nome_arquivo):
    pokemons = set()  # Para manter o controle dos POKEIDs únicos encontrados
    linhas_filtradasGen1 = []
    linhas_filtradasGen2 = []

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        next(leitor)  # Pula o cabeçalho
        for linha in leitor:
            pokeid = int(linha[0])  # Extrai o POKEID da linha
            
            # gen 1
            if pokeid <= 151 and pokeid not in pokemons:
                pokemons.add(pokeid)  # Adiciona o POKEID ao conjunto de pokemons
                linha_sem_imagem = linha[:-1]  # Remove a coluna de imagem no fim
                linhas_filtradasGen1.append(';'.join(linha_sem_imagem))  # Adiciona a linha filtrada

            if pokeid > 151 and pokeid <= 251 and pokeid not in pokemons:
                pokemons.add(pokeid)  # Adiciona o POKEID ao conjunto de pokemons
                linha_sem_imagem = linha[:-1]  # Remove a coluna de imagem no fim
                linhas_filtradasGen2.append(';'.join(linha_sem_imagem))  # Adiciona a linha filtrada
    # Escreve as linhas filtradas em um novo arquivo
    with open('pok_gen1.csv', 'w', encoding='utf-8', newline='') as arquivo_saida:
        escritor = csv.writer(arquivo_saida, delimiter=';')
        for linha in linhas_filtradasGen1:
            escritor.writerow(linha.split(';'))

    with open('pok_gen2.csv', 'w', encoding='utf-8', newline='') as arquivo_saida:
        escritor = csv.writer(arquivo_saida, delimiter=';')
        for linha in linhas_filtradasGen2:
            escritor.writerow(linha.split(';'))



if __name__ == '__main__':
    remover_duplicatas_e_imagens('pok.csv')
    print("Linhas duplicadas e imagens removidas. Novo arquivo salvo como 'pok_gen1.csv' e 'pok_gen2.csv'.")
