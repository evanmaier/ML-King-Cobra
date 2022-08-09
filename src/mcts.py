from mcts import mcts


class State():
    def __init__(self, data: dict):
        self.game = data["game"]
        self.board = data["board"]
        self.you = data["you"]

    def getPossibleActions(self):
        '''Returns an iterable of all actions which can be taken from this state'''
        possibleActions = ["up", "down", "left", "right"]
        self.avoidWalls(possibleActions)
        self.avoidBody(possibleActions)
        return possibleActions

    def avoidWalls(self, possibleActions: list):
        '''Avoid moves which run into walls'''

        return possibleActions

    def avoidBody(self, possibleActions: list):
        '''Avoid moves which run into your body'''

        return possibleActions

    def takeAction(self, action):
        '''Returns the state which results from taking action (action)'''

    def isTerminal(self):
        '''Returns whether this state is a terminal state'''

    def getReward(self):
        '''Returns the reward for this state. Only needed for terminal states.'''


def run(data: dict):
    initialState = State(data)
    searcher = mcts(timeLimit=data["game"]["timeout"])
    action = searcher.search(initialState=initialState)
    return action
