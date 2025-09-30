import pygame
import os
import random

# --- CÓDIGO CORRIGIDO E DEFINITIVO ---


diretorio_base = os.path.dirname(os.path.abspath(__file__))
caminho_imgs = os.path.join(diretorio_base, 'imgs')


TELA_LARGURA = 500
TELA_ALTURA = 800

# Agora, carregue todas as imagens usando a variável 'caminho_imgs'
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join(caminho_imgs, 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join(caminho_imgs, 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(caminho_imgs, 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(caminho_imgs, 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(caminho_imgs, 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(caminho_imgs, 'bird3.png')))
]

# --- FONTES DO JOGO ---
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
### NOVO: Fontes para a tela de Game Over ###
FONTE_GAMEOVER = pygame.font.SysFont('arial', 80, bold=True)
FONTE_REINICIAR = pygame.font.SysFont('arial', 30)


class Passaro:
    IMGS = IMAGENS_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = self.velocidade * self.tempo + 1.5 * (self.tempo**2)

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        if deslocamento < 0 or self.y < self.altura + 50:
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))

def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()

### NOVO: Função para exibir a tela de Game Over ###
def tela_game_over(tela, pontos):
    # Desenha o texto "GAME OVER"
    texto_gameover = FONTE_GAMEOVER.render("GAME OVER", 1, (255, 0, 0)) # Vermelho
    pos_x_go = TELA_LARGURA/2 - texto_gameover.get_width()/2
    pos_y_go = TELA_ALTURA/2 - 100
    tela.blit(texto_gameover, (pos_x_go, pos_y_go))

    # Desenha o texto da pontuação final
    texto_pontos = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    pos_x_pts = TELA_LARGURA/2 - texto_pontos.get_width()/2
    pos_y_pts = TELA_ALTURA/2
    tela.blit(texto_pontos, (pos_x_pts, pos_y_pts))


    # Desenha o botão/texto para reiniciar
    texto_reiniciar = FONTE_REINICIAR.render("Pressione R para reiniciar", 1, (255, 255, 255))
    pos_x_re = TELA_LARGURA/2 - texto_reiniciar.get_width()/2
    pos_y_re = TELA_ALTURA/2 + 80
    tela.blit(texto_reiniciar, (pos_x_re, pos_y_re))

    pygame.display.update()

    # Loop que espera o jogador decidir o que fazer
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: # Se a tecla 'R' for pressionada
                    esperando = False # Sai do loop para reiniciar o jogo


### ALTERADO: A antiga função 'main' foi renomeada para 'rodar_jogo' ###
def rodar_jogo(tela):
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        # Mover as coisas no jogo
        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True

            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))

        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)

        ### NOVO: Condição de Fim de Jogo ###
        # Se a lista de pássaros estiver vazia, o jogo acabou.
        if len(passaros) == 0:
            rodando = False # Para o loop do jogo

        desenhar_tela(tela, passaros, canos, chao, pontos)

    # ### ALTERADO: Retorna a pontuação final para a função principal ###
    return pontos


### NOVO: A nova função 'main' que controla o fluxo do programa ###
def main():
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pygame.display.set_caption("Flappy Bird")

    while True: # Loop principal do programa
        pontos_finais = rodar_jogo(tela) # Inicia uma partida
        tela_game_over(tela, pontos_finais) # Quando a partida acaba, mostra a tela de Game Over


if __name__ == '__main__':

    main()
