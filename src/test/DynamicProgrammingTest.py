import pytest

from src.main.DynamicProgramming import DP

def test_2x2_max_value_2():
    grid = [[0,0],
            [1,0]]
    initial_cell = [0, 0]
    goal_cell = [1, 1]

    dp = DP()

    expected_max_val = [[2,1],[99,0]]
    value_grid = dp.calculate_value_grid(grid, initial_cell, goal_cell)
    assert expected_max_val == value_grid


def test_6x6_max_val_12():
    grid = [[0,0,1,0,0,0],
            [0,0,1,0,0,0],
            [0,0,1,0,0,0],
            [0,0,0,0,1,0],
            [0,0,1,1,1,0],
            [0,0,0,0,1,0]]

    expected_grid = [[12,11,99, 7, 6, 5],
                     [11,10,99, 6, 5, 4],
                     [10, 9,99, 5, 4, 3],
                     [ 9, 8, 7, 6,99, 2],
                     [10, 9,99,99,99, 1],
                     [11,10,11,12,99, 0]]

    initial_cell = [0,0]
    goal_cell = [5,5]

    dp = DP()

    value_grid = dp.calculate_value_grid(grid, initial_cell, goal_cell)
    assert expected_grid == value_grid








