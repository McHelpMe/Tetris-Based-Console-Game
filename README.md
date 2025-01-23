# Tetris-Based-Console-Game

A simple yet engaging console-based Tetris game written in Python, featuring two distinct modes: **Classic Mode** for traditional gameplay and **Frenzy Mode** for a unique, unpredictable experience. The game tracks scores and high scores for added competitiveness.

## Features
### Game Modes
#### 1. Classic Mode
   * Traditional Tetris gameplay where players move, rotate, and drop Tetrominoes to clear rows and score points.
#### 2. Frenzy Mode
   * **Random Rotations**: Tetrominoes may rotate unexpectedly.
   * **Random Grid Modifications**: Rows may randomly fill with blocks or be cleared.
   * **Variable Speed**: The fall speed changes unpredictably, keeping players on their toes.

### Additional Features
* **Score Tracking**: Points are awarded for clearing rows, with higher scores achieved by clearing multiple rows at once.
* **High Score Persistence**: High scores are saved in a local file (high_score.txt) and persist across game sessions.
* **Interactive Console Controls**:<br>
  * `a`: Move piece left.<br>
  * `d`: Move piece right.<br>
  * `w`: Rotate piece.<br>
  * `s`: Drop piece faster.<br>
  * `q`: Quit the game.<br>

## Installation
### Requirements
 * Python 3.6 or higher
### Setup Instructions
#### 1. Clone the repository or download the game script:
 ```bash
git clone https://github.com/McHelpMe/Tetris-Based-Console-Game.git
 ```
Alternatively, [download TetrisGame.py](https://github.com/McHelpMe/Tetris-Based-Console-Game/blob/main/TetrisGame.py).

#### 2. Navigate to the project directory:
```bash
cd tetris-console-game
```

#### 3. Run the script:
```bash
python tetris.py
```

## How to Play
#### 1. **Launch the Game**: Run the script in your terminal:
```bash
python tetris.py
```
#### 2. Select a Mode
 * Enter `1` for **Classic Mode**
 * Enter `2` for **Chaos Mode**
#### 3. Game Controls
  * `a`: Move piece left.<br>
  * `d`: Move piece right.<br>
  * `w`: Rotate piece.<br>
  * `s`: Drop piece faster.<br>
  * `q`: Quit the game.<br>

## How the Game Works 
### Objective
The goal is to clear as many lines as possible by arranging falling shapes (tetrominoes) in a grid. Lines are cleared when they are completely filled, earning you points. The game ends when the grid fills up and no more shapes can fit.

### 1. Clearing Lines
       * Complete rows to clear them and earn points.
       * The more lines you clear at once, the higher the score (e.g., Tetris for 4 lines).
