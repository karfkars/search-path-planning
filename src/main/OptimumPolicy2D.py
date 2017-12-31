
class OptimumPolicy():


    forward  = [ [-1,  0],  # go up
                 [ 0, -1],  # go left
                 [ 1,  0],    # go down
                 [ 0,  1]]  # go right

    forward_names = ['up', 'left', 'down', 'right']

    actions = [-1, 0, 1]
    action_names = ['R','#','L']

    cost = [2, 1, 10]


    def isNotObstacle(self, grid, newX, newY):
        return (grid[newX][newY] != 1)

    def isNotOutOfGridBorders(self, grid, newX, newY):
        return ( newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) )



    def calculate(self,
                  grid, starting_cell, finishing_cell,
                  cost = cost,
                  forward = forward, forward_names = forward_names,
                  actions = actions, action_names = action_names):

        value3D = [ [[999 for row_cell in range(len(grid[0]))] for row in range(len(grid))],
                  [[999 for row_cell in range(len(grid[0]))] for row in range(len(grid))],
                  [[999 for row_cell in range(len(grid[0]))] for row in range(len(grid))],
                  [[999 for row_cell in range(len(grid[0]))] for row in range(len(grid))]]

        policy3D = [ [[' ' for row_cell in range(len(grid[0]))] for row in range(len(grid))],
                     [[' ' for row_cell in range(len(grid[0]))] for row in range(len(grid))],
                     [[' ' for row_cell in range(len(grid[0]))] for row in range(len(grid))],
                     [[' ' for row_cell in range(len(grid[0]))] for row in range(len(grid))]]

        policy2D = [[' ' for row in range(len(grid[0]))] for row in range(len(grid))]

        changed = True
        while changed:
            changed = False



            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    for orientation in range(4):

                        if x == finishing_cell[1] and y == finishing_cell[2]:
                            if value3D[orientation][x][y] > 0:
                                value3D[orientation][x][y] = 0
                                changed = True
                                policy3D[orientation][x][y] = '*'

                        elif grid[x][y] == 0:

                            for index in range(len(actions)):

                                orientation_new = ( orientation + actions[index] ) % 4
                                x_new = x + forward[orientation_new][0]
                                y_new = y + forward[orientation_new][1]

                                if self.isNotOutOfGridBorders(grid, x_new, y_new):
                                    if self.isNotObstacle(grid, x_new, y_new):
                                        value_new = value3D[orientation_new][x_new][y_new] + cost[index]

                                        if value_new < value3D[orientation][x][y]:
                                            value3D[orientation][x][y] = value_new
                                            changed = True
                                            policy3D[orientation][x][y] = action_names[index]


        x = starting_cell[1]
        y = starting_cell[2]
        orientation = starting_cell[0]

        policy2D[x][y] = policy3D[orientation][x][y]
        while policy3D[orientation][x][y] != '*':
            if policy3D[orientation][x][y] == '#':
                orientation_new = orientation
            elif policy3D[orientation][x][y] == 'R':
                orientation_new = (orientation - 1) % 4
            elif policy3D[orientation][x][y] == 'L':
                orientation_new = (orientation + 1) % 4

            x = x + forward[orientation_new][0]
            y = y + forward[orientation_new][1]
            orientation = orientation_new

            policy2D[x][y] = policy3D[orientation][x][y]



        print("policy2D:")
        for index in range(len(policy2D)):
            print(policy2D[index])

        return policy2D