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

        if self.board["width"] - self.you["head"]["x"] == 1:    # avoid right wall
            possibleActions.remove("right")
        if self.you["head"]["x"] == 0:                          # avoid left wall
            possibleActions.remove("left")
        if self.board["height"] - self.you["head"]["y"] == 1:   # avoid ceiling
            possibleActions.remove("up")
        if self.you["head"]["y"] == 0:                          # avoid floor
            possibleActions.remove("down")

        return possibleActions

    def avoidBody(self, possibleActions: list):
        '''Avoid moves which run into your body'''

        left = {"x": self.you["head"]["x"] - 1, "y": self.you["head"]["y"]}
        right = {"x": self.you["head"]["x"] + 1, "y": self.you["head"]["y"]}
        up = {"x": self.you["head"]["x"], "y": self.you["head"]["y"] + 1}
        down = {"x": self.you["head"]["x"], "y": self.you["head"]["y"] - 1}

        if left in self.you["body"]:
            possibleActions.remove("left")
        if right in self.you["body"]:
            possibleActions.remove("right")
        if up in self.you["body"]:
            possibleActions.remove("up")
        if down in self.you["body"]:
            possibleActions.remove("down")

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
