import random
import os
import time

# Game grid dimensions
GRID_HEIGHT = 20
GRID_WIDTH = 10

# Shape definitions (Tetris blocks)
SHAPES = [
    [[1, 1, 1, 1]],  # Line shape
    [[1, 1], [1, 1]],  # Square shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[0, 1, 1], [1, 1, 0]]   # S shape
]

# Creates a new grid (empty)
def create_grid():
    return [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Print the game grid to the console
def print_grid(grid, current_shape=None, offset=None):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("╔" + "═" * GRID_WIDTH + "╗")
    for y, row in enumerate(grid):
        row_str = ""
        for x, cell in enumerate(row):
            if current_shape and offset:
                # Check if the current block overlaps this cell and display it
                if y >= offset[1] and x >= offset[0] and y < offset[1] + len(current_shape) and x < offset[0] + len(current_shape[0]) and current_shape[y - offset[1]][x - offset[0]]:
                    row_str += "█"
                else:
                    row_str += " " if cell == 0 else "█"
            else:
                row_str += "█" if cell else " "
        print("║" + row_str + "║")
    print("╚" + "═" * GRID_WIDTH + "╝")

# Check if the current shape collides with others or goes out of bounds
def check_collision(grid, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if (x + off_x < 0 or x + off_x >= GRID_WIDTH or y + off_y >= GRID_HEIGHT or grid[y + off_y][x + off_x]):
                    return True
    return False

# Rotate the shape 90 degrees
def rotate_shape(shape):
    return [list(row) for row in zip(*shape[::-1])]

# Merge the current shape with the grid
def merge_shape(grid, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + off_y][x + off_x] = cell

# Clear any full rows and return the number of cleared rows
def clear_rows(grid):
    cleared_rows = 0
    grid[:] = [row for row in grid if any(cell == 0 for cell in row)]
    while len(grid) < GRID_HEIGHT:
        grid.insert(0, [0] * GRID_WIDTH)
        cleared_rows += 1
    return cleared_rows

# Save the high score to a file
def save_high_score(score):
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())
    except FileNotFoundError:
        high_score = 0

    if score > high_score:
        with open("high_score.txt", "w") as f:
            f.write(str(score))
        return score, True
    return high_score, False

# Load the high score from the file
def load_high_score():
    try:
        with open("high_score.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

# Apply random twist effects (e.g., rotate, speed change, rising bottom)
def apply_twist(grid, current_shape, offset, score):
    twist_event = random.choice(["rotate", "speed_change", "rising_bottom", None])
    new_fall_speed = 0.5  # Default fall speed for Classic Mode
    
    if twist_event == "rotate":
        current_shape = rotate_shape(current_shape)
        print("Twist Event: Rotation!")
        
    elif twist_event == "speed_change":
        new_fall_speed = 0.3  # Speed up the game
        print("Twist Event: Speed Change!")

    elif twist_event == "rising_bottom":
        lines_cleared = clear_rows(grid)  # Get the number of lines cleared
        if lines_cleared > 0 and (lines_cleared & (lines_cleared - 1)) == 0:  # Power of 2 check
            print(f"Twist Event: Rising Bottom! ({lines_cleared} lines cleared)")
            grid.insert(0, [0] * GRID_WIDTH)
            grid.pop()  # Remove the bottom row
        else:
            print("Twist Event: Rising Bottom (no power of 2 lines cleared)")

    return current_shape, new_fall_speed

# Main game loop for different game modes
def play_game(mode="classic"):
    grid = create_grid()
    current_shape = random.choice(SHAPES)
    offset = [GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0]
    score = 0
    fall_speed = 0.5 if mode == "classic" else 0.3

    while True:
        print_grid(grid, current_shape, offset)
        print(f"Score: {score}")
        if mode == "frenzy":
            print("Mode: Frenzy")

        command = input("Command (a: left, d: right, w: rotate, s: drop, q: quit): ").strip().lower()
        if command == "q":
            print("Game Over!")
            high_score, _ = save_high_score(score)
            print(f"Your score: {score} | High Score: {high_score}")
            break
        elif command == "a":
            offset[0] -= 1
            if check_collision(grid, current_shape, offset):
                offset[0] += 1
        elif command == "d":
            offset[0] += 1
            if check_collision(grid, current_shape, offset):
                offset[0] -= 1
        elif command == "w":
            rotated = rotate_shape(current_shape)
            if not check_collision(grid, rotated, offset):
                current_shape = rotated
        elif command == "s":
            offset[1] += 1

        if mode == "frenzy":
            current_shape, fall_speed = apply_twist(grid, current_shape, offset, score)

        offset[1] += 1
        if check_collision(grid, current_shape, offset):
            offset[1] -= 1
            merge_shape(grid, current_shape, offset)
            score += clear_rows(grid)
            current_shape = random.choice(SHAPES)
            offset = [GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0]
            if check_collision(grid, current_shape, offset):
                print("Game Over!")
                high_score, new_high = save_high_score(score)
                print(f"Your score: {score}")
                if new_high:
                    print("Congratulations! New High Score!")
                else:
                    print(f"High Score: {high_score}")
                break

        time.sleep(fall_speed)

# Main menu loop
def main():
    while True:
        print("Tetris Game")
        print("1. Classic Mode")
        print("2. Frenzy Mode")
        print("3. Quit")
        choice = input("Choose a mode (1/2/3): ").strip()
        if choice == "1":
            play_game("classic")
        elif choice == "2":
            play_game("frenzy")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the game
if __name__ == "__main__":
    main()
