from copy import deepcopy
from inspect import istraceback
from mcts import mcts
import logging


class State():
    def __init__(self, data: dict):
        self.snake = data['you']['body']
        self.head = data['you']['head']
        self.health = data['you']['health']
        self.food = data['board']['food']
        self.turn = data['turn']
        self.board = {'width': data['board']['width'],
                      'height': data['board']['height']}
        self.currentPlayer = 1

    def getCurrentPlayer(self):
        '''Return current player value'''
        return self.currentPlayer

    def getPossibleActions(self):
        '''Returns an iterable of all actions which can be taken from this state'''

        possibleActions = ['up', 'down', 'left', 'right']
        self.avoidWalls(possibleActions)
        self.avoidBody(possibleActions)
        return possibleActions

    def avoidWalls(self, possibleActions: list):
        '''Avoid moves which run into walls'''

        if self.board['width'] - self.head['x'] == 1:    # avoid right wall
            possibleActions.remove('right')
        if self.head['x'] == 0:                          # avoid left wall
            possibleActions.remove('left')
        if self.board['height'] - self.head['y'] == 1:   # avoid ceiling
            possibleActions.remove('up')
        if self.head['y'] == 0:                          # avoid floor
            possibleActions.remove('down')

        return possibleActions

    def avoidBody(self, possibleActions: list):
        '''Avoid moves which run into your body'''

        left = {'x': self.head['x'] - 1, 'y': self.head['y']}
        right = {'x': self.head['x'] + 1, 'y': self.head['y']}
        up = {'x': self.head['x'], 'y': self.head['y'] + 1}
        down = {'x': self.head['x'], 'y': self.head['y'] - 1}

        snakeNoTail = deepcopy(self.snake)
        snakeNoTail.pop()

        if left in snakeNoTail:
            possibleActions.remove('left')
        if right in snakeNoTail:
            possibleActions.remove('right')
        if up in snakeNoTail:
            possibleActions.remove('up')
        if down in snakeNoTail:
            possibleActions.remove('down')

        return possibleActions

    def takeAction(self, action):
        '''Returns the state which results from taking action (action)'''

        nextState = deepcopy(self)
        # apply action
        if action == 'up':
            nextState.head['y'] += 1

        elif action == 'down':
            nextState.head['y'] -= 1

        elif action == 'right':
            nextState.head['x'] += 1

        elif action == 'left':
            nextState.head['x'] -= 1

        else:
            raise Exception("Invalid Action!")

        # move head
        nextState.snake.insert(0, nextState.head)

        # move tail
        nextState.snake.pop()

        # eat food
        if nextState.head in nextState.food:
            nextState.health = 100
            nextState.food.remove(nextState.head)
            nextState.snake.insert(len(nextState.snake), nextState.snake[-1])
        else:
            nextState.health -= 1

        # update turn
        nextState.turn += 1

        # return new state
        return nextState

    def isTerminal(self):
        '''Returns whether this state is a terminal state'''

        if not self.getPossibleActions():
            return True

        if self.health == 0:
            return True

        return False

    def getReward(self):
        '''Returns the reward for this state'''
        if self.isTerminal():
            return self.turn
        else:
            return 1000000


def run(data: dict, debug=False):
    initialState = State(data)
    searcher = mcts(timeLimit=250)
    if debug:
        try:
            action = searcher.search(
                initialState=initialState, needDetails=True)
        except IndexError:
            print('No moves available')
            return 'up'
    else:
        try:
            action = searcher.search(initialState=initialState)
        except IndexError:
            print('No moves available')
            return 'up'
    return action
