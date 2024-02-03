def menu():
    
    opc = input("\n\n[1] - Suadação\n[2] - Despedida\n[6] - Sair\n\nResposta: ")
    
    if opc.isnumeric():
        opc = int(opc)
        if(opc < 0 and opc > 2):
            opc = - 1
    else:
            opc = -2
    
    return opc



