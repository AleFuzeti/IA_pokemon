import pandas as pd

# Carregar os dados do arquivo CSV
data = pd.read_csv('pok_gen1_w.csv', delimiter=';')

# Função para percorrer a árvore de decisão e fazer a classificação
def classify(data_row):
    if data_row['Defense'] <= 56.0:
        if data_row['HP'] <= 57.5:
            if data_row['HP'] <= 52.5:
                return 0
            elif data_row['Attack'] <= 73.5:
                if data_row['Attack'] <= 37.5:
                    return 0
                else:
                    return 0
            else:
                return 0
        else:
            if data_row['Speed'] <= 85.0:
                if data_row['HP'] <= 75.0:
                    return 0
                else:
                    if data_row['Defense'] <= 32.5:
                        return 0
                    else:
                        return 1
            else:
                return 1
    else:
        if data_row['HP'] <= 60.5:
            if data_row['Speed'] <= 66.5:
                if data_row['HP'] <= 59.5:
                    if data_row['HP'] <= 52.5:
                        return 0
                    else:
                        if data_row['Attack'] <= 73.5:
                            if data_row['Attack'] <= 37.5:
                                return 0
                            else:
                                return 0
                        else:
                            return 1
                else:
                    return 0
            else:
                if data_row['Sp. Def'] <= 97.5:
                    if data_row['Defense'] <= 59.0:
                        return 1
                    else:
                        return 0
                else:
                    return 1
        else:
            if data_row['HP'] <= 80.5:
                if data_row['Defense'] <= 79.0:
                    if data_row['HP'] <= 67.5:
                        return 1
                    else:
                        if data_row['Sp. Def'] <= 72.5:
                            if data_row['Attack'] <= 67.5:
                                return 1
                            else:
                                return 0
                        else:
                            return 1
                else:
                    return 0
            else:
                return 1

# Classificar cada linha de dados
predictions = []
for index, row in data.iterrows():
    predictions.append(classify(row))
# Adicionar as previsões ao DataFrame
data['Prediction'] = predictions

# Salvar o DataFrame com as previsões em um arquivo de texto com identação
data[['ID', 'Win', 'Prediction']].to_csv('predictions.txt', sep='\t', index=False)

print("Dados salvos em 'predictions.txt'")
