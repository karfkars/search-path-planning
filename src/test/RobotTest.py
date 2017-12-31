import pytest

from src.main.Robot import Robot


def test_isSamePosition():
    currnet_open_cell = (0,0,0)
    goal_cell = [0, 0]
    robot = Robot()

    expected = True
    actual = robot.isSamePosition(currnet_open_cell, goal_cell)

    assert expected == actual




def test_search_1x1_distance_is_0():
    grid = [[0]]
    initial_cell = [0, 0]
    goal_cell = [0, 0]


    robot = Robot()

    expected = (0,0,0)
    actual = robot.search(grid, initial_cell, goal_cell)
    assert expected == actual


def test_search_2x2_distance_is_1():
    grid = [ [ 0, 1],
             [ 0, 1]]

    initial_cell = [0, 0]
    goal_cell = [1, 0]
    robot = Robot()

    expected = (1, 1, 0) # distance is 1, coordinates [1,0]
    actual = robot.search(grid, initial_cell, goal_cell)
    assert expected == actual


def test_search_3x3_distance_unreachable_because_of_obstacle():
    grid = [[0,1,0],
            [0,1,0],
            [0,1,0]]

    initial_cell = [0,0]
    goal_cell = [2,2]

    robot = Robot()

    expected = "Failed!"
    actual = robot.search(grid, initial_cell, goal_cell)
    assert expected == actual

def test_search_5x6_distance_is_11():
    grid = [[0,0,1,0,0,0],
            [0,0,1,0,0,0],
            [0,0,0,0,1,0],
            [0,0,1,1,1,0],
            [0,0,0,0,1,0]]

    initial_cell = [0,0]
    goal_cell = [4,5]

    robot = Robot()

    expected = (11, 4, 5)
    actual = robot.search(grid, initial_cell, goal_cell)
    assert expected == actual

def test_search_5x6_distance_is_11():
    grid = [[0,0,1,0,0,0],
            [0,0,1,0,0,0],
            [0,0,0,0,1,0],
            [0,0,1,1,1,0],
            [0,0,0,0,1,0]]

    initial_cell = [4,1]
    goal_cell = [1,4]

    robot = Robot()

    expected = (6, 1, 4)
    actual = robot.search(grid, initial_cell, goal_cell)
    assert expected == actual




