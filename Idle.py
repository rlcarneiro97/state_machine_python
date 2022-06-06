from os import stat
from State import State

class Idle(State):

    def __init__(self, state):
        super().__init__(state)

    def getState(self):
        return super().getState()

    def setState(self, state):
        return super().setState(state)

    def setTransition(self, current_state, state_list):
        return super().setTransition(current_state, state_list)

    def applyState(self):
        print(__name__)