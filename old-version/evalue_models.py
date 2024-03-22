from src import rf
import pandas as pd

def avaliando_modelo(dataset:str,output_name:str)->None:
    """
    Com base no dataset passado em formato de excel, gera um excel de saida contendo os resultados obtidos ao treinar o modelo em diferentes senários.

    Args:
        dataset::str: Nome do dataset.xlsx contendo os dados usados para o modelo.
        output_name::str: Nome do arquivo de saida .xlsx contendo os resultos gerados a partir dos experimentos no dataset
        
    Return:
        None
    """
    lista_dados = []

    colunas = ['test_size','n_estimators','Acurácia','Precisão','Recall', 'F1-Score','Kappa']

    for test_size in range(10,40,10):
        for n_estimators in range(100,1100,100):
            
            model,acuracia, precision, recall, score, kappa = rf(test_size=test_size/100,n_estimators=n_estimators,excel_file=f'{dataset}')
            
            del model

            lista_dados.append([f'{(test_size/100):.1f}',n_estimators,acuracia,precision,recall,score, kappa])

            print(f'\n Teste usando {test_size} & {n_estimators} Realizado!')


    df = pd.DataFrame(data=lista_dados,columns=colunas)
    df.to_csv(output_name, index=False)