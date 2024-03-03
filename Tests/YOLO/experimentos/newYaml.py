def yaml_file(path:str,train_dir:str,valid_dir:str,test_dir:str,nc:int, names:list, fname:str = "dados")->None:
    """
    Recebe a estrutura de um arquivo .yaml e cria um arquivo .yaml
    baseado nos valores passado.

    
    Parâmetros:
        path::str: string contendo o diretório raiz do dataset
        train_dir::str: string contendo o diretório da pasta com os dados de treino
        valid_dir::str: string contendo o diretório da pasta com os dados de validação
        test_dir::str: string contendo o diretório da pasta com os dados de teste
        nc::int: número total de classes que estamos trabalhando
        names::list: lista contendo strings refernetes a classes que estamos identificando
        fname::str: nome do arquivo que será gerado ao final da função 
        
    """
    import ruamel.yaml

    # Dados a serem adicionados ao arquivo YAML


    # Nome do arquivo YAML
    
    dic = {
        "path": path,
        "train": train_dir,
        "val": valid_dir,
        "test": test_dir,
        
        "nc": nc,
        "names": names}


    # Crie um objeto YAML
    yaml = ruamel.yaml.YAML()


    # Escreva os dic no arquivo YAML
    with open(fname, 'w') as arquivo:
        yaml.dump(dic, arquivo)

    print(f'\nDados foram gravados no arquivo {fname}')
