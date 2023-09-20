import pandas as pd



def read_excel(excel_file="planilha.xlsx"):
    """
    Lê um arquivo excel e converte para um dataFrame pandas
    Retorno o dataFrame lido
    """
    df = pd.read_excel(excel_file)

    return df

def df_excel(df, excel_file="Resultado_Modelo.xlsx"):
    df.to_excel(excel_file, index=False)

