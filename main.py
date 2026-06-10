import pygame
import random
import pyttsx3
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador, pausar
from recursos.trabalho import mostrar_nivel

limpar_tela()
motor = pyttsx3.init()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maior_pontuador()
pygame.init()

while True:
    nome = input("Nickname: ")
    if len(nome) > 0: 
        break
    else:
        print("Nome Inválido!")
        
tamanho = (1000,700)
pygame.display.set_caption("Cosmic Survivor")
icone  = pygame.image.load("bases/icone_espaco.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
branco = (255, 255, 255)
preto = (0, 0, 0)
segundos = 5

fundo = pygame.image.load("bases/background_space .png")
fundoDead = pygame.image.load("bases/morreu.png")
fundoStart = pygame.image.load("bases/background_space_start.jpeg")

nave = pygame.image.load("bases/spaceship.png")
nave = pygame.transform.scale(nave, (200,100))
asteroide = pygame.image.load("bases/asteroide.png")
asteroide = pygame.transform.scale(asteroide, (150,150))
lua = pygame.image.load("bases/moon.png")
lua = pygame.transform.scale(lua, (150,150))
naveSound = pygame.mixer.Sound("bases/spaceship_sound.mp3")
explosaoSound = pygame.mixer.Sound("bases/explosion.mp3")
pygame.mixer.music.load("bases/musica_star_wars.mp3")
fonteMenu = pygame.font.SysFont("comicsans",18)
fonte_start_nome = pygame.font.SysFont("comicsans",25)
fonteMenu_titulo = pygame.font.Font("bases/Orbitron-Font.ttf",70)
fonteMenu_titulo_dead = pygame.font.Font("bases/Orbitron-Font.ttf",70)
fonteMenu_titulo_dead.set_bold(True)

def jogar():
    fundoMov1 = 0
    fundoMov2 = 1129
    posicaoXPersona = 0
    posicaoYPersona = 60
    movimentoYPersona  = 0
    velocidadeMovPersona = 5
    posicaoXAsteroide = 870
    posicaoYAsteroide = 500
    velocidadeAsteroide = 2
    posicaoXlua = 400
    posicaoYlua = 300
    velocidadeLuaX = random.randint(-2, 2)
    velocidadeLuaY = random.randint(-2, 2)
    pontos = 0
    raio_sol = 40
    crescendo = True
    pygame.mixer.Sound.play(naveSound)
    pygame.mixer.music.play(-1)
    dificuldade = 20
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoYPersona = -velocidadeMovPersona
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                movimentoYPersona = velocidadeMovPersona
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
                movimentoYPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
                movimentoYPersona = 0
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pausar(tela, preto)
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                quit()
                      
        posicaoYPersona = posicaoYPersona + movimentoYPersona            
        if posicaoXPersona < 0 :
            posicaoXPersona = 0
        elif posicaoXPersona > 870:
            posicaoXPersona = 870
        if posicaoYPersona < 0 :
            posicaoYPersona = 0
        elif posicaoYPersona > 600:
            posicaoYPersona = 600

        if crescendo:
            raio_sol += 0.2
            if raio_sol >= 50:
                crescendo = False
        else:
            raio_sol -= 0.2
            if raio_sol <= 40:
                crescendo = True

        posicaoXlua += velocidadeLuaX
        posicaoYlua += velocidadeLuaY

        if posicaoXlua <= 0 or posicaoXlua >= 850:
          velocidadeLuaX *= -1

        if posicaoYlua <= 0 or posicaoYlua >= 550:
          velocidadeLuaY *= -1

        if random.randint(1, 60) == 1:
          velocidadeLuaX = random.choice([-2, -1, 1, 2])
          velocidadeLuaY = random.choice([-2, -1, 1, 2])
            
        posicaoXAsteroide = posicaoXAsteroide - velocidadeAsteroide
        if posicaoXAsteroide < -125:
            pygame.mixer.Sound.play(naveSound)
            posicaoXAsteroide = 800
            pontos = pontos + 1
            velocidadeAsteroide = velocidadeAsteroide + 1
            posicaoYAsteroide = random.randint(0,600)
            
                            
        tela.fill(branco)
        tela.blit(fundo, (fundoMov1,0) )
        tela.blit(fundo, (fundoMov2,0) )
        fundoMov1 -= 1
        fundoMov2 -= 1
        if fundoMov1 <= -1129:
            fundoMov1 = 1129
        elif fundoMov2 <= -1129:
            fundoMov2 = 1129
        
        
        tela.blit(nave, (posicaoXPersona,posicaoYPersona))
        tela.blit(lua, (posicaoXlua, posicaoYlua))
        tela.blit( asteroide, (posicaoXAsteroide, posicaoYAsteroide) )
        texto = fonteMenu.render("Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (700,15))
        texto_press_space = fonteMenu.render("- Press Space to Pause Game", True, branco)
        tela.blit(texto_press_space, (360,630))
        pygame.draw.circle(tela, (255, 255, 0), (1000, 20), int(raio_sol))
        mostrar_nivel(tela, fonteMenu, velocidadeAsteroide)
            
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+200))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+100))
        pixelsAsteroideX = list(range(posicaoXAsteroide, posicaoXAsteroide + 150))
        pixelsAsteroideY = list(range(posicaoYAsteroide, posicaoYAsteroide + 150))
        if  len( list( set(pixelsAsteroideY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsAsteroideX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                escreverDados(nome, pontos)
                dead()
                
            else:
                print("Ainda Vivo, mas por pouco!")
        else:
            print("Ainda Vivo")
        
        
        pygame.display.update()
        relogio.tick(60)

def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    larguraButtonStart = 150
    alturaButtonStart  = 40
    larguraButtonQuit = 150
    alturaButtonQuit  = 40
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit  = 35

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                # Verifica se o clique foi dentro do retângulo
                if startButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()
                if quitButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonQuit = 150
                    alturaButtonQuit  = 40
                    quit()
            
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        startButton = pygame.draw.rect(tela, branco, (280,560, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (300,565))
        
        quitButton = pygame.draw.rect(tela, branco, (580,560, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (600,565))
        cosmic_survivor = fonteMenu_titulo_dead.render("MISSION FAILED", True, branco)
        tela.blit(cosmic_survivor, (100, 300))
        texto_dead = fonteMenu.render(f"The Best - {nome_maior}",True, branco)
        tela.blit(texto_dead, (700,15))
        
        pygame.display.update()
        relogio.tick(60)



def start():
    larguraButtonStart = 150
    alturaButtonStart  = 40
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                # Verifica se o clique foi dentro do retângulo
                if startButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()
            
        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        startButton = pygame.draw.rect(tela, branco, (400,570, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (420,575))
        
        texto = fonteMenu.render(f"The Best - {nome_maior} - {maior_pontos} - { dataJogada} ", True, branco)
        tela.blit(texto, (480,15))
        cosmic_survivor = fonteMenu_titulo.render("COSMIC SURVIVOR", True, branco)
        tela.blit(cosmic_survivor, (100, 200))
        cosmic_survivor = fonteMenu.render("Use as setas UP e DOWN para controlar a nave.", True, branco)
        tela.blit(cosmic_survivor, (260, 350))
        cosmic_survivor = fonteMenu.render("Desvie dos asteroides para ganhar pontos.", True, branco)
        tela.blit(cosmic_survivor, (300, 390))
        cosmic_survivor = fonteMenu.render("Quanto mais pontos, mais rápido o jogo fica.", True, branco)
        tela.blit(cosmic_survivor, (280, 430))
        cosmic_survivor = fonteMenu.render("Tente sobreviver e bater o recorde!", True, branco)
        tela.blit(cosmic_survivor, (320, 470))
        cosmic_survivor = fonte_start_nome.render(f"Seja bem vindo(a), {nome}!", True, branco)
        tela.blit(cosmic_survivor, (330, 300))
        motor.say(f"Seja bem vindo, {nome}!")
        motor.runAndWait()
        

        pygame.display.update()
        relogio.tick(60)
           
start() # estive aqui
