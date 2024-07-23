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

# Create output directory if it does not exist
os.makedirs('dist', exist_ok=True)

# Create SVG for light mode
create_svg_from_grid(grid, 'dist/random_grid.svg')

# Create SVG for dark mode
create_svg_from_grid(grid, 'dist/random_grid_dark.svg', dark_mode=True)
