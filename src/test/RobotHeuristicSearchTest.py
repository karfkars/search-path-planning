import pytest

from src.main.Robot import Robot




def test_heuristic_search():
    grid = [[0,1,0,0,0,0],
            [0,1,0,0,0,0],
            [0,1,0,0,0,0],
            [0,1,0,0,0,0],
            [0,0,0,0,0,0]]

    heuristic = [[9,8,7,6,5,4],
                 [8,7,6,5,4,3],
                 [7,5,5,4,3,2],
                 [6,5,4,3,2,1],
                 [5,4,3,2,1,0]]

    initial_cell = [0,0]
    goal_cell = [4,5]

    robot = Robot()

    expected = (9, 9, 0, 4, 5)
    actual = robot.search_heuristic(grid, heuristic, initial_cell, goal_cell)
    assert expected == actual

