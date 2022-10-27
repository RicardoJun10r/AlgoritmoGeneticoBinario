import random as rd
import math as math
import matplotlib.pyplot as grafico

# função matemática do problema
def funcao(individuo):
  #aptidao
    valor = math.sqrt(individuo[0] * 3 + 2 * individuo[1] * 4)
    
    if(valor == 0):
        return -1
    
    return 1/valor

# Métdos de conversão de decimal para binário e vice-versa
def decimalParaBinario(numero):
    remstack = []

    if(numero == 0):
      return "000"
    while numero > 0:
        rem = numero % 2
        remstack.append(rem)
        numero = numero // 2

    binString = ""
    while len(remstack) != 0:
        binString = binString + str(remstack.pop())

    while(len(binString) < 3):
      binString = "0" + binString
      
    return binString

def binarioParaDecimal(numero_binario): 
    
    binario = int(numero_binario)
    
    decimal, i, n = 0, 0, 0
    while(binario != 0): 
        dec = binario % 10
        decimal = decimal + dec * pow(2, i) 
        binario = binario//10
        i += 1
    return decimal
#--------------------------------------------------

# Método para incializar a população
def criarPopulacao(tamPopulacao):

    populacao = []
    
    # a população é iniciada randomicamente com números entre 0 e 7
    for x in range(tamPopulacao):
        populacao.append((rd.randint(0,7),rd.randint(0,7)))

    return populacao

# Método para selecionar, através de sorteio de roleta, que sofrerão o crossover e mutação
def selecaoSorteio(populacao):

    selecionado = []

    sorteio = rd.sample(range(0, len(populacao)), len(populacao))
    teste = 0

    # Será selecionado dois individuos aleatoriamente

    while(teste != 2):
        TMP = []

        TMP.append(populacao[sorteio[0]])
        TMP.append(populacao[sorteio[1]])

        if(TMP[0][0] > TMP[1][0]):
            selecionado.append(TMP[0])
        else:
            selecionado.append(TMP[1])

        teste+=1
    
    # retornando os individuos que passarão pelo crossover e mutação
    return selecionado

# Função de cruzamento junto com mutação
def crossover(selecionados):

    # criando lista populacao que ira receber a nova geração
    populacao = []
    populacao.append(selecionados[0][1])
    populacao.append(selecionados[1][1])


    # O corte do cruzamento é feito randomizado
    corte = rd.randint(1,2)

    # Cruzamento com ponto de corte 2
    if(corte == 2):

        # primeiro par ordenado
        x = decimalParaBinario(populacao[0][0])
        pai1a = x[0:2]
        pai1b = x[2:3]

        y = decimalParaBinario(populacao[0][1])
        mae1a = y[0:2]
        mae1b = y[2:3]

        # segundo par ordenado
        x2 = decimalParaBinario(populacao[1][0])
        pai2a = x[0:2]
        pai2b = x[2:3]

        y2 = decimalParaBinario(populacao[1][1])
        mae2a = y2[0:2]
        mae2b = y2[2:3]

        # Fazendo permutação dos bits, criando a nova geração
        
        crianca1 = ( binarioParaDecimal(pai1a + pai2b), binarioParaDecimal(mae1a + mae2b) )

        crianca2 = ( binarioParaDecimal(pai2a + pai1b), binarioParaDecimal(mae2a + mae1b) )

        # Criando probabilidade da nova geração sofrer mutação
        mutacao = rd.randint(0, 100)

        if (mutacao <= 2):
            # A mutação, funciona, movimentando dois bits de cada criança para direita
            crianca1 = (crianca1[0] >> 2, crianca1[1] >> 2)
            crianca2 = (crianca2[0] >> 2, crianca2[1] >> 2)

        populacao.append(crianca1)
        populacao.append(crianca2)

    # Cruzamento com ponto de corte 1
    else:

        # primeiro par ordenado
        x = decimalParaBinario(populacao[0][0])
        pai1a = x[0:1]
        pai1b = x[1:3]

        y = decimalParaBinario(populacao[0][1])
        mae1a = y[0:1]
        mae1b = y[1:3]

        # segundo par ordenado
        x2 = decimalParaBinario(populacao[1][0])
        pai2a = x2[0:1]
        pai2b = x2[1:3]

        y2 = decimalParaBinario(populacao[1][1])
        mae2a = y2[0:1]
        mae2b = y2[1:3]

        # Fazendo permutação dos bits, criando a nova geração

        crianca1 = ( binarioParaDecimal(pai1a + pai2b), binarioParaDecimal(mae1a + mae2b) )

        crianca2 = ( binarioParaDecimal(pai2a + pai1b), binarioParaDecimal(mae2a + mae1b) )


        # Criando probabilidade da nova geração sofrer mutação
        mutacao = rd.randint(0, 100)

        if (mutacao <= 2):
            # A mutação, funciona, movimentando dois bits de cada criança para direita
            crianca1 = (crianca1[0] >> 2, crianca1[1] >> 2)
            crianca2 = (crianca2[0] >> 2, crianca2[1] >> 2)

        populacao.append(crianca1)
        populacao.append(crianca2)

    # retornando a lista da nova população 
    return populacao

def algoritmoGenetico(tamanho_populacao):

    epoca = 1
    maisAptos = []
    populacao = criarPopulacao(tamanho_populacao)

    # Loop principal do Algoritmo, ele irá parar quando o critério de parada ser atendido
    teste = False
    while(teste != True):
        resultado = []

        for individuo in populacao:
            resultado.append((funcao(individuo),individuo))

        # Ordendando a lista de resultados para pegar sempre os mais apto da iteração na primeira posição
        resultado.sort()
        maisAptos.append(resultado[0][0])

        # Condicao de parada
        if (resultado[0][0] == -1):
            teste = True
        
            # Criando gráfico com os valores dos individuos mais aptos das iterações
            grafico.plot(maisAptos)
            grafico.title("AG")
            grafico.show()
            #-----------------------


        # Mostrar interaçao e o resultado da geração
        print(f"Geração {epoca}")
        print(resultado[0][0], " : ", resultado[0][1])


        selecionados = selecaoSorteio(resultado)
        populacao = crossover(selecionados)
        epoca+=1

algoritmoGenetico(15)

#   Algoritmo Genético Passo-a-passo
#
#   1° Inicializar população
#
#   2° Selecionar individuos mais aptos ( SORTEIO )
#
#   3° Crossover, permutar os bits de dois individuos pais, utilizando dois diferentes pontos de cortes
#
#   4° Mutação, Trocar randomicamente um bit    
#
#   5° Critério de parada, se atendido, ele para, se não ele repete o passo 2
#