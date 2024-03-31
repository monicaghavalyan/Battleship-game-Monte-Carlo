import random
import argparse
import copy

def create_grid(size):
    return [['.'] * size for _ in range(size)]

def place_ships_randomly(grid, ships):
    for ship in ships:
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, len(grid) - 1)
                col = random.randint(0, len(grid) - len(ship))
            else:
                row = random.randint(0, len(grid) - len(ship))
                col = random.randint(0, len(grid) - 1)
            
            if check_placement(grid, ship, row, col, orientation):
                put_ship(grid, ship, row, col, orientation)
                placed = True

def check_placement(grid, ship, row, col, orientation):
    if orientation == 'horizontal':
        return all(grid[row][col + i] == '.' for i in range(len(ship)))
    else:
        return all(grid[row + i][col] == '.' for i in range(len(ship)))

def put_ship(grid, ship, row, col, orientation):
    for i in range(len(ship)):
        if orientation == 'horizontal':
            grid[row][col + i] = ship[i]
        else:
            grid[row + i][col] = ship[i]

def monte_carlo_shot(grid, ships, shots, samples):
    hit_counts = { (i, j): 0 for i in range(len(grid)) for j in range(len(grid)) }
    for _ in range(samples):
        sample_grid = create_grid(len(grid))
        place_ships_randomly(sample_grid, ships)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if sample_grid[i][j] == '*' and (i, j) not in shots:
                    hit_counts[(i, j)] += 1

    best_shot = max(hit_counts, key=hit_counts.get)
    return best_shot

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()
        
def main(grid_size, ship_lengths, num_samples, num_of_shots):
    ships = [['*'] * length for length in ship_lengths]
    grid_demo = create_grid(grid_size)
    place_ships_randomly(grid_demo, ships)
    grid_demo_arr = [copy.deepcopy(grid_demo) for _ in range(len(num_samples))]

    print("-" * 20)
    print("Initial grid")
    print_grid(grid_demo)

    for i, samples in enumerate(num_samples):
        shots = set()
        curr_grid = grid_demo_arr[i]
        for _ in range(num_of_shots):
            shot = monte_carlo_shot(create_grid(grid_size), ships, shots, samples)
            shots.add(shot)
            hit = False
            for ship in ships:
                if curr_grid[shot[0]][shot[1]] == '*':
                    hit = True
                    curr_grid[shot[0]][shot[1]] = 'X'
                    break
            if not hit and curr_grid[shot[0]][shot[1]] != 'X':
                curr_grid[shot[0]][shot[1]] = 'O'
        
        print("\n")
        print(f"The result of {num_of_shots} shots after running {samples} samples of Monte-Carlo")
        print_grid(curr_grid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Battleship Monte Carlo simulation.')
    parser.add_argument('--grid_size', type=int, default=8, help='Size of the Battleship grid')
    parser.add_argument('--ship_lengths', nargs='+', type=int, default=[3, 3, 2], help='Lengths of the ships')
    parser.add_argument('--num_samples', nargs='+', type=int, default=[100, 500, 1000, 10000, 30000], help='Number of Monte Carlo samples')
    parser.add_argument('--num_of_shots', type=int, default=25, help='Number of shots for each sampling')
    
    args = parser.parse_args()
    main(args.grid_size, args.ship_lengths, args.num_samples, args.num_of_shots)

