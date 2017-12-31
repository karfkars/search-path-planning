
class Robot():

    delta = [[-1, 0],  # go up
             [0, -1],  # go left
             [1, 0],  # go down
             [0, 1]]  # go right

    delta_name = ['^', '<', 'v', '>']

    def isSamePosition(self, current, target):

        g = current[0]
        xA = current[1]
        yA = current[2]

        xB = target[0]
        yB = target[1]

        if ( (xA == xB) and (yA == yB) ):
            return True

        return False

    def isNotAlredyInList(self, open_cells, newX, newY):

        for item in range(len(open_cells)):
            x = open_cells[item][1]
            y = open_cells[item][2]
            if (x == newX and y == newY):
                return False

        return True


    def isNotObstacle(self, grid, newX, newY):
        return (grid[newX][newY] != 1)

    def isNotOutOfGridBorders(self, grid, newX, newY):
        return ( newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) )




    def search(self, grid, initial_cell, goal_cell, cost = 1, delta = delta, delta_name = delta_name):
        g = 0
        x = initial_cell[0]
        y = initial_cell[1]



        open_cells = [(g,x,y)]
        checked_cells = []

        counter = 0
        expanded_cells = [[-1 for row_cell in range(len(grid[0]))] for row in range(len(grid))]
        expanded_cells[x][y] = counter

        actions = [[-1 for row_cell in range(len(grid[0]))] for row in range(len(grid))]

        target_found = False
        all_grid_searched = False

        while ( (not target_found) and (not all_grid_searched) ):

            # increment path length when all open cells with this g consumed
            if ( g == open_cells[0][0]):
                g += cost

            if (self.isSamePosition(open_cells[0], goal_cell)):
                target = open_cells[0]
                target_found = True

            for index in range(len(delta)):
                newX = open_cells[0][1] + delta[index][0]
                newY = open_cells[0][2] + delta[index][1]

                if ( self.isNotOutOfGridBorders(grid, newX, newY)):
                    if ( self.isNotObstacle(grid, newX, newY)):
                        if ( self.isNotAlredyInList(open_cells, newX, newY)): #openCell
                            if (self.isNotAlredyInList(checked_cells, newX, newY)): #extendedCells
                                open_cells.append((g, newX, newY))
                                counter = counter + 1
                                expanded_cells[newX][newY] = counter
                                actions[newX][newY] = index

            checked_cells.append(open_cells[0])
            open_cells.pop(0)


            if (len(open_cells) == 0):
                all_grid_searched = True


        print()
        for i in range(len(expanded_cells)):
                print(expanded_cells[i])

        policy = [[' ' for row_cell in range(len(grid[0]))] for row in range(len(grid))]
        x = goal_cell[0]
        y = goal_cell[1]
        policy[x][y] = '*'
        while not (x == initial_cell[0] and y == initial_cell[1]):
            previous_x = x - delta[actions[x][y]][0]
            previous_y = y - delta[actions[x][y]][1]

            policy[previous_x][previous_y] = delta_name[actions[x][y]]
            print(policy[previous_x][previous_y])

            x = previous_x
            y = previous_y

        print()
        for i in range(len(actions)):
            print(actions[i])

        print()
        for i in range(len(policy)):
            print(policy[i])

        if target_found: return target
        else: return "Failed!"

