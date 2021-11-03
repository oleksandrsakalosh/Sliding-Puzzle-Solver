import timeit
import sys

from Puzzle import *

def GreedyAlgorithm(puzzle, n, rowLen):
    """
    Searching for solution with greedy algorithm
    ----------
    Parameters
        puzzle : object type Puzzle
            Puzzle that holds starting and final state.
        n : int
            number(type) of heuristic to use.
        rowLen : int
            Lenght of one row in puzzle.
    ----------
    Return
        rightPath : list
            List of right way to final state.
        len(pastStates) : int
            Count of all explored states.
    """

    #Creating list with priority queue for possible states to observe
    #Getting heuristic score of first state and pushing them into queue
    stateQueue = []
    heurScore = getHeurScore(puzzle.startState, puzzle.goalState, n, rowLen)
    heappush(stateQueue, (heurScore, puzzle.startState))

    #Creating list with all explored states
    pastStates = []
    k = 0
    while stateQueue:#Repeating until out of moves
        priorityState = heappop(stateQueue)[1]#Getting state from queue with smallest heuristic score
        pastStates.append(priorityState)

        if priorityState == puzzle.goalState:#Check if we found final state
            k = 1
            break

        #Getting all possible moves from current state, checking if they wasn't explored earlier and pushing them into queue
        possibleStates = getPossMoves(priorityState, rowLen)
        for state in possibleStates:
            if state not in pastStates and state not in stateQueue:
                heappush(stateQueue, (getHeurScore(state, puzzle.goalState, n, rowLen), state))

    if k == 1:
        rightPath = getRightPath(pastStates, rowLen)
        return rightPath, len(pastStates)
    else:#Out of possible moves
        print("Unnable to solve the problem!")
        sys.exit()

if __name__ == '__main__':

    opt = input("If you want to type in your puzzle enter \'my\'.\nAlso you can choose from test variants. Type \'3x2\', \'3x3\', \'4x2\', \'5x2\'.\n")
    if opt == 'my':
        list1 = input("Print start state in format \'x1 x2 x3 x4 ... xn\': ")
        list1 = list(map(int, list1.split(' ')))
        list2 = input("Print goal state in format \'x1 x2 x3 x4 ... xn\': ")
        list2 = list(map(int, list2.split(' ')))
        m = int(input("Print size of row: "))
    elif opt == '3x2':
        list1 = [0, 1, 2, 3, 4, 5]
        list2 =  [3, 4, 5, 0, 1, 2]
        m = 3
    elif opt == '3x3':
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        list2 =  [8, 0, 6, 5, 4, 7, 2, 3, 1]
        m = 3
    elif opt == '4x2':
        list1 = [0, 1, 2, 3, 4, 5, 6, 7]
        list2 =  [3, 2, 5, 4, 7, 6, 1, 0]
        m = 4
    elif opt == '5x2':
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        list2 =  [4, 3, 2, 6, 1, 9, 8, 7, 5, 0]
        m = 5
    else: 
        print("Wrong input.")
        sys.exit()

    puzzle = Puzzle(list1, list2)
    printBoard(puzzle.startState, m)

    print("Starting combinated Greedy search...")
    startTime = timeit.default_timer()
    res = GreedyAlgorithm(puzzle, 3, m)
    endTime = timeit.default_timer()
    path = res[0]
    k = 0
    for state in path:
        k += 1
        print("\nDepth {}".format(k))
        printBoard(state, m)
    printBoard(puzzle.goalState, m)
    
    print("Done! Time taken: {}s".format(endTime - startTime))
    print("Total step processed: {}".format(res[1]))
    print("{} moves required.\n".format(len(path)))

    print("Starting Greedy search with first heuristic...")
    startTime = timeit.default_timer()
    res = GreedyAlgorithm(puzzle, 1, m)
    endTime = timeit.default_timer()
    path = res[0]
    k = 0
    for state in path:
        k += 1
        print("\nDepth {}".format(k))
        printBoard(state, m)
    printBoard(puzzle.goalState, m)

    print("Done! Time taken: {}s".format(endTime - startTime))
    print("Total step processed: {}".format(res[1]))
    print("{} moves required.\n".format(len(path)))

    print("Starting Greedy search with second heuristic...")
    startTime = timeit.default_timer()
    res = GreedyAlgorithm(puzzle, 2, m)
    endTime = timeit.default_timer()

    path = res[0]
    k = 0
    for state in path:
        k += 1
        print("\nDepth {}".format(k))
        printBoard(state, m)
    printBoard(puzzle.goalState, m)

    print("Done! Time taken: {}s".format(endTime - startTime))
    print("Total step processed: {}".format(res[1]))
    print("{} moves required.\n".format(len(path)))