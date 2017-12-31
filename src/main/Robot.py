
class Robot():

    delta = [[-1, 0],  # go up
             [0, -1],  # go left
             [1, 0],  # go down
             [0, 1]]  # go right

    delta_name = ['^', '<', 'v', '>']

    def isSamePosition(self, current, indexX, indexY, target):

        #g = current[indexG]

        xA = current[indexX]
        yA = current[indexY]

        xB = target[0]
        yB = target[1]

        if ( (xA == xB) and (yA == yB) ):
            return True

        return False

    def isNotAlredyInList(self, open_cells, indexX, indexY, newX, newY):

        for item in range(len(open_cells)):
            x = open_cells[item][indexX]
            y = open_cells[item][indexY]
            if (x == newX and y == newY):
                return False

        return True


    def isNotObstacle(self, grid, newX, newY):
        return (grid[newX][newY] != 1)

    def isNotOutOfGridBorders(self, grid, newX, newY):
        return ( newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) )




    def search(self, grid, initial_cell, goal_cell, cost = 1, delta = delta, delta_name = delta_name):


        x = initial_cell[0]
        y = initial_cell[1]
        g = 0



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

            if (self.isSamePosition(open_cells[0], 1,2, goal_cell)):
                target = open_cells[0]
                target_found = True

            for index in range(len(delta)):
                newX = open_cells[0][1] + delta[index][0]
                newY = open_cells[0][2] + delta[index][1]

                if ( self.isNotOutOfGridBorders(grid, newX, newY)):
                    if ( self.isNotObstacle(grid, newX, newY)):
                        if ( self.isNotAlredyInList(open_cells, 1,2, newX, newY)): #openCell
                            if (self.isNotAlredyInList(checked_cells, 1,2, newX, newY)): #extendedCells
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




    # heuristic search (A-star)
    def search_heuristic(self, grid, heuristic, initial_cell, goal_cell, cost=1, delta=delta, delta_name=delta_name):

        x = initial_cell[0]
        y = initial_cell[1]
        g = 0
        h = heuristic[x][y]
        f = g + h


        open_cells = [(f, g, h, x, y)]
        checked_cells = []

        counter = 0
        expanded_cells = [[-1 for row_cell in range(len(grid[0]))] for row in range(len(grid))]
        expanded_cells[x][y] = counter

        actions = [[-1 for row_cell in range(len(grid[0]))] for row in range(len(grid))]

        target_found = False
        all_grid_searched = False

        while ((not target_found) and (not all_grid_searched)):

            # increment path length when all open cells with this g consumed
            if (g == open_cells[0][1]):
                g += cost

            if (self.isSamePosition(open_cells[0], 3,4, goal_cell)):
                target = open_cells[0]
                target_found = True

            for index in range(len(delta)):
                newX = open_cells[0][3] + delta[index][0]
                newY = open_cells[0][4] + delta[index][1]

                if (self.isNotOutOfGridBorders(grid, newX, newY)):
                    if (self.isNotObstacle(grid, newX, newY)):
                        if (self.isNotAlredyInList(open_cells, 3,4,newX, newY)):  # openCell
                            if (self.isNotAlredyInList(checked_cells, 3,4, newX, newY)):  # extendedCells
                                h = heuristic[newX][newY]
                                f = g + h
                                open_cells.append((f, g, h, newX, newY))
                                counter = counter + 1
                                expanded_cells[newX][newY] = counter
                                actions[newX][newY] = index

            checked_cells.append(open_cells[0])
            open_cells.pop(0)

            open_cells.sort()


            if (len(open_cells) == 0):
                all_grid_searched = True

        print("expanded_cells")
        for i in range(len(expanded_cells)):
            print(expanded_cells[i])

        policy = [[' ' for row_cell in range(len(grid[0]))] for row in range(len(grid))]
        x = goal_cell[0]
        y = goal_cell[1]
        policy[x][y] = '*'
        while not (x == initial_cell[0] and y == initial_cell[1]):
            previous_x = x - delta[actions[x][y]][0]
            previous_y = y - delta[actions[x][y]][1]
            #print(x,y,delta_name[actions[x][y]],previous_x,previous_y )
            policy[previous_x][previous_y] = delta_name[actions[x][y]]
            #print(policy[previous_x][previous_y])

            x = previous_x
            y = previous_y

        print("actions")
        for i in range(len(actions)):
            print(actions[i])

        print("policy")
        for i in range(len(policy)):
            print(policy[i])

        if target_found:
            return target
        else:
            return "Failed!"

