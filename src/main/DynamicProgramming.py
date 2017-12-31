
class DP():

    delta = [[-1, 0],  # go up
             [0, -1],  # go left
             [1, 0],  # go down
             [0, 1]]  # go right

    delta_name = ['^', '<', 'v', '>']

    cost = 1

    def isNotObstacle(self, grid, newX, newY):
        return (grid[newX][newY] != 1)

    def isNotOutOfGridBorders(self, grid, newX, newY):
        return ( newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) )

    def calculate_value_grid(self, grid, initial_cell, goal_cell, cost = cost, delta = delta, delta_name = delta_name):

        value_grid = [[99 for row_cell in range(len(grid[0]))] for row in range(len(grid))]
        policy = [[' ' for row in range(len(grid[0]))] for row in range(len(grid))]

        change = True
        while change:
            change = False

            for x in range(len(grid)):
                for y in range(len(grid[0])):

                    if ((x == goal_cell[0]) and (y == goal_cell[1])):
                        if (value_grid[x][y] != 0):
                            value_grid[x][y] = 0
                            change = True
                            policy[x][y] = '*'


                    elif grid[x][y] == 0:

                        for index in range(len(delta)):
                            x_new = x + delta[index][0]
                            y_new = y + delta[index][1]

                            if self.isNotOutOfGridBorders(grid, x_new, y_new):
                                if self.isNotObstacle(grid, x_new, y_new):

                                    cost_to_finish = value_grid[x_new][y_new] + cost

                                    if value_grid[x][y] > cost_to_finish:
                                        value_grid[x][y] = cost_to_finish
                                        change = True
                                        policy[x][y] = delta_name[index]



        print("value grid:")
        for index in range(len(value_grid)):
            print(value_grid[index])

        print("policy grid:")
        for index in range(len(policy)):
            print(policy[index])

        return value_grid

