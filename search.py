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

import util

class SearchProblem:
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
    return  [s, s, w, s, w, w, s, w]

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
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Stack()
    explored = set()
    cur = problem.getStartState()
    hashtable = {cur:[]}
    frontier.push(cur)
    

    while not frontier.isEmpty():
        cur = frontier.pop()
        explored.add(cur)
        if problem.isGoalState(cur):
   		    #print hashtable[cur]
   		    return hashtable[cur]
        for nextPoint in problem.getSuccessors(cur):
   		    if not nextPoint[0] in explored:
   		 		frontier.push(nextPoint[0])
   		 		path = []
   		 		path = list(hashtable[cur])
   		 		path.append(nextPoint[1])
   		 		hashtable[nextPoint[0]] = path
   		 

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    explored = set()
    cur = problem.getStartState()
    hashtable = {cur:[]}
    frontier.push(cur)

    while not frontier.isEmpty():
        cur = frontier.pop()
        explored.add(cur)
        if problem.isGoalState(cur):
        	return hashtable[cur]
        for nextPoint in problem.getSuccessors(cur):
        	if not nextPoint[0] in explored:
        		frontier.push(nextPoint[0])
			# add node into explored everytime we push it into the queue to avoid duplicate
        		explored.add(nextPoint[0]) 
        		path = []
        		path = list(hashtable[cur])
        		path.append(nextPoint[1])
        		hashtable[nextPoint[0]] = path

    return []
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    frontier = util.PriorityQueue()
    explored = set()
    infronter = set()
    cur = problem.getStartState()
    hashtable = {cur:[]}
    frontier.push(cur, 0) #the queue will keep pairs of node and node's cost

    while not frontier.isEmpty():
    	cur = frontier.pop()
    	#print "cur is ", cur
    	if problem.isGoalState(cur):
    		return hashtable[cur]
    	explored.add(cur)    
    	for nextPoint in problem.getSuccessors(cur):
    		#print "cur is now ", cur, "next point [0] is ", nextPoint[0]
    		if not (nextPoint[0] in explored or nextPoint[0] in infronter): 
                #print nextPoint[0], "get there"
    			path = []
    			path = list(hashtable[cur])
    			path.append(nextPoint[1])
    			hashtable[nextPoint[0]] = path
    			#print "hashtable key is ", nextPoint[0], "path is ", path
    			#explored.add(nextPoint[0])
    			infronter.add(nextPoint[0])
    			#print problem.getCostOfActions(path)
    			frontier.push(nextPoint[0], problem.getCostOfActions(path))
    			#print frontier
     		elif nextPoint[0] in infronter:
    			path = []
    			path = list(hashtable[cur])
    			path.append(nextPoint[1])
    			#print path
    			if (problem.getCostOfActions(hashtable[nextPoint[0]]) > problem.getCostOfActions(path)):
					frontier.push(nextPoint[0],problem.getCostOfActions(path))
					hashtable[nextPoint[0]] = path
			
    return []
 
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    frontier = util.PriorityQueue()
    explored = set()
    infronter = set()
    cur = problem.getStartState()
    hashtable = {cur:[]}
    frontier.push(cur, 0) #the queue will keep pairs of node and node's cost

    while not frontier.isEmpty():
    	cur = frontier.pop()
    	#print "cur is ", cur
    	if problem.isGoalState(cur):
    		return hashtable[cur]
    	explored.add(cur)    
    	for nextPoint in problem.getSuccessors(cur):
    		#print "cur is now ", cur, "next point [0] is ", nextPoint[0]
    		if not (nextPoint[0] in explored or nextPoint[0] in infronter): 
                #print nextPoint[0], "get there"
    			path = []
    			path = list(hashtable[cur])
    			path.append(nextPoint[1])
    			hashtable[nextPoint[0]] = path
    			#print "hashtable key is ", nextPoint[0], "path is ", path
    			#explored.add(nextPoint[0])
    			infronter.add(nextPoint[0])
    			#print problem.getCostOfActions(path)
    			frontier.push(nextPoint[0], problem.getCostOfActions(path)+heuristic(nextPoint[0],problem))
    			#print frontier
     		elif nextPoint[0] in infronter:
    			path = []
    			path = list(hashtable[cur])
    			path.append(nextPoint[1])
    			#print path
    			if (problem.getCostOfActions(hashtable[nextPoint[0]])+heuristic(nextPoint[0],problem) > problem.getCostOfActions(path)+heuristic(nextPoint[0],problem)):
					frontier.push(nextPoint[0],problem.getCostOfActions(path)+heuristic(nextPoint[0],problem))
					hashtable[nextPoint[0]] = path
			
    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
