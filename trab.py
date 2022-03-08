# Importando somente o necessário
import scipy
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from scipy.io import arff
from collections import defaultdict
from sklearn.svm import SVC
# # classificadores
from skmultilearn.problem_transform import LabelPowerset
from skmultilearn.adapt import MLkNN
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.ensemble import RandomForestClassifier

# Cada info tem 2 campos, nome do dataset e a quantidade
# de colunas no Y
datasetsName = [('birds', 19),
                ('yeast', 14),
                ('flags', 7),
                ('genbase', 27),
                ('emotions', 6)]

# Inicializando as variaveis
data_train = [0, 0, 0, 0, 0]
meta_train = [0, 0, 0, 0, 0]
X_train = [0, 0, 0, 0, 0]
X_test = [0, 0, 0, 0, 0]
Y_train = [0, 0, 0, 0, 0]
Y_test = [0, 0, 0, 0, 0]
data_test = [0, 0, 0, 0, 0]
meta_test = [0, 0, 0, 0, 0]


def convert(a):
    # tenta converter para uma string
    try:
        b = a.decode("utf-8")
    except:
        # eh um numero
        return a
    # tenta converter para um inteiro
    try:
        return int(b)
    except:
        # eh um atributo nominal
        if b == 'Yes':
            return 1
        if b == 'No':
            return 0
        return b


# Banido
# def ml_knn(X_train, y_train, X_test):
#     print(X_train)

#     X_train_matrix = scipy.sparse.csr_matrix(X_train.values)
#     y_train_matrix = scipy.sparse.csr_matrix(y_train.values)

#     mlknn = MLkNN(k=5)

#     print(X_train.to_numpy())
#     # train
#     # no fits???
#     mlknn.fit(X=X_train.to_numpy(), y=y_train.to_numpy())

#     # predict
#     predictions = mlknn.predict(X_test)


# def ml_knn_grid_search(X, y):
#     parameters = {'k': range(1, 3), 's': [0.5, 0.7, 1.0]}
#     score = 'f1_macro'

#     clf = GridSearchCV(MLkNN(), parameters, scoring=score)
#     clf.fit(X, y)

#     print(clf.best_params_, clf.best_score_)


def label_powerset(X_train, X_test, Y_train, Y_test):
    lp = LabelPowerset(RandomForestClassifier())
    lp.fit(X_train, Y_train)

    pred = lp.predict(X_test)
    accuracy_score(Y_test, pred)


def binary_relevance(X_train, y_train):
    classifier = BinaryRelevance(
        classifier=SVC(),
        require_dense=[False, True]
    )

    # train
    classifier.fit(X_train, y_train)

    # predict
    predictions = classifier.predict(X_test)


for i in range(len(datasetsName)):
    # Carregando o treino
    # dt, mt = scipy.io.arff.loadarff(f'datasets/{datasetsName[i][0]}/{datasetsName[i][0]}-train.arff')
    data_train[i], meta_train[i] = scipy.io.arff.loadarff(
        f'datasets/{datasetsName[i][0]}/{datasetsName[i][0]}-train.arff')
    X_train[i] = pd.DataFrame(data_train[i])

    # Carregando o teste
    data_test[i], meta_test[i] = scipy.io.arff.loadarff(
        f'datasets/{datasetsName[i][0]}/{datasetsName[i][0]}-test.arff')
    X_test[i] = pd.DataFrame(data_test[i])

    X_test[i] = X_test[i].applymap(convert)
    X_train[i] = X_train[i].applymap(convert)

    # Separando o Y do treino
    Y_train[i] = X_train[i].iloc[:, -datasetsName[i][1]:]
    X_train[i].drop(columns=list(Y_train[i].columns), inplace=True)

    # Separando o Y do teste
    Y_test[i] = X_test[i].iloc[:, -datasetsName[i][1]:]
    X_test[i].drop(columns=list(Y_test[i].columns), inplace=True)

print('amogus')
ml_knn(X_train[0], Y_train[0], X_test[0])
print(X_train[2])
