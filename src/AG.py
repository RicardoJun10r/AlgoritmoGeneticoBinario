import math
import random
import sys

def funcao(x, y):
    return math.sqrt(x**3 + (2 * y)**4)

def fitness(individuo):
    z = funcao(individuo[0], individuo[1])

    if z == 0:
        return sys.maxsize

    return 1 / z

def gerarPopulacao(individuos: int):
    populacao = []
    for _ in range(individuos):
        populacao.append((random.randint(0,7), random.randint(0,7)))

    return populacao

def crossover(maisApto):
    resultado = [x[1] for x in maisApto]

    random.shuffle(maisApto)

    for i in range(len(maisApto) // 2):
        pai = maisApto[i][1]
        mae = maisApto[i+1][1]

        crianca1 = (
            pai[0] & mae[0],
            pai[1] & mae[1]
        )

        crianca2 = (
            pai[0] >> 1,
            mae[1] >> 1
        )

        resultado.append(crianca1)
        resultado.append(crianca2)

    return resultado


def algoritmoGenetico(tamanho_populacao, iteracoes):
    # inicialização da população
    population = gerarPopulacao(tamanho_populacao)
    maisAptoTodos = ()

    # épocas
    for iteracao in range(iteracoes):
        resultados = []

        # avaliação de cada individuo
        for individual in population:
            resultados.append((fitness(individual), individual))

        resultados.sort()
        resultados.reverse()

        maisAptoTodos = resultados[0]

        print(f'==== Generation {iteracao + 1} ====')
        print('Most fit: ', maisAptoTodos)

        # condição de parada
        if resultados[0][0] > 1:
            break

        # seleção de alguns individuos
        maisApto = resultados[:math.ceil(tamanho_populacao / 2)]

        # cross-over, mutação e concepção da nova geração
        population = crossover(maisApto)

    print(f'\n==== End of execution ====')
    print('Most fit of all: ', maisAptoTodos)


algoritmoGenetico(5, 20)