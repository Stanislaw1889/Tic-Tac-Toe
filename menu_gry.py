import pygame
import sys
import ustawienia

class Button:
    def __init__(self, text, x, y, w, h, color):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, ustawienia.GRUBOŚĆ_RAMKI)
        font = pygame.font.SysFont("Arial", 24, bold=True)
        text_surf = font.render(self.text, True, ustawienia.BIEL)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def run_game_setup_menu(screen, is_singleplayer=True):
    clock = pygame.time.Clock()
    
    selected_size = 3
    selected_difficulty = "Łatwy"
    selected_timed = False


    btn_3x3 = Button("Plansza 3x3", 250, 140, 300, 45, ustawienia.ZIELEN)
    btn_4x4 = Button("Plansza 4x4", 250, 200, 300, 45, ustawienia.ZIELEN)
    btn_5x5 = Button("Plansza 5x5", 250, 260, 300, 45, ustawienia.ZIELEN) #Poprawilem miejsce przycisku
    
    btn_diff = Button(f"Poziom: {selected_difficulty}", 250, 320, 300, 45, ustawienia.SZARY_TEKST)
    btn_mode = Button("Tryb: Klasyczny", 250, 380, 300, 45, ustawienia.ZIELEN)
    btn_start = Button("URUCHOM GRĘ", 250, 460, 300, 45, ustawienia.CZERWIEN)
    btn_back = Button("Powrót", 250, 520, 300, 45, ustawienia.SZARY_TEKST)

    in_menu = True
    while in_menu:
        screen.fill(ustawienia.CZERN_TLA) 
        mouse_pos = pygame.mouse.get_pos()
        
        font = pygame.font.SysFont("Arial", 32, bold=True)
        title_text = "GRA Z KOMPUTEREM" if is_singleplayer else "GRA WIELOOSOBOWA"
        title_surf = font.render(title_text, True, ustawienia.BIEL)
        title_x = (ustawienia.OKNO_SZEROKOSC // 2) - (title_surf.get_width() // 2)
        screen.blit(title_surf, (title_x, 80))

        btn_3x3.color = ustawienia.ZIELEN if selected_size == 3 else ustawienia.SZARY_TEKST
        btn_4x4.color = ustawienia.ZIELEN if selected_size == 4 else ustawienia.SZARY_TEKST
        btn_5x5.color = ustawienia.ZIELEN if selected_size == 5 else ustawienia.SZARY_TEKST

        btn_3x3.draw(screen)
        btn_4x4.draw(screen)
        btn_5x5.draw(screen)
        if is_singleplayer:
            btn_diff.draw(screen)
       
        btn_mode.draw(screen) #Zniknal przycisk do wyboru trybu gry
        btn_start.draw(screen)
        btn_back.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_3x3.is_clicked(mouse_pos):
                    selected_size = 3
                elif btn_4x4.is_clicked(mouse_pos):
                    selected_size = 4
                elif btn_5x5.is_clicked(mouse_pos):
                    selected_size = 5
                
                elif btn_diff.is_clicked(mouse_pos) and is_singleplayer:
                    if selected_difficulty == "Łatwy": selected_difficulty = "Średni"
                    elif selected_difficulty == "Średni": selected_difficulty = "Trudny"
                    else: selected_difficulty = "Łatwy"
                    btn_diff.text = f"Poziom: {selected_difficulty}"

                elif btn_mode.is_clicked(mouse_pos):
                    selected_timed = not selected_timed
                    btn_mode.text = "Tryb: Na czas (5s)" if selected_timed else "Tryb: Klasyczny"

                #Usuwam ten blok bo mozliwe ze jest niepotrzebny    
                #elif btn_start.is_clicked(mouse_pos):
                    #return {"size": selected_size, "difficulty": selected_difficulty, "action": "START"}
                    
                elif btn_back.is_clicked(mouse_pos):
                    return {"action": "BACK"}

                elif btn_start.is_clicked(mouse_pos):
                    return {
                        "size": selected_size, 
                        "difficulty": selected_difficulty, 
                        "timed": selected_timed, 
                        "action": "START"
                    }

        pygame.display.flip()
        clock.tick(60)
