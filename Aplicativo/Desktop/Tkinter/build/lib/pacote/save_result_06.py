from .excel_access_04 import df_excel

from .create_model_05 import test_model

import pandas as pd

def avaliando_modelo(excel_file_input='FAMACHA_SEGMENTADA.xlsx',excel_file_output='Resultados.xlsx'):
    lista_dados = []


    colunas = ['test_size','n_estimators','Acurácia','Precisão','Recall', 'F1-Score','Kappa']

    for test_size in range(10,40,10):
        for n_estimators in range(100,1100,100):
            

            acuracia, precision, recall, score, kappa = test_model(test_size=test_size/100,n_estimators=n_estimators,excel_file=f'{excel_file_input}')


            lista_dados.append([f'{(test_size/100):.1f}',n_estimators,acuracia,precision,recall,score, kappa])

            print(f'\n Teste usando {test_size} & {n_estimators} Realizado!')


    df = pd.DataFrame(data=lista_dados,columns=colunas)

    df_excel(df=df,excel_file=excel_file_output)