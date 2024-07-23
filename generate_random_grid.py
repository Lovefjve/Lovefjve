import random
import json

def generate_random_grid(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

grid = generate_random_grid(7, 52)  # 7 rows, 52 columns

with open('random_grid.json', 'w') as f:
    json.dump(grid, f)
