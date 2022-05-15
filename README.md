# INTRODUCTION

This is the game of life, developed by the mathematician **John Horton Conway**, who proposed a world confined to a two-dimensional grid, where each cell could take two states: alive or dead. The state of each cell would then depend on each iteration of the eight neighboring cells, fulfilling these simple rules:

1. A dead cell with exactly **three living neighbor cells** will come back to life.
2. A living cell with **two or three living neighbors** will continue to live.
3. Otherwise, it will die from **loneliness** or **overpopulation**.

## DEPLOYMENT

This game is developed in Python with the [Numpy](https://numpy.org/ "Numpy") and [Pygame](https://www.pygame.org/ "Pygame") libraries.

You need to install these libraries with `pip install` in order to run the game.