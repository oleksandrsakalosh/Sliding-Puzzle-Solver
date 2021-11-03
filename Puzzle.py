import copy
import math
from heapq import *


class Puzzle:
    """
    Class for m*n puzzle to solve.
    """

    def __init__(self, startState, goalState):
        """
        Initialization of class
        ----------
        Parameters
            startState : list
                First state initialized by user.
            goalState : list
                Final state to which the program should find a way.
        """
        self.startState = startState
        self.goalState = goalState

def printBoard(board, rowLen):
    """
    Function to print given board
    ----------
    Parameters
        board : list
            State of puzzle to be printed
        rowLen : int
            Lenght of one row in state
    """
    out = ''

    for i in range(rowLen):
        out+=' __'
    out += '\n|'

    for idx, val in enumerate(board):
        out += '{:>2}|'.format(val)
        if idx % rowLen == rowLen - 1 and idx != len(board) - 1:
            out += '\n|'

    out += '\n'
    for i in range(rowLen):
        out+=' ‾‾'
    out += '\n'

    print(out)

def moveLeft(board, rowLen):
    """
    Function to move square from right to empty place.
    ----------
    Parameters
        board : list
            State of puzzle to be changed
        rowLen : int
            Lenght of one row in state
    ----------
    Return
        possible : boolean
            Returns True if it possible to make move
        res : list
            New state of puzzle after move
    """
    idxEmpty = board.index(0)
    if idxEmpty % rowLen == rowLen - 1:#checks if it is possible to move square
        possible = False
    else:
        possible = True
    res = copy.deepcopy(board)

    if possible:
        res[idxEmpty] = board[idxEmpty + 1]
        res[idxEmpty + 1] = 0

    return possible, res

def moveRight(board, rowLen):
    """
    Function to move square from left to empty place.
    ----------
    Parameters
        board : list
            State of puzzle to be changed
        rowLen : int
            Lenght of one row in state
    ----------
    Return
        possible : boolean
            Returns True if it possible to make move
        res : list
            New state of puzzle after move
    """
    idxEmpty = board.index(0)
    if idxEmpty % rowLen == 0:#checks if it is possible to move square
        possible = False
    else:
        possible = True
    res = copy.deepcopy(board)

    if possible:
        res[idxEmpty] = board[idxEmpty - 1]
        res[idxEmpty - 1] = 0

    return possible, res

def moveUp(board, rowLen):
    """
    Function to move square from bottom to empty place.
    ----------
    Parameters
        board : list
            State of puzzle to be changed
        rowLen : int
            Lenght of one row in state
    ----------
    Return
        possible : boolean
            Returns True if it possible to make move
        res : list
            New state of puzzle after move
    """
    idxEmpty = board.index(0)
    if idxEmpty >= len(board) - rowLen:#checks if it is possible to move square
        possible = False
    else:
        possible = True
    res = copy.deepcopy(board)

    if possible:
        res[idxEmpty] = board[idxEmpty + rowLen]
        res[idxEmpty + rowLen] = 0

    return possible, res

def moveDown(board, rowLen):
    """
    Function to move square from top to empty place.
    ----------
    Parameters
        board : list
            State of puzzle to be changed
        rowLen : int
            Lenght of one row in state
    ----------
    Return
        possible : boolean
            True if it possible to make move
        res : list
            New state of puzzle after move
    """
    idxEmpty = board.index(0)
    if rowLen > idxEmpty:#checks if it is possible to move square
        possible = False
    else:
        possible = True
    res = copy.deepcopy(board)

    if possible:
        res[idxEmpty] = board[idxEmpty - rowLen]
        res[idxEmpty - rowLen] = 0

    return possible, res

def getPossMoves(board, m):
    """
    Function to check and get all possible moves from current state.
    ----------
    Parameters
        board : list
            State of puzzle to be changed.
        m : int
            Lenght of one row in state.
    ----------
    Return
        possibleMoves : list
            List with all possible states to get after move.
    """
    possibleMoves = []
    
    right = moveRight(board, m)
    left = moveLeft(board, m)
    down = moveDown(board, m)
    up = moveUp(board, m)

    if right[0]:
        possibleMoves.append(right[1])
    if left[0]:
        possibleMoves.append(left[1])
    if down[0]:
        possibleMoves.append(down[1])
    if up[0]:
        possibleMoves.append(up[1])

    return possibleMoves

def getHeuristic1(board, final):
    """
    Function that counts how many squares are misplaced.
    ----------
    Parameters
        board : list
            State from which to count misplaced squares.
        final : list
            Final state to compare with.
    """
    misplaced = 0

    for idx, val in enumerate(board):
        if val != final[idx]:
            misplaced+=1

    return misplaced

def getHeuristic2(board, final, rowLen):
    """
    Function that counts sum of the distances of fields from their final position.
    ----------
    Parameters
        board : list
            Current state of puzzle.
        final : list
            Final state with final position of fields.
        rowLen : int
            Lenght of one row in state.
    Return
        distance : int
            Sum of the distances of fields from their final position.
    """
    distance = 0

    for idx, val in enumerate(board):
        finVal = final.index(val)
        distance += abs(idx % rowLen - finVal % rowLen) + abs(idx // rowLen - finVal // rowLen)

    return distance

def getHeurScore(board, final, n, rowLen):
    """
    Function that calls right heuristic functions depending on the given entry.
    ----------
    Parameters
        board : list
            Current state of puzzle.
        final : list
            Final state with final position of fields.
        n : int
            Number of heuristic.
        rowLen : int
            Lenght of one row in state.
    Return
        getHeuristic1(board, final) : function
        getHeuristic2(board, final, rowLen) : function
        getHeuristic1(board, final) + getHeuristic2(board, final, rowLen) : function
    """
    if n == 1:
        return getHeuristic1(board, final)
    elif n == 2:
        return getHeuristic2(board, final, rowLen)
    else:
        return getHeuristic1(board, final) + getHeuristic2(board, final, rowLen)# Sum of points of first and second heuristics.

def getRightPath(pastStates, m):
    """
    Function that finds final way from all explored branches by filtring unvalid moves.
    ----------
    Parameters
        pastStates : list
            List that holds all traveled states.
        m : int
            Lenght of one row in state.
    Return
        rightPath : list
            List of right way to final state.
    """
    pastStates.reverse()#Reverse order of states to start from last
    
    rightPath = []
    idx = 0

    for idxList, state in enumerate(pastStates):
        if idxList >= idx and idx != len(pastStates) - 1:
            possibleMoves = getPossMoves(state, m)#Get possible moves from which we came to current state.
            i = 1

            while True:#Goes through states and find right branch from which we came
                move = pastStates[idx + i]
                if move in possibleMoves:
                    rightPath.append(move)
                    idx+=i
                    break#Stop if we found right state
                else:
                    i+=1

    rightPath.reverse()
    return rightPath