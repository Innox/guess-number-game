### `README.md`

```markdown
# Guess The Number Game

Welcome to the Guess The Number game. 
This is a fun, interactive game where the player tries to guess a randomly generated number within a specific range. The goal is to guess the correct number in as few attempts as possible. You can customize the difficulty level by choosing the range of numbers, making the game more challenging or easier depending on your preference. Keep track of your attempts, and try to beat your previous records.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [How to Play](#how-to-play)
- [Customization](#customization)
- [Game Controls](#game-controls)
- [Project Structure](#project-structure)

## Features
- Customizable Difficulty Levels: Choose from different difficulty levels, adjusting the range of possible numbers to guess.
- Attempt Tracking: Keep track of how many guesses you've made to find the correct number.
- User-Friendly Interface: Simple and intuitive design for easy gameplay.
- Responsive Design: Optimized for various screen sizes, allowing play on both desktop and mobile devices.
- Restart Option: Restart the game at any time to try again with a new number.
- Input Validation: Handles invalid inputs to ensure smooth gameplay (e.g., when entering non-numeric values).

## Requirements

To run this game, ensure that you have the following installed:
- Python 3.x
- PyQt5 for the graphical user interface (GUI)
- Dependencies listed in `requirements.txt`

## Installation

Follow these steps to set up the environment and install dependencies:

1. **Clone the repository:**

   Open your terminal and run the following command to clone the project:

   ```bash
   git clone https://github.com/Innox/guess-number-game.git
   ```

2. **Navigate to the project folder:**

   ```bash
   cd guess-number-game
   ```

3. **Create a virtual environment:**

   Create a virtual environment to keep dependencies isolated.

   On Linux/macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install the required dependencies:**

   Make sure `pip` is installed and up-to-date. Then install all the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

Once you have installed all dependencies, follow these steps to run the game:

1. **Launch the game by running the main Python file that is the main.py:**

   In your terminal, run the following command to start the server:

   ```bash
   python main.py
   ```

A window should appear where you can start playing the "Guess the Number" game by entering your guesses and interacting with the game's user interface.


## How to Play

- **Goal**: The objective of the game is to guess the randomly selected number within a certain range in as few attempts as possible.

- **Controls**: Enter your guesses into the input box and click "Submit" or press Enter to see if your guess is too high, too low, or correct.


### Scoring
The game keeps track of the number of attempts it takes you to guess the correct number. Try to guess the number in the fewest attempts possible.


## Customization

### Difficulty Levels
The game includes three difficulty levels: **Easy**, **Medium**, and **Hard**. You can adjust the difficulty before starting the game. The difficulty setting controls the range of numbers you have to guess from:

- **Easy**: Guess a number between 1 and 10.
- **Medium**: Guess a number between 1 and 50.
- **Hard**: Guess a number between 1 and 100.

### Difficulty Levels:
1. Before starting the game, select the desired difficulty level from the settings or the dropdown menu.
2. Click "Start Game" to begin.

## Game Controls
- **Enter your guess**: Type your guess into the input field and either press Enter or click the "Submit" button.

- **Hints**: After each guess, you'll receive feedback indicating whether the correct number is higher or lower than your guess.

- **Restart the game**: Click the "Restart" button at any time to generate a new number and start fresh.


## Project Structure
Here is a basic overview of the project structure:

```plaintext
guess-number-game/
├── main.py
├── game_logic.py
├── gui.py
├── utils.py
└── requirements.txt
```

main.py: Initializes and starts the application.
game_logic.py: Contains the core game logic, including number generation and guess evaluation.
gui.py: Manages the graphical user interface (GUI).
utils.py: Placeholder for additional utility functions (not used in the current version).
requirements.txt: Lists the required Python packages for the project
README.md: This file, which provides detailed information about the project and how to run it.

## License
This project is open-source and available under the MIT License.

### Explanation of the README:

- **Features**: Outlines the key features of the game, including its responsiveness, controls, and difficulty settings.
- **Requirements**: Lists the necessary prerequisites for running the game, such as Python 3.x.
- **Installation**: Provides clear steps to set up the environment, including creating a virtual environment and installing dependencies from `requirements.txt`.
- **Running the Game**: Explains how to run the game.
- **How to Play**: Describes the gameplay mechanics and controls.
- **Customization**: Explains the difficulty settings and how to change them.
- **Game Controls**: Provides a quick summary of the game controls.
- **Project Structure**: Gives a high-level overview of the project folder structure, making it easier for developers to navigate the codebase.
