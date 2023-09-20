from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score, f1_score, recall_score, cohen_kappa_score


from .excel_access_04 import read_excel

def test_model(excel_file,test_size=0.1, n_estimators=100):

    df = read_excel(f'{excel_file}')

    #Filtragem das colunas que usaremos, no caso todos exceto o nome da imagem que não será útil
    colunas = ['Media_Canal_R','Media_Canal_G','Media_Canal_B','Mediana_Canal_R','Mediana_Canal_G','Mediana_Canal_B','Desvio_Canal_R','Desvio_Canal_G','Desvio_Canal_B']

    #usaremos x para procurar um padrão nos dados visando encontrar o Grau FAMACHA localizando nesse padrão
    x = df[colunas]

    # y é nosso 'target' ou objetivo, logo todos os resultados de x visam encontrar a resposta certa em y
    y = df['Vermifuga']

    
    x_treino, x_teste, y_treino,y_teste = train_test_split(x,y,test_size=test_size,random_state=0)

    modelo = RandomForestClassifier(n_estimators=n_estimators,n_jobs=-1,random_state=0, max_depth=8, max_features=4,bootstrap=True)

    modelo.fit(x_treino,y_treino)

    #realizando a predição do modelo com alguns testes
    y_pred = modelo.predict(x_teste)

    acuracia = (f'{(accuracy_score(y_teste, y_pred) * 100):.2f}')
    precision = (f'{(precision_score(y_teste, y_pred) * 100):.2f}')
    recall = (f'{(recall_score(y_teste, y_pred) * 100):.2f}')
    score = (f'{(f1_score(y_teste, y_pred)* 100 ):.2f}')
    kappa =  (f'{(cohen_kappa_score(y_teste, y_pred)* 100 ):.2f}')


    return acuracia, precision, recall, score, kappa
    
def create(excel_file,test_size=0.1, n_estimators=100):
    df = read_excel(f"{excel_file}")

    colunas = ['Media_Canal_R','Media_Canal_G','Media_Canal_B','Mediana_Canal_R','Mediana_Canal_G','Mediana_Canal_B','Desvio_Canal_R','Desvio_Canal_G','Desvio_Canal_B']

    x = df[colunas]
    y = df['Vermifuga']
    
    x_treino, x_teste, y_treino,y_teste = train_test_split(x,y,test_size=test_size,random_state=0)

    modelo = RandomForestClassifier(n_estimators=n_estimators,n_jobs=-1,random_state=0, max_depth=8, max_features=4,bootstrap=True)

    modelo.fit(x_treino,y_treino)

    return modelo

def save(model,name_model='Modelo'):
    
    import pickle

    # salvar o modelo treinado em um arquivo pkl
    with open(f'{name_model}.pkl', 'wb') as arquivo:
        pickle.dump(model, arquivo)


if __name__ == '__main__':
    acuracia, precision, recall, score,kappa = test_model('FAMACHA_SEGMENTADA')

    print('Acurácia = ',acuracia)
    print('Precisão = ', precision)
    print('Recall = ', recall)
    print('F1-Score = ', score)
    #kappa é mais sensivel a balanceamento
    print('Kappa = ', kappa)

