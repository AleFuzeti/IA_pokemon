import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

# Carregar os dados
data = pd.read_csv('pok_w.csv', delimiter=';')

# Separar features e target
X = data.drop(columns=['ID', 'Nome', 'Tipo(s)', 'Win'])
y = data['Win']

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o classificador de árvore de decisão
clf = DecisionTreeClassifier()

# Treinar o classificador
clf.fit(X_train, y_train)

# Exportar a árvore de decisão para um arquivo .dot
export_graphviz(clf, out_file='tree.dot', feature_names=X.columns, class_names=['Lost', 'Win'], filled=True, rounded=True)

