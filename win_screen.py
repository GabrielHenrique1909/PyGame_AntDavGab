import pygame
from os import path
from config import (IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT,
                    HIGH_SCORE_FILE, YELLOW, WHITE, FNT_DIR, INIT, WIN)
from assets import TIME_FONT, BTN_CLICK_SOUND
from sprites import BotaoRestartWin

def format_time_display(total_seconds):
    """Formata o tempo total em segundos para MM:SS."""
    if total_seconds is None:
        return "N/A"
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def load_player_high_scores():
    """Carrega os high scores do arquivo."""
    if not path.exists(HIGH_SCORE_FILE): # HIGH_SCORE_FILE de config.py
        return []
    try:
        with open(HIGH_SCORE_FILE, 'r') as f:
            scores = [float(line.strip()) for line in f if line.strip()]
        scores.sort() # Ordena: menor tempo primeiro
        return scores
    except Exception as e:
        print(f"Erro ao carregar high scores: {e}")
        return []

def save_player_high_scores(scores_list, new_player_score):
    """Adiciona novo score, mantém os top 5 e salva no arquivo."""
    if new_player_score is not None:
        scores_list.append(new_player_score)
    
    scores_list.sort() # Ordena: menor tempo primeiro
    updated_top_scores = scores_list[:5] # Mantém apenas os 5 melhores
    
    try:
        with open(HIGH_SCORE_FILE, 'w') as f: # HIGH_SCORE_FILE de config.py
            for score_val in updated_top_scores:
                f.write(f"{score_val}\n")
        return updated_top_scores # Retorna a lista atualizada dos top 5
    except Exception as e:
        print(f"Erro ao salvar high scores: {e}")
        # Retorna a lista como estava antes de tentar adicionar o novo score em caso de erro no salvamento,
        # mas após a ordenação e truncamento caso o novo score tenha sido adicionado à lista em memória.
        return scores_list[:5] if new_player_score is not None and new_player_score in scores_list else scores_list


def win_screen(screen, player_current_time, assets): # Recebe o tempo do jogador
    clock = pygame.time.Clock()

    pygame.mixer.music.stop()

    # Carrega os scores existentes
    current_high_scores = load_player_high_scores()
    
    # Adiciona o tempo do jogador atual (se houver) e atualiza a lista de recordes
    # A função save_player_high_scores agora retorna a lista atualizada dos top 5
    if player_current_time is not None:
        final_high_scores = save_player_high_scores(list(current_high_scores), player_current_time)
    else:
        final_high_scores = current_high_scores

    # Criando o botao
    all_buttons = pygame.sprite.Group()
    x = 560
    y = 670
    # Criando o botão restart
    botao_restart = BotaoRestartWin(assets)
    botao_restart.rect.x = x
    botao_restart.rect.centery = y
    all_buttons.add(botao_restart)

    # Carrega o fundo da tela de vitória
    victory_img_path = path.join(IMG_DIR, 'victory.png') #
    try:
        victory_background = pygame.image.load(victory_img_path).convert()
    except pygame.error as e:
        print(f"Erro ao carregar imagem de vitória '{victory_img_path}': {e}")
        victory_background = pygame.Surface((WIDTH, HEIGHT))
        victory_background.fill(BLACK) # Fallback para fundo preto

    victory_background = pygame.transform.scale(victory_background, (WIDTH, HEIGHT))
    victory_background_rect = victory_background.get_rect()

    # Fontes para o ranking
    title_rank_font = assets.get(TIME_FONT) # Fonte para o título "Melhores Tempos" e tempo do jogador
    
    # Para os scores individuais, usa a mesma família de fonte, mas pode ser um tamanho diferente
    font_file_path = path.join(FNT_DIR, 'PressStart2P.ttf') # Arquivo da fonte
    individual_score_font = pygame.font.Font(font_file_path, 24) # Tamanho um pouco menor para a lista
    instructions_font = pygame.font.Font(font_file_path, 20)


    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão
                for restart in all_buttons:
                    if restart.rect.collidepoint(event.pos):
                        restart.mouse_over(True)
                    else:
                        restart.mouse_over(False)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for restart in all_buttons:
                    if restart.rect.collidepoint(event.pos):
                        assets[BTN_CLICK_SOUND].play()
                        state = GAME
                        running = False 
        
        screen.fill(BLACK)
        screen.blit(victory_background, victory_background_rect)

        # Exibir Ranking
        if title_rank_font:
            # Título do Ranking
            rank_title_text = "Melhores Tempos:"
            rank_title_surface = title_rank_font.render(rank_title_text, True, YELLOW) #
            rank_title_rect = rank_title_surface.get_rect(center=(WIDTH / 2, HEIGHT * 0.25))
            screen.blit(rank_title_surface, rank_title_rect)

            # Exibir os 5 melhores tempos
            for i, score_value in enumerate(final_high_scores[:5]):
                score_display_text = f"{i+1}. {format_time_display(score_value)}"
                score_surface = individual_score_font.render(score_display_text, True, WHITE) #
                score_rect = score_surface.get_rect(center=(WIDTH / 2, HEIGHT * 0.35 + (i * 35)))
                screen.blit(score_surface, score_rect)
            
            # Exibir tempo do jogador atual
            player_time_str = format_time_display(player_current_time)
            player_score_text = f"Seu Tempo: {player_time_str}"
            player_score_surface = title_rank_font.render(player_score_text, True, YELLOW)
            # Posiciona abaixo da lista de recordes, ou em uma posição fixa se a lista estiver vazia
            player_score_y_pos = HEIGHT * 0.35 + (len(final_high_scores[:5]) * 35) + 20 
            if not final_high_scores: # Caso não haja high scores ainda
                 player_score_y_pos = HEIGHT * 0.35 + 20

            player_score_rect = player_score_surface.get_rect(center=(WIDTH / 2, player_score_y_pos ))
            screen.blit(player_score_surface, player_score_rect)
            all_buttons.draw(screen)

        pygame.display.flip()

    return state