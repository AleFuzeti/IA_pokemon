from tabulate import tabulate

# Ler os dados do arquivo predictions.txt
with open('predictions.txt', 'r') as file:
    lines = file.readlines()

# Inicializar contadores da matriz de confusão
true_positive = 0
false_positive = 0
true_negative = 0
false_negative = 0

# Percorrer as linhas do arquivo
for line in lines[1:]:  # Ignorar o cabeçalho
    columns = line.strip().split('\t')
    true_value = int(columns[1])
    predicted_value = int(columns[2])
    
    # Atualizar os contadores da matriz de confusão
    if true_value == 1 and predicted_value == 1:
        true_positive += 1
    elif true_value == 0 and predicted_value == 1:
        false_positive += 1
    elif true_value == 0 and predicted_value == 0:
        true_negative += 1
    elif true_value == 1 and predicted_value == 0:
        false_negative += 1

# Calcular acurácia, precisão e recall
accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)
precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0

# Criar a matriz de confusão
confusion_matrix = [
    ["", "Predicted Lost", "Predicted Win"],
    ["Actual Lost", true_negative, false_positive],
    ["Actual Win", false_negative, true_positive]
]

# Imprimir a matriz de confusão e as métricas de avaliação
print("\nMatriz de Confusão:")
print(tabulate(confusion_matrix, headers="firstrow", tablefmt="grid"))
print("\nMétricas de Avaliação:")
print("Acurácia:", accuracy)
print("Precisão:", precision)
print("Recall:", recall)
