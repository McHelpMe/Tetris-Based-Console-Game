
import random
import os
import time

# Constants
GRID_HEIGHT = 20
GRID_WIDTH = 10
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

def create_grid():
    return [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔" + "═" * GRID_WIDTH + "╗")
    for row in grid:
        print("║" + "".join("█" if cell else " " for cell in row) + "║")
    print("╚" + "═" * GRID_WIDTH + "╝")

def check_collision(grid, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if (x + off_x < 0 or
                    x + off_x >= GRID_WIDTH or
                    y + off_y >= GRID_HEIGHT or
                    grid[y + off_y][x + off_x]):
                    return True
    return False

def rotate_shape(shape):
    return [list(row) for row in zip(*shape[::-1])]

def merge_shape(grid, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + off_y][x + off_x] = cell

def clear_rows(grid):
    cleared_rows = 0
    grid[:] = [row for row in grid if any(cell == 0 for cell in row)]
    while len(grid) < GRID_HEIGHT:
        grid.insert(0, [0] * GRID_WIDTH)
        cleared_rows += 1
    return cleared_rows

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

def load_high_score():
    try:
        with open("high_score.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def apply_twist(grid, current_shape, offset):
    twist_event = random.choice(["rotate", "modify_grid", "speed_change", None])
    if twist_event == "rotate":
        current_shape = rotate_shape(current_shape)
    elif twist_event == "modify_grid":
        for i in range(random.randint(1, 3)):
            row = random.randint(0, GRID_HEIGHT - 1)
            grid[row] = [random.choice([0, 1]) for _ in range(GRID_WIDTH)]
    return current_shape, twist_event

def play_game(mode="classic"):
    grid = create_grid()
    current_shape = random.choice(SHAPES)
    offset = [GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0]
    score = 0
    fall_speed = 0.5 if mode == "classic" else 0.3

    while True:
        print_grid(grid)
        print(f"Score: {score}")
        if mode == "chaos":
            print("Mode: Chaos")

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

        if mode == "chaos":
            current_shape, twist_event = apply_twist(grid, current_shape, offset)
            if twist_event:
                print(f"Twist Event: {twist_event}!")

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

def main():
    while True:
        print("Tetris Game")
        print("1. Classic Mode")
        print("2. Chaos Mode")
        print("3. Quit")
        choice = input("Choose a mode (1/2/3): ").strip()
        if choice == "1":
            play_game("classic")
        elif choice == "2":
            play_game("chaos")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
