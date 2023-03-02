''' 
----------------------------------------------------------------------
# Instituto Federal de Ciências e Tecnologia de Minas Gerais
# Marçal Henrique Moreira RA: 0026790
# Modelagem e Simulação - Professor Itagildo Garbazza
# 06/02/22
# Bambuí - MG
---------------------------------------------------------------------- 
'''

#Atividade Avaliativa
'''
Projeto Computacional "Bola na Urna"

Descrição:
* Em uma urna existem "n" bolas brancas idênticas. Ao se retirar uma bola, uma moeda justa é jogada e se cair cara, a bola é pintada de vermelho, senão, é pintada de preto. Depois, a bola é devolvida para a urna. Quando uma bola pintada de vermelho ou preto é retirada haverá 50% de chance dela ter sua cor trocada. Assim uma moeda justa é jogada e se cair cara, a bola vermelha será pintada de preto e vice-versa, e se cair coroa a bola volta a ser branca.

Dados de entrada:

* Quantidade de bolas na urna;
* Quantidade de sequências a serem realizadas.

Você deverá implementar esse jogo de forma a apresentar ao usuário todas as modificações que ocorrerem no jogo, passo a passo. Também deverá manter atualizada a quantidade de bolas dentro da urna, informando a quantidade por cor e a quantidade total.

Deverá ser enviado o código fonte e também o programa executável, em arquivos compactados separados.

Não será exigido nenhuma linguagem de programação específica, fiquem à vontade para utilizar aquela que melhor lhe agradem.

Data limite para entrega: 06 de fevereiro de 2022
'''
#---------------------------------------------------------------------
# bibliotecas
import random as rd


#Random da moeda
def jogar_moeda():
    moeda = rd.randint(0,1)
    if moeda == 0:
        print("A moeda foi jogada para cima, seu resultado foi -CARA-\n")
    else:
        print("A moeda foi jogada para cima, seu resultado foi -COROA-\n")
    return int(moeda)


# Função da Urna
def urna(total_bolas, total_jogadas):
    #preenchendo a urna vazia com bolas brancas
    vet_urna = []
    for i in range(0, total_bolas, 1):
        vet_urna.append("Bola Branca")
    print(f"Existe um total de {total_bolas} bolas brancas na caixa!!!\n")
    print("--------------------------------------------------------\n")

    
    
    #retirando uma bola da urna
    for i in range(0, total_jogadas, 1):
        aux = rd.randint(0,total_bolas-1)
        bola_retirada = vet_urna[aux]
        print(f"============ Rodada {i+1}!!! ============\n")
        print(f"Foi retirada uma {bola_retirada}!!!\n")



        #bola branca
        if(bola_retirada == "Bola Branca"):
            if(jogar_moeda() == 0):
                vet_urna[aux] = "Bola Vermelha"
                print("A Bola Branca retirada foi pintada de Vermelho!!!")
            else:
                vet_urna[aux] = "Bola Preta"
                print("A Bola Branca retirada foi pintada de Preto!!!")

        #bola vermelha
        if(bola_retirada == "Bola Vermelha"):
            if(jogar_moeda() == 0):
                vet_urna[aux] = "Bola Preta"
                print("A Bola Vermelha retirada foi pintada de Preto")
            else:
                vet_urna[aux] = "Bola Branca"
                print("A Bola Vermelha retirada foi pintada de Branco")
        
        #bola preta
        if(bola_retirada == "Bola Preta"):
            if(jogar_moeda() == 0):
                vet_urna[aux] = "Bola Vermelha"
                print("A Bola Preta retirada foi pintada de Vermelho")
            else:
                vet_urna[aux] = "Bola Branca"
                print("A Bola Preta retirada foi pintada de Branco")
        print(" ")
        print("A bola foi posta novamente na caixa!!!\n")
        
        #final da rodada
        #contagem da bola por rodada
        print("\n")
        print("== Final da rodada!!! ==\n")
        qtd_branca = 0
        qtd_vermelha = 0
        qtd_preta = 0
        for i in range(len(vet_urna)):
            if vet_urna[i] == "Bola Branca":
                qtd_branca += 1
            elif vet_urna[i] == "Bola Vermelha":
                qtd_vermelha += 1
            elif vet_urna[i] == "Bola Preta":
                qtd_preta += 1
        print(f"Existe na caixa, no momento:\n {qtd_branca} Bolas Brancas:\n {qtd_vermelha} Bolas Vermelhas:\n {qtd_preta} Bolas Pretas: \n Total de bolas: {total_bolas}\n")
        print("Bolas dentro da caixa: ")
        print(vet_urna)
        print("--------------------------------------------------------\n")
        
    
#Menu do jogo
print("--------------------- Bola na Urna ---------------------\n")
print("Explicação do Jogo: \n")
print("O jogo se inicia com uma certa quantidades de bolas brancas, em cada rodada uma bola é puxada da caixa, também é jogado uma moeda.") 
print("Se a bola for branca e o resultado da moeda for CARA, a bola é pintada de vermelho. Se a bola for branca e o resultado da moeda for COROA, a bola é pintada de preto.")
print("Se a bola retirada for vermelha e o resultado da moeda for CARA, a bola é pintada de preto. Se a bola for vermelha e o resultado da moeda for COROA, a bola é pintada de branco.")
print("Se a bola retirada for preta e o resultado da moeda for CARA, a bola é pintada de vermelho. Se a bola retirada for preta e o resultado da moeda for COROA, a bola é pintada de branca.\n")
print("--------------------------------------------------------\n")

print("Comece escolhendo a quantidade de bolas da caixa: ")
total_bolas = int(input())
print("--------------------------------------------------------\n")
print("Digite a quantidade de rodadas a ser jogada: ")
total_jogadas = int(input())
print("--------------------------------------------------------\n")

urna(total_bolas, total_jogadas)




