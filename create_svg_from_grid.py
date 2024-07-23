import json
import os
from svgwrite import Drawing

def create_svg_from_grid(grid, output_file, cell_size=10, dark_mode=False):
    rows, cols = len(grid), len(grid[0])
    dwg = Drawing(output_file, profile='tiny', size=(cols * cell_size, rows * cell_size))
    background_color = 'black' if dark_mode else 'white'
    dwg.add(dwg.rect(insert=(0, 0), size=(cols * cell_size, rows * cell_size), fill=background_color))
    fill_color = 'white' if dark_mode else 'black'
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                dwg.add(dwg.rect(insert=(x * cell_size, y * cell_size), size=(cell_size, cell_size), fill=fill_color))
    dwg.save()

with open('random_grid.json') as f:
    grid = json.load(f)

# Tạo thư mục output nếu chưa tồn tại
os.makedirs('dist', exist_ok=True)

# Tạo SVG cho chế độ sáng
create_svg_from_grid(grid, 'dist/github-contribution-grid-snake.svg')

# Tạo SVG cho chế độ tối
create_svg_from_grid(grid, 'dist/github-contribution-grid-snake-dark.svg', dark_mode=True)
