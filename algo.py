
map = [
    ["-", "#", "-", "#", "-"],
    ["-", "-", "-", "#", "-"],
    ["-", "#", "-", "-", "-"],
    ["-", "#", "-", "#", "-"],
    ["o", "#", "#", "-", "-"],
]

queue = [(4, 0)]
end = (4,4)

totalSize = len(map[:]) * len(map[0])

def pmap():
    for row in map[:]:
        print(row)

def checkEnd(x,y):
    if (x == end[0] and y == end[1]):
        return True
    else :
        return False

def solve(map, queue, end):
    while (True):

        if len(queue) == 0:
            print("No path found")
            break
        else :
            current = queue.pop(0)

        row = current[0]
        column = current[1]

        map[row][column] = "X"

        if (checkEnd(row, column)):
            print()
            pmap()
            print("Path found")
            break

        if (row + 1 < len(map[:])): #checks bottom index
            checkDown = (map[row + 1][column] == "-")
        else:
            checkDown = False

        if (column + 1 < len(map[0][:])): #checks the right index
            checkRight = (map[row][column + 1] == "-")
        else :
            checkRight = False

        if (column - 1 > -1): #checks the left index
            checkLeft = (map[row][column - 1] == "-")
        else :
            checkLeft = False

        if (row - 1 > -1): #checks the top index
            checkTop = (map[row - 1][column] == "-")
        else :
            checkTop = False

        # checkDown = (map[row + 1][column] == "-") and row + 1 < len(map[:])
        # checkRight = (map[row][column + 1] == "-") and column + 1 < len(map[0][:])

        if (checkDown): # if down index for example is empty and equals '-' then append the coord tuple
            queue.append((row + 1, column))

        if (checkRight):
            queue.append((row, column + 1))

        if (checkTop):
            queue.append((row - 1, column))

        if (checkLeft):
            queue.append((row, column - 1))

        print(queue)
        pmap()

solve(map, queue, end)
