import random
import pygame


class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self):
        mx, my = pygame.mouse.get_pos()
        return (self.x < mx < self.x + self.width) and (self.y < my < self.y + self.height)


class RpsGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        # Load Images.
        self.bg = pygame.image.load("background.jpeg")
        self.r_btn = pygame.image.load("rbutton.png").convert_alpha()
        self.p_btn = pygame.image.load("pbutton.png").convert_alpha()
        self.s_btn = pygame.image.load("sbutton.png").convert_alpha()
         # define buttons
        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()

        # Buttons position & size
        self.rock_btn = Button(30, 520, 300, 140)
        self.paper_btn = Button(340, 520, 300, 140)
        self.scissors_btn = Button(640, 520, 300, 140)

        # Fonts and Score
        self.font = pygame.font.Font(None, 90)
        self.text = self.font.render(" ", True, (255, 255, 255))
        self.pl_score = 0
        self.pc_score = 0

        self.p_option = ""
        self.pc_random_choice = ""

    def player(self):
        if self.rock_btn.clicked():
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_btn.clicked():
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
        elif self.scissors_btn.clicked():
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors, (120, 200))
        return self.p_option

    def computer(self):
        option = ["rock", "paper", "scissors"]
        self.pc_random_choice = random.choice(option)

        if self.pc_random_choice == "rock":
            image = self.choose_rock
        elif self.pc_random_choice == "paper":
            image = self.choose_paper
        else:
            image = self.choose_scissors

        self.screen.blit(image, (600, 200))
        return self.pc_random_choice

    def scoring(self):
        pl = self.p_option
        pc = self.pc_random_choice

        if pl == pc:
            return  # Tie

        if (pl == "rock" and pc == "scissors") or \
           (pl == "paper" and pc == "rock") or \
           (pl == "scissors" and pc == "paper"):
            self.pl_score += 1
        else:
            self.pc_score += 1

    def image_reset(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        score_text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))
        self.screen.blit(score_text, (330, 0))

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            self.image_reset()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rock_btn.clicked() or self.paper_btn.clicked() or self.scissors_btn.clicked():
                        self.player()
                        self.computer()
                        self.scoring()

            pygame.display.update()
            clock.tick(50)

        pygame.quit()


if __name__ == "__main__":
    game = RpsGame()
    game.game_loop()
