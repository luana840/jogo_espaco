import pygame

def mostrar_nivel(tela, fonte, velocidade):
    texto = fonte.render(f"Nivel: {velocidade-1}", True, (255,255,255))
    tela.blit(texto, (700, 40))