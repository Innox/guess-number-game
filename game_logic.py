import random
import time

class GameLogic:
    def __init__(self):
        self.difficulty = 100
        self.reset_game()

    def reset_game(self, difficulty=None):
        if difficulty:
            self.difficulty = difficulty
        self.secret_number = random.randint(1, self.difficulty)
        self.attempts = 0
        self.start_time = time.time()

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "Too low"
        elif guess > self.secret_number:
            return "Too high"
        else:
            elapsed_time = time.time() - self.start_time
            return f"Correct! Attempts: {self.attempts}, Time: {elapsed_time:.2f} seconds"
