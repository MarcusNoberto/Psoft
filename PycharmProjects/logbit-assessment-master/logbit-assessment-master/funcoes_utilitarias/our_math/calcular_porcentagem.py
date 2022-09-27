def calcular_porcentagem(valor: float, total: float) -> float:
    '''
    Função simples que recebe um valor e um total e retorna a porcentagem.
    Por exemplo, você tem 37 e quer saber quantos % 37 é em 58, basta passar os dois para essa função.
    
    Nesse caso, ela lhe retornará 63,79, pois 37 é 63,79% de 58.
    '''

    porcentagem = ((valor * 100) / total if total != 0 else 0)
    return round(porcentagem, 2)
