import pygame
from os import path
from config import BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, HIGH_SCORE_FILE, YELLOW, WHITE, FNT_DIR, RED
from assets import TIME_FONT, BTN_CLICK_SOUND, WIN_SCREEN_IMG
from sprites import BotaoRestartWin

def format_time_display(total_seconds):
    """
    Formata o tempo total em segundos para o formato MM:SS.
    Args:
        total_seconds (float): Tempo total em segundos.
    Returns:
        str: Tempo formatado como "MM:SS". Retorna "N/A" se total_seconds for None.
    """
    if total_seconds is None:
        return "N/A"
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def load_player_high_scores():
    '''
    Carrega os high scores do arquivo e retorna uma lista ordenada.
    Se o arquivo não existir, retorna uma lista vazia.
    Se houver erro ao ler o arquivo, imprime o erro e retorna uma lista vazia.
    '''
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
    """
    Salva os high scores no arquivo, mantendo apenas os 5 melhores tempos.
    Args:
        scores_list (list): Lista de tempos dos jogadores.
        new_player_score (float): Tempo do novo jogador a ser adicionado.
    Returns:
        list: Lista atualizada dos 5 melhores tempos.
    """
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
        return scores_list[:5] if new_player_score is not None and new_player_score in scores_list else scores_list


def win_screen(screen, player_current_time, assets):
    """
    Tela de vitória do jogo.
    Exibe o ranking dos melhores tempos e permite que o jogador reinicie o jogo.
    Args:
        screen (pygame.Surface): A superfície onde a tela será desenhada.
        player_current_time (float): Tempo do jogador atual em segundos.
        assets (dict): Dicionário contendo os recursos do jogo, como sons e imagens.
    Returns:
        int: O estado do jogo após a interação do usuário.
    """
    clock = pygame.time.Clock()

    pygame.mixer.music.stop()

    # Carrega os scores existentes
    current_high_scores = load_player_high_scores()
    
    # Flag para verificar se o tempo do jogador entrou no ranking
    player_score_in_ranking = False
    if player_current_time is not None:
        temp_scores_for_check = sorted(list(current_high_scores) + [player_current_time])
        if player_current_time in temp_scores_for_check[:5]:
            player_score_in_ranking = True

    # Adiciona o tempo do jogador atual (se houver) e atualiza a lista de recordes
    final_high_scores = save_player_high_scores(list(current_high_scores), player_current_time)


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
    victory_background = assets.get(WIN_SCREEN_IMG)
    if victory_background is None:
        print(f"Erro: Imagem de vitória não encontrada em assets['{WIN_SCREEN_IMG}']. Verifique o caminho e carregamento.")
        victory_background = pygame.Surface((WIDTH, HEIGHT))
        victory_background.fill(BLACK) # Fallback para um fundo preto se a imagem não for carregada corretamente.
    
    victory_background = pygame.transform.scale(victory_background, (WIDTH, HEIGHT))
    victory_background_rect = victory_background.get_rect()

    # Fontes para o ranking
    title_rank_font = assets.get(TIME_FONT)
    
    font_file_path = path.join(FNT_DIR, 'PressStart2P.ttf')
    individual_score_font = pygame.font.Font(font_file_path, 24)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.MOUSEMOTION:
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
            rank_title_surface = title_rank_font.render(rank_title_text, True, YELLOW)
            rank_title_rect = rank_title_surface.get_rect(center=(WIDTH / 2, HEIGHT * 0.25))
            screen.blit(rank_title_surface, rank_title_rect)

            # Exibir os 5 melhores tempos
            for i, score_value in enumerate(final_high_scores[:5]):
                score_display_text = f"{i+1}. {format_time_display(score_value)}"
                
                score_color = WHITE
                # Verifica se o score atual na lista é o tempo do jogador e se ele entrou no ranking
                if player_score_in_ranking and score_value == player_current_time:
                    score_color = RED

                score_surface = individual_score_font.render(score_display_text, True, score_color)
                score_rect = score_surface.get_rect(center=(WIDTH / 2, HEIGHT * 0.35 + (i * 35)))
                screen.blit(score_surface, score_rect)
            
            # Exibir tempo do jogador atual
            player_time_str = format_time_display(player_current_time)
            player_score_text = f"Seu Tempo: {player_time_str}"
            
            player_time_color = YELLOW
            if player_score_in_ranking:
                player_time_color = RED

            player_score_surface = title_rank_font.render(player_score_text, True, player_time_color)
            player_score_y_pos = HEIGHT * 0.35 + (len(final_high_scores[:5]) * 35) + 20 
            if not final_high_scores:
                 player_score_y_pos = HEIGHT * 0.35 + 20

            player_score_rect = player_score_surface.get_rect(center=(WIDTH / 2, player_score_y_pos ))
            screen.blit(player_score_surface, player_score_rect)
            all_buttons.draw(screen)

        pygame.display.flip()

    return state