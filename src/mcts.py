from mcts import mcts

class State():
  def __init__(self, data: dict):
    self.game = data["game"]
    self.board = data["board"]
    self.you = data["you"]

  def getPossibleActions(self):
    '''Returns an iterable of all actions which can be taken from this state'''

  def takeAction(self, action):
    '''Returns the state which results from taking action (action)'''

  def isTerminal(self):
    '''Returns whether this state is a terminal state'''

class Action():
  def __init__(self, move: str):
    self.move = move

def run(data: dict):
  initialState = State(data)
  searcher = mcts(timeLimit=data["game"]["timeout"])
  action = searcher.search(initialState=initialState)
  return action
