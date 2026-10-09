
import random
import pygame
from game.text_box import TextBox


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.max_attempts = 10
        self.max_history = 5

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.min_range = 1
        self.max_range = 100
        self.guess_history = []

        self.feedback_msg = "Enter a number between 1 and 100"
        self.feedback_color = (220, 220, 220)
        self.game_won = False
        self.game_over = False

        self.input_box = TextBox(width // 2 - 110, 150, 120, 48)
        self.submit_btn = pygame.Rect(width // 2 + 25, 150, 100, 48)

        self.font_title = pygame.font.SysFont(None, 42)
        self.font_medium = pygame.font.SysFont(None, 28)
        self.font_btn = pygame.font.SysFont(None, 26)
        self.font_small = pygame.font.SysFont(None, 24)

    def submit_guess(self):
        if self.game_won or self.game_over:
            return

        # Task 1: Handle empty input without crashing
        text = self.input_box.text.strip()

        if not text:
            self.feedback_msg = "Please enter a number!"
            self.feedback_color = (255, 220, 80)
            return

        try:
            guess = int(text)
        except ValueError:
            self.feedback_msg = "Please enter a valid number!"
            self.feedback_color = (255, 220, 80)
            return

        if not 1 <= guess <= 100:
            self.feedback_msg = "Enter a number between 1 and 100!"
            self.feedback_color = (255, 220, 80)
            return

        self.attempts += 1
        self.input_box.clear()

        if guess < self.secret_number:
            result = "TOO LOW"
            self.min_range = max(self.min_range, guess + 1)
            self.feedback_msg = f"TOO LOW! (Guess was {guess})"
            self.feedback_color = (80, 160, 240)

        elif guess > self.secret_number:
            result = "TOO HIGH"
            self.max_range = min(self.max_range, guess - 1)
            self.feedback_msg = f"TOO HIGH! (Guess was {guess})"
            self.feedback_color = (240, 100, 80)

        else:
            result = "CORRECT"
            self.feedback_msg = (
                f"CORRECT! Found in {self.attempts} attempts."
            )
            self.feedback_color = (80, 220, 90)
            self.game_won = True

        # Task 3: Store the latest valid guesses
        self.guess_history.append((guess, result))
        self.guess_history = self.guess_history[-self.max_history:]

        # Task 4: End the game after the attempt limit
        if not self.game_won and self.attempts >= self.max_attempts:
            self.game_over = True
            self.feedback_msg = (
                f"GAME OVER! The number was {self.secret_number}."
            )
            self.feedback_color = (255, 100, 100)

    def reset(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.min_range = 1
        self.max_range = 100
        self.guess_history.clear()

        self.feedback_msg = "Enter a number between 1 and 100"
        self.feedback_color = (220, 220, 220)
        self.game_won = False
        self.game_over = False
        self.input_box.clear()

    def handle_event(self, event):
        self.input_box.handle_event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (
                self.game_won or self.game_over
            ):
                self.reset()
            elif event.key == pygame.K_RETURN:
                self.submit_guess()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.submit_btn.collidepoint(event.pos):
                self.submit_guess()

    def update(self):
        pass

    def render(self, screen):
        screen.fill((30, 34, 42))

        title_surf = self.font_title.render(
            "Number Guessing Arena", True, (245, 245, 245)
        )
        screen.blit(
            title_surf,
            (self.width // 2 - title_surf.get_width() // 2, 35),
        )

        attempts_surf = self.font_medium.render(
            f"Attempts: {self.attempts}/{self.max_attempts}",
            True,
            (180, 185, 195),
        )
        screen.blit(
            attempts_surf,
            (self.width // 2 - attempts_surf.get_width() // 2, 95),
        )

        # Task 2: Display the narrowing search range
        range_surf = self.font_medium.render(
            f"Possible range: {self.min_range} - {self.max_range}",
            True,
            (180, 185, 195),
        )
        screen.blit(
            range_surf,
            (self.width // 2 - range_surf.get_width() // 2, 120),
        )

        self.input_box.render(screen)

        pygame.draw.rect(
            screen, (50, 150, 80), self.submit_btn, border_radius=6
        )
        pygame.draw.rect(
            screen, (220, 220, 220), self.submit_btn,
            width=2, border_radius=6
        )

        btn_text = self.font_btn.render(
            "SUBMIT", True, (255, 255, 255)
        )
        screen.blit(
            btn_text,
            (
                self.submit_btn.centerx - btn_text.get_width() // 2,
                self.submit_btn.centery - btn_text.get_height() // 2,
            ),
        )

        feedback_surf = self.font_medium.render(
            self.feedback_msg, True, self.feedback_color
        )
        screen.blit(
            feedback_surf,
            (
                self.width // 2 - feedback_surf.get_width() // 2,
                235,
            ),
        )

        # Task 3: Recent guess history
        history_title = self.font_medium.render(
            "Recent Guess History", True, (245, 245, 245)
        )
        screen.blit(
            history_title,
            (
                self.width // 2 - history_title.get_width() // 2,
                290,
            ),
        )

        history_y = 330
        for guess, result in reversed(self.guess_history):
            if result == "TOO LOW":
                color = (80, 160, 240)
            elif result == "TOO HIGH":
                color = (240, 100, 80)
            else:
                color = (80, 220, 90)

            history_surf = self.font_small.render(
                f"{guess} - {result}", True, color
            )
            screen.blit(
                history_surf,
                (
                    self.width // 2 - history_surf.get_width() // 2,
                    history_y,
                ),
            )
            history_y += 27

        # Task 4: Win or failure state
        if self.game_won:
            message = "You won! Press [R] to play again"
        elif self.game_over:
            message = "Game over! Press [R] to try again"
        else:
            message = None

        if message:
            restart_surf = self.font_medium.render(
                message, True, (255, 220, 80)
            )
            restart_y = self.height - 40
            screen.blit(
                restart_surf,
                (
                    self.width // 2 - restart_surf.get_width() // 2,
                    restart_y,
                ),
            )
