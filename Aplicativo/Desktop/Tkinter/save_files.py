from pandas import DataFrame

def export(df: DataFrame,mode:str,output_filename)->None:
    """
    Processa uma página de imagens FAMACHA e salva o resultado no formato escolhido pelo usuário. 
    Opções válidas para mode [csv, excel, json]

    Args:
        df::DataFrame: Dataframe pandas com os dados processados pelo classificador
        output_filename::str: Nome e caminho de saida para o arquivo que será gerado.
        mode::str: Palavra chave que define como serão salvos os dados processados [csv,excel,json].

    Return:
        None
    """
        
    match mode.lower():
        case 'csv':
            df.to_csv(output_filename+'.csv',index=False)
        
        case 'excel':
            df.to_excel(output_filename+'.xlsx',index=False)
        
        case 'json':
            df.to_json(output_filename+'.json',orient='records')
