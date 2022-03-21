import pygame, sys
# classes
class GameState():
    def __init__(self):
        self.state ='intro'

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # on mouse click
                self.state = "main_game"
            # Drawing
        screen.fill((0, 0, 255))
        screen.blit(login, (0, 0))
        screen.blit(button, button_rect)
        screen.blit(ready_text,button_rect)
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #if event.type == pygame.MOUSEBUTTONDOWN:  # on mouse click
                #self.state = "main_game"
            # Drawing
        screen.fill((0, 0, 255))
        screen.blit(main, (0, 0))

        pygame.display.flip()


    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()
        #if self.state == "start_screen":
          #  self.start_screen()


# General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()
# Game Screen
screen_width = 1270
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game intro")

# Variables
login = pygame.image.load("assets/login.png")
main = pygame.image.load("assets/blue_screen.png")
button = pygame.image.load("assets/button.png")
button_rect = button.get_rect(center=(250, 100))
ready_text = pygame.image.load("assets/ready_text.png")

# Creating the sprites and groups

while True:
    game_state.state_manager()
    # game state setup here
    clock.tick(60)
