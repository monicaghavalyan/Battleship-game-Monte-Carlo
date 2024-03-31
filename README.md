# Battleship Monte Carlo Simulation

montecarlo.py Python script implements Monte Carlo algorithm for the battleship game. It generates moves according to Monte Carlo algorithm with different numbers of samples. After that, those moves are applied to the same initial grid, and the algorithm's effectiveness based on the sampling number is observed.

## Features

- Creating battleship game grid with customizable size.
- Placement of ships of any size.
- Implementation of Monte Carlo algorithm for calculating probabilities based on a large number of samples.
- Firing shots on the same initial grid using Monte Carlo algorithm based on different numbers of samples.
- Displaying the order of shots for each case and the resulting grid.

## Libraries

No additional libraries are used.

## Usage

Can be runned with the following line of code:
>_python battleship_monte_carlo.py --grid_size [GRID_SIZE] --ship_lengths [SHIP_LENGTHS] --num_samples [NUM_SAMPLES] --num_of_shots [NUM_OF_SHOTS]_
What is written with capital letters should be given as arguments. If not default values will be assigned (those are the vaalues we have chosen for our report).

After running the script will:
- Create an initial grid (in our case with size 8x8) with randomly placed ships.
- Use the Monte Carlo algorithm to predict the most probable ship locations for different numbers of samplings.
- Simulate firing a fixed number of shots for each sampling scenario.
- Output the grid after each scenario, showing hits (X) and misses (O).

## Configuration

Script is created so that it can be easily configured by modifying the following parameters:
- 'grid_size': Size of the Battleship grid (default is 8).
- 'ship_lengths': Lengths of the ships (default is [3, 3, 2]).
- 'num_samples': Number of Monte Carlo samples to test (default is [100, 500, 1000, 10000, 30000]).
- 'num_of_shots': Number of shots to fire in each scenario (default is 25).
