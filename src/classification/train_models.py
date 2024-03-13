from pandas import read_csv, read_json
from pickle import dump
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    f1_score,
    recall_score,
    cohen_kappa_score,
)
from pandas import DataFrame
from os.path import basename,splitext, exists, join

def File2df(file:str="dataset.csv")->DataFrame:
    """
    Carrega um dataset no formato DataFrame Pandas
    
    Args:
        file::str: Caminho de acesso para o dataset que será carregado
        
    Return:
        df::DataFrame : DataFrame gerado após o carregamento do arquivo
    """
    ext = splitext(basename(file))[-1]
    print(ext)
    
    match ext:
        case ".csv":
            df = read_csv(file)
        
        case ".json":
            df = read_json(file)
            
    return df
    

def Rf(df: DataFrame, test_size:float=0.1, n_estimators:int=100)-> tuple:
    """
    Realiza o treinamento de um modelo para um classficador RandomForest
    Retorna o modelo e o calculo de suas principais métricas:
    a acurácia (que expressa a precisão das previsões),
    a precisão (indicando a proporção de previsões positivas corretas), 
    o recall (que representa a capacidade do modelo de identificar corretamente instâncias positivas), 
    o F1-score (uma média harmônica entre precisão e recall) 
    e o coeficiente Kappa de Cohen (uma medida que avalia a concordância entre as previsões do modelo e os valores reais, ajustada para o acaso).

    Args:
        df::DataFrame: DataFrame contendo as caracteristicas dos dados que serão usadas para treinar o modelo
        test_size::float: Quantidade de dados destinados para os testes, onde o restante será destinado para treino.
        n_estimators::int: Número de estimadores (árvores de decisão) que serão utilizados no modelo de RandomForest.

    Returns:
        model, accuracy, precision, recall, f1, kappa ::tuple: Modelo e suas métricas 
 
    """

    # Seleciona colunas relevantes para análise
    selected_columns = [
        'Mean_R',
        'Mean_G',
        'Mean_B',
        'Median_R',
        'Median_G',
        'Median_B',
        'Std_R',
        'Std_G',
        'Std_B'
    ]

    features = df[selected_columns]
    target = df['FAMACHA']

    # Divide os dados em conjuntos de treino e teste
    train_data, test_data, train_target, test_target = train_test_split(
        features, target, test_size=test_size, random_state=0
    )

    model = RF(
        n_estimators=n_estimators,
        n_jobs=-1,
        random_state=0,
        max_depth=8,
        max_features=4,
        bootstrap=True,
    )
    
    model.fit(train_data, train_target)
    predictions = model.predict(test_data)

    accuracy = round(accuracy_score(test_target, predictions) * 100,2)
    precision = round(precision_score(test_target, predictions) * 100,2)
    recall = round(recall_score(test_target, predictions) * 100,2)
    f1 = round(f1_score(test_target, predictions) * 100,2)
    kappa = round(cohen_kappa_score(test_target, predictions) * 100,2)

    return model, accuracy, precision, recall, f1, kappa

from sklearn.svm import SVC

def SVM(df: DataFrame, test_size:float=0.1)-> tuple:
    selected_columns = [
        'Mean_R',
        'Mean_G',
        'Mean_B',
        'Median_R',
        'Median_G',
        'Median_B',
        'Std_R',
        'Std_G',
        'Std_B'
    ]

    features = df[selected_columns]
    target = df['FAMACHA']

    # Divide os dados em conjuntos de treino e teste
    train_data, test_data, train_target, test_target = train_test_split(
        features, target, test_size=test_size, random_state=0)
    
    model = SVC(kernel='rbf', random_state=0)  # Kernel pode ser alterado conforme necessário
    model.fit(train_data, train_target)
    predictions = model.predict(test_data)

    accuracy = round(accuracy_score(test_target, predictions) * 100,2)
    precision = round(precision_score(test_target, predictions) * 100,2)
    recall = round(recall_score(test_target, predictions) * 100,2)
    f1 = round(f1_score(test_target, predictions) * 100,2)
    kappa = round(cohen_kappa_score(test_target, predictions) * 100,2)

    return model, accuracy, precision, recall, f1, kappa

from sklearn.neural_network import MLPClassifier

def MLP(df: DataFrame, test_size:float=0.1)-> tuple:
    selected_columns = [
        'Mean_R',
        'Mean_G',
        'Mean_B',
        'Median_R',
        'Median_G',
        'Median_B',
        'Std_R',
        'Std_G',
        'Std_B'
    ]

    features = df[selected_columns]
    target = df['FAMACHA']

    # Divide os dados em conjuntos de treino e teste
    train_data, test_data, train_target, test_target = train_test_split(
        features, target, test_size=test_size, random_state=0
    )
    # Resto do seu código permanece igual, exceto pelo modelo a ser treinado
    model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=0)
    model.fit(train_data, train_target)
    predictions = model.predict(test_data)

    accuracy = round(accuracy_score(test_target, predictions) * 100,2)
    precision = round(precision_score(test_target, predictions) * 100,2)
    recall = round(recall_score(test_target, predictions) * 100,2)
    f1 = round(f1_score(test_target, predictions) * 100,2)
    kappa = round(cohen_kappa_score(test_target, predictions) * 100,2)

    return model, accuracy, precision, recall, f1, kappa
    
from sklearn.ensemble import GradientBoostingClassifier

def GBM(df: DataFrame, test_size:float=0.1)-> tuple:
    selected_columns = [
        'Mean_R',
        'Mean_G',
        'Mean_B',
        'Median_R',
        'Median_G',
        'Median_B',
        'Std_R',
        'Std_G',
        'Std_B'
    ]

    features = df[selected_columns]
    target = df['FAMACHA']

    # Divide os dados em conjuntos de treino e teste
    train_data, test_data, train_target, test_target = train_test_split(
        features, target, test_size=test_size, random_state=0
    )
    model = GradientBoostingClassifier(random_state=0)
    model.fit(train_data, train_target)
    predictions = model.predict(test_data)

    accuracy = round(accuracy_score(test_target, predictions) * 100,2)
    precision = round(precision_score(test_target, predictions) * 100,2)
    recall = round(recall_score(test_target, predictions) * 100,2)
    f1 = round(f1_score(test_target, predictions) * 100,2)
    kappa = round(cohen_kappa_score(test_target, predictions) * 100,2)

    return model, accuracy, precision, recall, f1, kappa

from sklearn.neighbors import KNeighborsClassifier

def KNN(df: DataFrame, test_size:float=0.1)-> tuple:
    selected_columns = [
        'Mean_R',
        'Mean_G',
        'Mean_B',
        'Median_R',
        'Median_G',
        'Median_B',
        'Std_R',
        'Std_G',
        'Std_B'
    ]

    features = df[selected_columns]
    target = df['FAMACHA']

    # Divide os dados em conjuntos de treino e teste
    train_data, test_data, train_target, test_target = train_test_split(
        features, target, test_size=test_size, random_state=0
    )
    model = KNeighborsClassifier()
    model.fit(train_data, train_target)
    predictions = model.predict(test_data)

    accuracy = round(accuracy_score(test_target, predictions) * 100,2)
    precision = round(precision_score(test_target, predictions) * 100,2)
    recall = round(recall_score(test_target, predictions) * 100,2)
    f1 = round(f1_score(test_target, predictions) * 100,2)
    kappa = round(cohen_kappa_score(test_target, predictions) * 100,2)

    return model, accuracy, precision, recall, f1, kappa
    
# Exemplo de CNN usando Keras com TensorFlow backend
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

"""
def CNN(df: DataFrame, test_size:float=0.1)-> tuple:
    # Seus dados precisam estar em um formato adequado para CNNs (ex: imagens)
    # Você pode precisar adaptar seu DataFrame para se adequar a este modelo
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(altura, largura, canais)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    # Treine seu modelo com os dados e retorne as métricas
"""    


def Best_rf(df: DataFrame, save_results: str = '', )->RF:
    """
    Obtem o melhor resultado do modelo RandomForest calculado com base na melhor combinação dos parâmetros (testsize, n_estimators) 
    Gera um arquivo .csv contendo todos os parâmetros testados
    o nome do csv aponta para a linha do melhor resultado

    Args:
       df::DataFrame: DataFrame contendo as caracteristicas dos dados que serão usadas para treinar o modelo
       save_results::str: Caminho para salvar o dataset com os resultados do modelo, onde caso seja passado um caminho valido, é gerado um csv com os resultados do processamento.
        
    Return:
        best::RF: Melhor modelo gerado apartir do treinamento
    """
    lista_dados = []

    colunas = ['test_size','n_estimators','Acurácia','Precisão','Recall', 'F1-Score','Kappa']
    
    #Guardando o melhor modelo, somatório das metricas e linha no dataset corresponde contendo a avaliação individuas das metricas juntamente com os parâmetros
    best = None
    metrics = 0
    idx = -1
    
    row = -1
    for test_size in range(10,40,10):
        for n_estimators in range(100,1100,100):
            
            row +=1
            
            model,acuracia, precision, recall, f1, kappa = Rf(df,test_size=test_size/100,n_estimators=n_estimators)
            
            result = acuracia + precision + recall + f1 + kappa
            
            if result > metrics:
                metrics = result
                best = model
                idx = row
                
            
            lista_dados.append([f'{(test_size/100):.1f}',n_estimators,acuracia,precision,recall,f1, kappa])

            print(f'\n Teste usando {test_size} & {n_estimators} Realizado!')

    if save_results != '' and exists(save_results):
        df = DataFrame(data=lista_dados,columns=colunas)
        df.to_csv(join(save_results,f"best in row {idx}.csv"), index=False)
    
    return best


def Save_model(model:RF, model_name:str)->None:
    """
    Salva um modelo RandomForestClassifer em um arquivo.pkl 
    
    Args:
        model::RF: Modelo que sera salvo
        model_name::str: Nome do arquivo que será gerado
        
    Return:
        None
    """ 

    with open(f'{model_name}.pkl', 'wb') as file:
        dump(model, file)
            

if __name__ == '__main__':
    # Avalia o modelo com o arquivo de dados 'FAMACHA_SEGMENTADA'
    model, accuracy, precision, recall, f1, kappa = Rf('FAMACHA_SEGMENTADA')

    # Imprime as métricas de avaliação
    print('Acurácia = ', accuracy)
    print('Precisão = ', precision)
    print('Recall = ', recall)
    print('F1-Score = ', f1)
    print('Kappa = ', kappa)
