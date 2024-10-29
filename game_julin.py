"""
Universidade de Brasília
Institudo de Ciências Exatas
Departamento de Ciência da Computação
Algoritmos e Programação de Computadores - 2/2023
Turma: Prof. Carla Castanho e Prof. Frank Ned

Aluno(a): Júlio César de Souza Lima
Matrícula: 232009530

Projeto Final - Parte 1
Descrição:
"""




import pygame
from pygame.locals import *
import random
import sys

pygame.init()

def jogo():
    

    largura_jogo = 800
    altura_jogo = 200
    x = altura_jogo/2
    y = altura_jogo/2

    pontos = 0
    fonte = pygame.font.SysFont("calibri", 20, True, True)
    combutivel = 400
    consumo_combustivel = 1
    mais_combustivel = 40

    pygame.font.init()
    fonte_combustivel = pygame.font.SysFont("calibri", 20, True, True)


    tela1 = pygame.display.set_mode((largura_jogo, altura_jogo))
    pygame.display.set_caption("Mate ou Morra")
    fps = pygame.time.Clock()

    ret_vermelhos = []
    geracao_ret_vermelhos = 10
    ret_azuis = []
    geracao_ret_azuis = 15

    tiro_ativo = False
    tiro_x = 0
    tiro_y = 0

    jogando = True
    while True:
        if jogando:
            fps.tick(30)
            tela1.fill((0, 0, 0))
            mensagem = f"Pontos: {pontos}"
            texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
            mensagem1 = f"Combustível: {combutivel}"
            texto_formatado1 = fonte_combustivel.render(mensagem1, True, (255, 255, 255))
            tela1.blit(texto_formatado1, (10, 10))
            ret_verde = pygame.draw.rect(tela1, (0, 255, 0), (50, y, 10, 10))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_x:
                        tiro_ativo = True
                        tiro_x = 50
                        tiro_y = y
                '''
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        y = y - 10
                    if event.key == K_s:
                        y = y + 10'''
            if pygame.key.get_pressed()[K_w]:
                y = max(0, y - 10)
            if pygame.key.get_pressed()[K_s]:
                y = min(altura_jogo - 10, y + 10)
            
            combutivel -= consumo_combustivel
            if pygame.key.get_pressed()[K_w]:
                combutivel -= 2
            if pygame.key.get_pressed()[K_s]:
                combutivel -= 2
            if pygame.key.get_pressed()[K_x]:
                combutivel -= 3
            if combutivel < 0:
                combutivel = 0
                print("ACABOU A GASOSA")
                pygame.quit()
                exit()

            if pygame.time.get_ticks() % geracao_ret_vermelhos == 0:
                ret_vermelho = pygame.Rect(largura_jogo, random.randint(0, altura_jogo - 10), 10, 10)
                ret_vermelhos.append(ret_vermelho)
                

            for ret_vermelho in ret_vermelhos:
                ret_vermelho.x -= 5

                pygame.draw.rect(tela1, (255, 0, 0), ret_vermelho)

                if ret_vermelho.right < 0:
                    ret_vermelhos.remove(ret_vermelho)
                
                if tiro_ativo and ret_vermelho.colliderect(pygame.Rect(tiro_x, tiro_y, 10, 10)):
                    
                    ret_vermelhos.remove(ret_vermelho)
                    pontos = pontos + 50
            
                if ret_verde.colliderect(ret_vermelho):
                    
                    
                    jogando = False

            if pygame.time.get_ticks() % geracao_ret_azuis == 0:
                ret_azul = pygame.Rect(largura_jogo, random.randint(0, altura_jogo - 10), 10, 10)
                ret_azuis.append(ret_azul)

            for ret_azul in ret_azuis:
                ret_azul.x -= 5

                pygame.draw.rect(tela1, (0, 0, 255), ret_azul)

                if ret_azul.right < 0:
                    ret_azuis.remove(ret_azul)

                if ret_verde.colliderect(ret_azul):
                    ret_azuis.remove(ret_azul)

                if ret_verde.colliderect(ret_azul):
                    
                    combutivel += mais_combustivel

            if tiro_ativo:
                tiro_x += 10
                pygame.draw.rect(tela1, (0, 128, 0), (tiro_x, tiro_y, 10, 10))

                if tiro_x > largura_jogo:
                    tiro_ativo = False

            
            tela1.blit(texto_formatado, (650,10))
            pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        tela_opcoes()
            tela_final1()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mate ou Morra')

cor_fundo = (255, 255, 255)
cor_linha = (0, 0, 0)

tamanho_celula = largura // 135

fonte = pygame.font.Font(None, 36)

def desenhar_grid():
    tela.fill(cor_fundo)

    for linha in range(10):
        for coluna in range(135):
            pygame.draw.rect(tela, cor_linha, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula), 1)

    pygame.display.flip()

def exibir_texto(texto, cor, posicao):
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, posicao)

def tela_boas_vindas():
    tela.fill(cor_fundo)
    exibir_texto('Bem-vindo ao Meu Jogo', (0, 0, 0), (250, 250))
    exibir_texto('Pressione Enter para continuar', (0, 0, 0), (200, 300))
    pygame.display.flip()

def instrucoes():
    tela.fill(cor_fundo)
    exibir_texto('1 - Use W e S para se movimentar', (0, 0, 0), (100, 50))
    exibir_texto('2 - Mate os inimigos de vermelho para ganhar pontos', (0, 0, 0), (100, 100))
    exibir_texto('3 - Use X para atirar e acertar os inimigos', (0, 0, 0), (100, 150))
    exibir_texto('4 - Pegue o quadrado azul para ganhar 40 de combustível', (0, 0, 0), (100, 200))
    exibir_texto('5 - Se você colidir com o inimigo, você perde', (0, 0, 0), (100, 250))
    exibir_texto('6 - Se o seu combutível acabar, você perde', (0, 0, 0), (100, 300))
    exibir_texto('7 - Você gasta combustível quando se movimenta/atira', (0, 0, 0), (100, 350))
    exibir_texto('Pressione ENTER para voltar', (0, 0, 0), (100, 500))
    pygame.display.flip()

def tela_final1():
    tela.fill(cor_fundo)
    exibir_texto('GAME OVER', (0, 0, 0,), (100, 50))
    exibir_texto('Você se chocou com o inimigo', (0, 0, 0), (100, 100))
    exibir_texto('Pressione ENTER para voltar ao menu inicial', (0, 0, 0), (100, 150))
    pygame.display.flip()

def tela_opcoes():
    tela.fill(cor_fundo)
    exibir_texto('Escolha uma opção:', (0, 0, 0), (250, 200))
    exibir_texto('1 - Jogar', (0, 0, 0), (250, 250))
    exibir_texto('2 - Configurações', (0, 0, 0), (250, 300))
    exibir_texto('3 - Ranking', (0, 0, 0), (250, 350))
    exibir_texto('4 - Instruções', (0, 0, 0), (250, 400))
    exibir_texto('5 - Sair', (0, 0, 0), (250, 450))
    pygame.display.flip()


def main():
    tela_boas_vindas()
    

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    
                    tela_opcoes()
                    opcao = ''
                    while not opcao.isdigit() or int(opcao) not in range(1, 6):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                                opcao = '1'
                            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                                opcao = '2'
                            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                                opcao = '3'
                            elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                                opcao = '4'
                            elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                                opcao = '5'

                    if opcao == '1':
                        jogo()
                    elif opcao == '2':
                        print("Abrir configurações aqui.")
                    elif opcao == '3':
                        print("Mostrar o ranking aqui.")
                    elif opcao == '4':
                        instrucoes()
                        
                        pygame.display.flip()
                        esperando_tecla = True
                        while esperando_tecla:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                    esperando_tecla = False
                                    tela_opcoes()
                    elif opcao == '5':
                        pygame.quit()
                        exit()

                    tela_boas_vindas()

        pygame.display.update()

if __name__ == "__main__":
    main()