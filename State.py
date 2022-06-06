import abc

class State(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, state):
        self._state = state

    @abc.abstractmethod
    def getState(self):
        return self._state

    @abc.abstractmethod
    def setState(self, state):
        self._state = state

    @abc.abstractmethod
    def setTransition(self, current_state, state_list):
        current_state = self.getState()
        return current_state

    @abc.abstractmethod
    def applyState(self):
        pass