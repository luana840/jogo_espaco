import os, time, pygame
import json
from datetime import datetime

def limpar_tela():
    os.system("cls")
    
def aguarde(segundos):
    time.sleep(segundos)
    
def inicializarBancoDeDados():
    # r - read, w - write, a - append
    try:
        banco = open("base.atitus","r")
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("base.atitus","w")
    
def escreverDados(nome, pontos):
    # INI - inserindo no arquivo
    banco = open("base.atitus","r")
    dados = banco.read()
    banco.close()
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}
        
    data_br = datetime.now().strftime("%d/%m/%Y")
    dadosDict[nome] = (pontos, data_br)
    
    banco = open("base.atitus","w")
    banco.write(json.dumps(dadosDict))
    banco.close()
    
    # END - inserindo no arquivo
    
def maior_pontuador():
    banco = open("base.atitus","r")
    dados = banco.read()
    banco.close()
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

    nome_maior = None
    dataJogada =  None
    maior_pontos = -1

    for nome, info in dadosDict.items():

        pontos = info[0]
        
        if pontos > maior_pontos:
            maior_pontos = pontos
            nome_maior = nome
            dataJogada = info[1]            

    return nome_maior, maior_pontos, dataJogada

def pausar(tela, preto):
    branco_azulado = (235,235,255)
    fonteMenu = pygame.font.SysFont("bahnschrift", 115, bold = True)
    fonte_escrita = pygame.font.SysFont("bahnschrift", 20)

    texto = fonteMenu.render("PAUSE", True, branco_azulado)
    aperte_espaco = fonte_escrita.render("Aperte >space< novamente para voltar ao jogo", True, branco_azulado)
    pygame.draw.rect(tela, branco_azulado, (470, 180, 25, 120))
    pygame.draw.rect(tela, branco_azulado, (505, 180, 25, 120))
    

    pausado = True

    while pausado:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = False  # volta para o jogo

        tela.blit(texto, (300, 350))
        tela.blit(aperte_espaco, (290, 650))
        pygame.display.update()






        