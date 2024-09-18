from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox)
from PyQt5.QtCore import Qt
from game_logic import GameLogic

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.game_logic = GameLogic()
        self.init_ui()
        self.set_default_difficulty()

    def init_ui(self):
        self.guess_input = QLineEdit(self)
        self.guess_input.setPlaceholderText("Enter your guess")
        self.feedback_label = QLabel("", self)
        self.attempts_label = QLabel("Attempts: 0", self)
        self.submit_button = QPushButton("Submit", self)
        self.new_game_button = QPushButton("New Game", self)
        self.difficulty_combo = QComboBox(self)
        self.difficulty_combo.addItems(["Easy (1-50)", "Medium (1-100)", "Hard (1-200)"])

        self.submit_button.clicked.connect(self.submit_guess)
        self.new_game_button.clicked.connect(self.new_game)
        self.difficulty_combo.currentIndexChanged.connect(self.change_difficulty)
        self.guess_input.returnPressed.connect(self.submit_guess)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.guess_input)
        hbox1.addWidget(self.submit_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.feedback_label)
        vbox.addWidget(self.attempts_label)
        vbox.addWidget(self.difficulty_combo)
        vbox.addWidget(self.new_game_button)

        self.setLayout(vbox)
        self.setWindowTitle("Guess the Number")
        self.setGeometry(100, 100, 500, 300)  # Increase the size of the window

    def set_default_difficulty(self):
        self.difficulty_combo.setCurrentIndex(0)  # Set default to "Easy"
        self.new_game()  # Start a new game with the default difficulty

    def submit_guess(self):
        try:
            guess = int(self.guess_input.text())
            feedback = self.game_logic.check_guess(guess)
            self.feedback_label.setText(feedback)
            self.attempts_label.setText(f"Attempts: {self.game_logic.attempts}")
            if "Correct" in feedback:
                self.submit_button.setEnabled(False)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")

    def new_game(self):
        difficulty = self.get_difficulty()
        self.game_logic.reset_game(difficulty)
        self.feedback_label.setText("")
        self.attempts_label.setText("Attempts: 0")
        self.guess_input.clear()
        self.submit_button.setEnabled(True)

    def change_difficulty(self):
        self.new_game()  # Restart the game with the new difficulty level

    def get_difficulty(self):
        level = self.difficulty_combo.currentText()
        if "Easy" in level:
            return 50
        elif "Medium" in level:
            return 100
        elif "Hard" in level:
            return 200
