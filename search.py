# George Wang
#
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from builtins import object
import util


class SearchProblem(object):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    problem.getStartState(): returns a pair (tuple of size 2) that represents
    the coordinate of where the pacman starts

    problem.isGoalState((x, y)): returns a boolean True/False based on whether
    the coordinate (x, y) is a goal state.

    problem.getSuccessors((x, y)): given a position (x, y), returns a list of
    triples (list of tuples, with each tuple being size 3) of the successor
    positions of pacman.
    The tuple consists of position, action required to get to it, and the step
    cost i.e. ((35,2), 'North', 1).

    For the search functions, you are required to return a list of actions
    (that is, a list of strings such as ['North', 'North', 'West'])

    """
    "*** YOUR CODE HERE ***"

    # visited is a dictionary with location:([path], cost) pairs
    # i realize now that cost is kinda unnecessary lmao. whoops
    visited = {}
    stack = util.Stack()

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []
    stack.push((startState, '', 0))
    # response are dictionaries for finding prev
    response = {"North": (0, -1), "South": (0, 1), "East": (-1, 0), "West": (1, 0)}

    # Main loop
    while not stack.isEmpty():
        # Pop from stack - node is (location, direction, cost)
        node = stack.pop()
        visited[node[0]] = (node[1], node[2])

        # Managing successors
        for s in problem.getSuccessors(node[0]):
            # Check goal state on creation
            if problem.isGoalState(s[0]):
                get = response[s[1]]
                back = (s[0][0] + get[0], s[0][1] + get[1])
                path = [s[1]]
                cost = s[2]
                while back != startState:
                    path.append(visited[back][0])
                    cost += visited[back][1]
                    get = response[visited[back][0]]
                    back = (back[0] + get[0], back[1] + get[1])
                path.reverse()
                return path

            # Check if s in frontier (stack)
            inFrontier = False
            for f in stack.list:
                if s[0] == f[0]:
                    inFrontier = True
            # Put in stack if not visited or in frontier
            if (not s[0] in visited) and (not inFrontier):
                stack.push(s)
    return None


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # visited is a dictionary with location:([path], cost) pairs
    visited = {}
    stack = util.Queue()

    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []
    stack.push((startState, '', 0))
    # response are dictionaries for finding prev
    response = {"North": (0, -1), "South": (0, 1), "East": (-1, 0), "West": (1, 0)}

    # Main loop
    while not stack.isEmpty():
        # Pop from stack - node is (location, direction, cost)
        node = stack.pop()
        visited[node[0]] = (node[1], node[2])

        # Managing successors
        for s in problem.getSuccessors(node[0]):
            # Check goal state on creation
            if problem.isGoalState(s[0]):
                get = response[s[1]]
                back = (s[0][0] + get[0], s[0][1] + get[1])
                path = [s[1]]
                cost = s[2]
                while back != startState:
                    path.append(visited[back][0])
                    cost += visited[back][1]
                    get = response[visited[back][0]]
                    back = (back[0] + get[0], back[1] + get[1])
                path.reverse()
                return path

            # Check if s in frontier (stack)
            inFrontier = False
            for f in stack.list:
                if s[0] == f[0]:
                    inFrontier = True
            # Put in stack if not visited or in frontier
            if (not s[0] in visited) and (not inFrontier):
                stack.push(s)
    return None


def iterativeDeepeningSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    Please use a maximum depth limit of 1000
    """
    "*** YOUR CODE HERE ***"
    # Goal is checked on creation, so we need to check start state
    startLocation = problem.getStartState()
    if problem.isGoalState(startLocation):
        return []

    # Max depth limit of 1000
    for limit in range(1, 1001):
        answer = searchLevel(problem, startLocation, 0, limit, [])
        if answer != "F":
            return answer
    return None


def searchLevel(problem, location, level, limit, path):
    successors = problem.getSuccessors(location)
    # Iterating through successors backwards to simulate a stack
    successors.reverse()
    for s in successors:  # (location, direction, cost)
        # Goal test on creation
        if problem.isGoalState(s[0]):
            path.append(s[1])
            return path

        # If successor is at limit and isn't goal state, do nothing
        if level + 1 != limit:
            # Add to path
            newPath = path
            newPath.append(s[1])
            # Recursion
            answer = searchLevel(problem, s[0], level + 1, limit, newPath)
            if answer != "F":
                return answer
            # Remove from path
            path.pop(-1)

    return "F"


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = {}  # Stores things as - location:(direction, total cost)
    frontInfo = {}  # Frontier items - location:(direction, total cost)
    frontier = util.PriorityQueue()  # Items are (location)
    startState = problem.getStartState()
    frontier.push(startState, 0)
    frontInfo[startState] = ("", 0)
    # backtrack is a dictionary for backtracking
    backtrack = {"North": (0, -1), "South": (0, 1), "East": (-1, 0), "West": (1, 0)}

    # Main loop
    while not frontier.isEmpty():
        visiting = frontier.pop()  # (location)
        visitInfo = frontInfo[visiting]  # (direction, total cost)
        if visiting == startState:
            # Stores - startState:('', 0)
            visited[startState] = (visitInfo[0], visitInfo[1])
        else:  # Backtracks by one to get the total cost of the previous node
            back = backtrack[visitInfo[0]]
            prev = (visiting[0] + back[0], visiting[1] + back[1])
            prevCost = visited[prev][1]
            # Stores - location:(direction, prevCost + cost)
            visited[visiting] = (visitInfo[0], visitInfo[1])

        # Goal check on expansion
        if problem.isGoalState(visiting):
            back = backtrack[visitInfo[0]]
            prev = (visiting[0] + back[0], visiting[1] + back[1])
            path = [visitInfo[0]]
            while prev != startState:
                path.append(visited[prev][0])
                back = backtrack[visited[prev][0]]
                prev = (prev[0] + back[0], prev[1] + back[1])
            path.reverse()
            return path

        # Managing successors
        for s in problem.getSuccessors(visiting):  # (location, direction, cost)
            if not s[0] in visited:
                # If s[0] is already in frontier and new total cost would be greater, do nothing
                sucCost = visited[visiting][1] + s[2]
                if not (s[0] in frontInfo and sucCost >= frontInfo[s[0]][1]):
                    frontInfo[s[0]] = (s[1], sucCost)
                frontier.update(s[0], sucCost)

    return None


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the
    nearest goal in the provided SearchProblem.  This heuristic is trivial.
    Please do not modify this.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = {}  # Stores things as - location:(direction, total cost)
    frontInfo = {}  # Frontier items - location:(direction, total cost)
    frontier = util.PriorityQueue()  # Items are (location)
    startState = problem.getStartState()
    frontier.push(startState, 0)
    frontInfo[startState] = ("", 0)
    # backtrack is a dictionary for backtracking
    backtrack = {"North": (0, -1), "South": (0, 1), "East": (-1, 0), "West": (1, 0)}

    # Main loop
    while not frontier.isEmpty():
        visiting = frontier.pop()  # (location)
        visitInfo = frontInfo[visiting]  # (direction, total cost)
        if visiting == startState:
            # Stores - startState:('', 0)
            visited[startState] = (visitInfo[0], visitInfo[1])
        else:  # Backtracks by one to get the total cost of the previous node
            back = backtrack[visitInfo[0]]
            prev = (visiting[0] + back[0], visiting[1] + back[1])
            prevCost = visited[prev][1]
            # Stores - location:(direction, prevCost + cost)
            visited[visiting] = (visitInfo[0], visitInfo[1])

        # Goal check on expansion
        if problem.isGoalState(visiting):
            back = backtrack[visitInfo[0]]
            prev = (visiting[0] + back[0], visiting[1] + back[1])
            path = [visitInfo[0]]
            while prev != startState:
                path.append(visited[prev][0])
                back = backtrack[visited[prev][0]]
                prev = (prev[0] + back[0], prev[1] + back[1])
            path.reverse()
            return path

        # Managing successors
        for s in problem.getSuccessors(visiting):  # (location, direction, cost)
            if not s[0] in visited:
                # If s[0] is already in frontier and new total cost would be greater, do nothing
                sucCost = visited[visiting][1] + s[2] + heuristic(s[0], problem)
                if not (s[0] in frontInfo and sucCost >= frontInfo[s[0]][1]):
                    frontInfo[s[0]] = (s[1], sucCost)
                frontier.update(s[0], sucCost)

    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ids = iterativeDeepeningSearch
astar = aStarSearch
ucs = uniformCostSearch
