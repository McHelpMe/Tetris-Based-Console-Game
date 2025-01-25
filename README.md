# Tetris-Based-Console-Game

A simple yet engaging console-based Tetris game written in Python, featuring two distinct modes: **Classic Mode** for traditional gameplay and **Frenzy Mode** for a unique, unpredictable experience. The game tracks scores and high scores for added competitiveness.

## Features
### Game Modes
#### **1. Classic Mode**
   * Traditional Tetris gameplay where players move, rotate, and drop Tetrominoes to clear rows and score points.
#### **2. Frenzy Mode**
   * **Random Rotations**: Tetrominoes may rotate unexpectedly.
   * **Rising Bottom**: The Rising Bottom feature adds a row at the top after clearing a power-of-2<br> number of lines (1, 2, 4, 8, etc.), pushing blocks down and increasing difficulty.
   * **Changing Speed**: The fall speed changes unpredictably, keeping players on their toes.

### Additional Features
* **Score Tracking**: Points are awarded for clearing rows, with higher scores achieved by clearing multiple rows at once.
* **High Score Persistence**: High scores are saved in a local file (high_score.txt) and persist across game sessions.
* **Interactive Console Controls**:<br>
  * `a`: Move piece left.<br>
  * `d`: Move piece right.<br>
  * `w`: Rotate piece.<br>
  * `s`: Drop piece faster.<br>
  * `q`: Quit the game.<br>
* **Automatic Updates**: The game now updates frames automatically without requiring constant input, allowing smooth gameplay even without user commands.

## Installation
### Requirements
 * Python 3.6 or higher
### Setup Instructions
#### 1. You can either clone the repository using Git:
 ```bash
git clone https://github.com/McHelpMe/Tetris-Based-Console-Game.git
 ```
Or download the script directly by clicking [here](https://github.com/McHelpMe/Tetris-Based-Console-Game/raw/main/TetrisGame.py).

#### 2. Navigate to the project directory:
```bash
cd Tetris-Based-Console-Game
```

#### 3. Run the script:
```bash
python TetrisGame.py
```

## How to Play
#### 1. **Launch the Game**: Run the script in your terminal:
```bash
python tetris.py
```
#### 2. Select a Mode
 * Enter `1` for **Classic Mode**
 * Enter `2` for **Frenzy Mode**
#### 3. Game Controls
  * `a`: Move piece left.<br>
  * `d`: Move piece right.<br>
  * `w`: Rotate piece.<br>
  * `s`: Drop piece faster.<br>
  * `q`: Quit the game.<br>

## How the Game Works 
### Objective
The goal is to clear as many lines as possible by arranging falling shapes (tetrominoes) in a grid. Lines are cleared when they are completely filled, earning you points. The game ends when the grid fills up and no more shapes can fit.

#### 1. Clearing Lines
  * Complete rows to clear them and earn points.
  * The more lines you clear at once, the higher the score (e.g., Tetris for 4 lines).
#### 2. Difficulty
  * As you clear lines, the falling speed increases.
  * **Frenzy Mode** adds random events like shape rotations or speed changes.

### Game Over & High Score
  * The game ends when the grid is full and no more shapes can fall.
  * If your score beats the high score, it will be saved to `high_score.txt`.
  * On subsequent plays, the game will display the current high score, and if you break it, you'll be congratulated!
  * Example:
    ```bash
    Game Over!
    Your Score: 250
    New High Score: 250
    ```

## Changelog 
 ### Version 0.1 - Initial Release
  * Basic Classic Mode implemented.
  * Added grid rendering and Tetromino shapes (Line, Square, T, Z, S).
  * Basic movement controls: `a` (left), `d` (right), `w` (rotate), `s` (drop).
  * Line-clearing functionality with scoring.

 ### Version 0.2 - Score Tracking and Persistence
  * Added score tracking to calculate points based on rows cleared.
  * Implemented high score persistence using high_score.txt.
  * Displayed current score and high score during gameplay.

 ### Version 0.3 - Frenzy Mode Prototype
  * Introduced Frenzy Mode with random events:
    * Random Tetromino rotations.
    * Dynamic speed changes.
    * Initial prototype of the rising bottom feature.
  * Added a main menu for mode selection.

 ### Version 0.4 - Gameplay Improvements
  * Fixed a bug where blocks appeared outside the grid.
  * Improved collision detection for moving and rotating Tetrominoes.
  * Updated Rising Bottom feature to activate only after clearing a power-of-2 number of lines (1, 2, 4, etc.).
  * Displayed event messages for Frenzy Mode twists.

 ### Version 0.5 - Bug Fixes and Tweaks
  * Fixed an `IndexError` when blocks spawned partially outside the grid.
  * Added logic to delete out-of-bounds blocks and replace them with new ones at the top center of the grid.
  * Ensured Frenzy Mode events occur consistently

 ### Version 0.6 - Visual and Gameplay Enhancements
  * Refined the grid display for better readability in the console.
  * Added animations (via `time.sleep`) for falling Tetrominoes.
  * Improved feedback for Frenzy Mode events (e.g., "Twist Event: Speed Change").

 ### Version 0.7 - Automatic Frame Progression
  * Introduced optional automatic frame updates for smoother gameplay.
  * Added fall speed adjustments to balance gameplay between Classic and Frenzy modes

 ### Version 0.8 - Polishing Features
  * Improved the Rising Bottom feature to ensure consistent behavior.
  * Fixed a bug where the game would incorrectly end if blocks overlapped during spawning.

 ### Version 0.9 - Final Bug Fixes
  * Fixed an issue where Frenzy Mode events would occasionally conflict, causing unexpected behaviors.
  * Resolved a problem where the game would immediately end if blocks spawned outside the grid.
  * Optimized event-triggering logic for Frenzy Mode.

 ### Version 1.0 - Complete Release
  * Finalized Classic Mode and Frenzy Mode with balanced difficulty.
  * Added comprehensive comments to the code for clarity without revealing sensitive details.
  * Ensured all known bugs and edge cases are addressed:
    * Prevented blocks from spawning outside the grid.
    * Stabilized Frenzy Mode events and rising bottom mechanics.
    * Guaranteed seamless gameplay in both modes.
  * Added a detailed README and updated game description to include all features and controls.



## Possible Issues/Errors
 * **Race conditions in Frenzy Mode**: Rapid events might lead to glitches.
 * **Block collision edge cases**: Blocks may misalign at grid edges.
 * **Grid overflow during Rising Bottom**: Adding rows when the grid is nearly full may not gracefully trigger game-over.
 * **Timing desynchronization**: Auto-updates may conflict with user inputs.
 * **Performance issues**: Slower systems may experience delays or lag.
 * **Input responsiveness at high speeds**: Inputs might not register consistently.
 * **Save file corruption**: Manual tampering with `high_score.txt` can cause crashes.
 * **Unexpected grid behavior**: Misuse of controls or manual rotation can lead to blocks behaving oddly.




## Contact<br>
* [Send an Email](mailto:sorianojustin05@gmail.com)
