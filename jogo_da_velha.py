#Autor: Mateus Pereira Benvenutti
#Data: 05/09/2024
#Florianópolis, SC
#Bacharelado em Ciências da Computação
#Universidade do Vale do Itajaí
#Disciplina de Introdução à Python
#Professor: Evandro

#Este código visa construir um jogo da velha simples para o primeiro trabalho da disciplina.
#A ideia é tabular pequenas células num tabuleiro e ir preenchendo elas checando a input do usuário com a função if
#Provavelmente tem um jeito mais eficiente de fazer isso, mas acho que é o jeito que fica mais bonitinho no terminal
#(Mesmo assim a coluna C fica levemente mais separada das outras, o que me deixa bem frustrado.)

#O comando para a jogada segue mais ou menos uma notação de xadrez: primeiro a peça, depois coluna, depois linha.

#Essas são as strings que montam o tabuleiro e que checam se há vitória. As primeiras mudam conforme anda o jogo,
#as últimas são fixas. Poderia ter declarado uma lista fixa, mas fiquei preocupado que a comparação com as linhas
#que é feita depois desse erro por causa disso.
celA1 = '| |'
celA2 = '| |'
celA3 = '| |'
celB1 = '| |'
celB2 = '| |'
celB3 = '| |'
celC1 = '| |'
celC2 = '| |'
celC3 = '| |'
vitoriaX = ['|X|', '|X|', '|X|']
vitoriaO = ['|O|', '|O|', '|O|']

print('Jogo da Velha\nDigite seu símbolo (X ou O), a letra (coluna) e o número (linha) para marcar no tabuleiro. (Ex. ob2, xa3)\nDigite "SAIR" para sair.')

while True:

#Aqui começa o loop. A primeira coisa que ele faz é atualizar as listas que vão ser comparadas com vitoriaX e vitoriaO
#para imprimir a mensagem de vitória.
#Em pensei em tentar fazer uma forma do jogo indicar quando deu empate (deu velha), mas não achei nada que não fosse talvez
#quebrar outra coisa. Uma ideia que um amigo me deu foi definir o tamanho do loop para 9 iterações (número máximo de jogadas).
#Achei que isso fosse dar erro caso alguém marcasse errado e tivesse que remarcar, então escolhi fazer uma pergunta no final de
#cada jogo.

#Outra coisa que eu queria fazer mas não sei como é impedir que um jogador "marque por cima" do outro.

#Essa variável desenha o tabuleiro. Tem que ficar dentro do loop para se atualizar.
    tabuleiro = f'\t   A\t B\t C\n\t1 {celA1}\t{celB1}\t{celC1}\n\n\t2 {celA2}\t{celB2}\t{celC2}\n\n\t3 {celA3}\t{celB3}\t{celC3}'


#Eu fiquei com muitos problemas com essa parte e acabei pesquisando online e fui relembrado de que as listas não se atualizam
#sozinhas quando uma variável que foi declarada dentro delas sofre alteração. Quando a lista é declarada, ela faz um snapshot
#das variáveis. Por isso coloquei essa parte dentro do loop.
    checkLinha1 = [celA1, celB1, celC1]
    checkLinha2 = [celA2, celB2, celC2]
    checkLinha3 = [celA3, celB3, celC3]
    checkColunaA = [celA1, celA2, celA3]
    checkColunaB = [celB1, celB2, celB3]
    checkColunaC = [celC1, celC2, celC3]
    checkDiagEsq = [celA1, celB2, celC3]
    checkDiagDir = [celC1, celB2, celA3]

#Aqui declarei esta variável para não ficar enorme o código nas duas vezes que se checa por vitória.
    listaLinColDiag = [checkLinha1, checkLinha2, checkLinha3, checkColunaA, checkColunaB, checkColunaC, checkDiagDir, checkDiagEsq]
    allCels = [celA1, celA2, celA3, celB1, celB2, celB3, celC1, celC2, celC3]

#Checando se há vitória. Também imprime o tabuleiro final.
    if vitoriaX in listaLinColDiag:
        print(tabuleiro)
        print('X é o vencedor!')
        a = input("Jogar de novo?(s/n) ").lower()
        if a == 's':
            celA1 = celA2 = celA3 = celB1 = celB2 = celB3 = celC1 = celC2 = celC3 = '| |'
            continue
        else:
            break

    elif vitoriaO in listaLinColDiag:
        print(tabuleiro)
        print('O é o vencedor!')
        a = input("Jogar de novo?(s/n) ").lower()
        if a == 's':
            celA1 = celA2 = celA3 = celB1 = celB2 = celB3 = celC1 = celC2 = celC3 = '| |'
            continue
        else:
            break

    elif '| |' not in allCels: #checa se o tabuleiro está cheio (se deu velha)
        print(tabuleiro)
        print('Deu velha! :(')
        a = input("Jogar de novo?(s/n) ").lower()
        if a == 's':
            celA1 = celA2 = celA3 = celB1 = celB2 = celB3 = celC1 = celC2 = celC3 = '| |'
            continue
        else:
            break
#No fim de cada checagem, o programa pergunta se quer continuar jogando. Se diz que sim, ele "apaga" todas as marcações no
#tabuleiro e retorna para o começo do loop

    else:
        print(tabuleiro)
        jogada = input("Jogada: ").upper() #coloca o input em uppercase para padronizar mesmo se o usuário usar lowercase

#if dentro de if para computar as jogadas e desenhar elas no tabuleiro

        if jogada == 'XA1' and celA1 == '| |':
            celA1 = '|X|'
        elif jogada == 'OA1' and celA1 == '| |':
            celA1 = '|O|'
        elif jogada == 'XB1' and celB1 == '| |':
            celB1 = '|X|'
        elif jogada == 'OB1' and celB1 == '| |':
            celB1 = '|O|'
        elif jogada == 'XC1' and celC1 == '| |':
            celC1 = '|X|'
        elif jogada == 'OC1' and celC1 == '| |':
            celC1 = '|O|'
        elif jogada == 'XA2' and celA2 == '| |':
            celA2 = '|X|'
        elif jogada == 'OA2' and celA2 == '| |':
            celA2 = '|O|'
        elif jogada == 'XB2' and celB2 == '| |':
            celB2 = '|X|'
        elif jogada == 'OB2' and celB2 == '| |':
            celB2 = '|O|'
        elif jogada == 'XC2' and celC2 == '| |':
            celC2 = '|X|'
        elif jogada == 'OC2' and celC2 == '| |':
            celC2 = '|O|'
        elif jogada == 'XA3' and celA3 == '| |':
            celA3 = '|X|'
        elif jogada == 'OA3' and celA3 == '| |':
            celA3 = '|O|'
        elif jogada == 'XB3' and celB3 == '| |':
            celB3 = '|X|'
        elif jogada == 'OB3' and celB3 == '| |':
            celB3 = '|O|'
        elif jogada == 'XC3' and celC3 == '| |':
            celC3 = '|X|'
        elif jogada == 'OC3' and celC3 == '| |':
            celC3 = '|O|'
        elif jogada == 'SAIR':
            break

        #manda o usuário usar o programa direito caso ele só digite qualquer coisa
        else:
            print('Digite uma jogada válida. Seu símbolo, letra e depois número (nesta ordem. Ex: ob2).\nO espaço deve estar vazio.\nDigite "SAIR" para sair.')

input("Obrigado por jogar! ") #essa mensagem é um input pro programa não fechar abruptamente no fim do jogo.
