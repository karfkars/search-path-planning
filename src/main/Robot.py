
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

            checked_cells.append(open_cells[0])
            open_cells.pop(0)


            if (len(open_cells) == 0):
                all_grid_searched = True

            print("-------------")
            print(checked_cells)
            print(open_cells)
            print(target_found)
            print(all_grid_searched)
            print("-------------")


        if target_found: return target
        else: return "Failed!"
