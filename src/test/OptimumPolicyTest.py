from src.main.OptimumPolicy2D import OptimumPolicy


def test_turnLeft():
    grid = [[0,0],
            [1,0]]

    #direction, row, col
    starting_cell = [0, 1, 1]
    finishing_cell = [3, 0, 0]

    policy = OptimumPolicy()

    expected_optimum_policy = [['*','L'],[' ','#']]
    actual_optimum_policy = policy.calculate(grid, starting_cell, finishing_cell)
    assert expected_optimum_policy == actual_optimum_policy

def test_turnLeft_5x6():
    grid = [[1,1,1,0,0,0],
            [1,1,1,0,1,0],
            [0,0,0,0,0,0],
            [1,1,1,0,1,1],
            [1,1,1,0,1,1]]
    #direction, row, col
    starting_cell = [0, 4, 3]
    finishing_cell = [3, 2, 0]

    policy = OptimumPolicy()

    expected_optimum_policy = [[' ', ' ', ' ', ' ', ' ', ' '],
                               [' ', ' ', ' ', ' ', ' ', ' '],
                               ['*', '#', '#', 'L', ' ', ' '],
                               [' ', ' ', ' ', '#', ' ', ' '],
                               [' ', ' ', ' ', '#', ' ', ' ']]

    actual_optimum_policy = policy.calculate(grid, starting_cell, finishing_cell)
    assert expected_optimum_policy == actual_optimum_policy


def test_turnLeft_5x6_left_too_expensive():
    grid = [[1,1,1,0,0,0],
            [1,1,1,0,1,0],
            [0,0,0,0,0,0],
            [1,1,1,0,1,1],
            [1,1,1,0,1,1]]
    #direction, row, col
    starting_cell = [0, 4, 3]
    finishing_cell = [3, 2, 0]

    cost = [2, 1, 20]

    policy = OptimumPolicy()

    expected_optimum_policy = [[' ', ' ', ' ', 'R', '#', 'R'],
                               [' ', ' ', ' ', '#', ' ', '#'],
                               ['*', '#', '#', '#', '#', 'R'],
                               [' ', ' ', ' ', '#', ' ', ' '],
                               [' ', ' ', ' ', '#', ' ', ' ']]

    actual_optimum_policy = policy.calculate(grid, starting_cell, finishing_cell, cost)
    assert expected_optimum_policy == actual_optimum_policy

