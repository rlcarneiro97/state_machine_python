class StateMachine:

    def __init__(self, states=[]):
        self._sensor = 1
        self._current_state = 1
        self._states = states

    def getSensor(self):
        return self._sensor

    def setSensor(self, sensor):
        self._sensor = sensor

    def getCurrentState(self):
        return self._current_state

    def setCurrentState(self, current_state):
        self._current_state = current_state

    def getStates(self):
        return self._states

    def setStates(self, states):
        self._states = states

    def setUniqueState(self, state):
        self._states.append(state)

    def _printCurrentState(self, current_state, state_list):

        for elem in state_list:
            if current_state == elem.getState():
                elem.applyState()
                return True
        return False

    def runApplication(self):

        sensor = self.getCurrentState()
        state_list = self.getStates()

        while sensor != 0:

            sensor = int(input("Digite um estímulo: "))

            for state in state_list:
                if sensor == state.getState():
                    current_state = state.setTransition(self.getCurrentState(), state_list)
                    self._printCurrentState(current_state, state_list)
                    self.setCurrentState(current_state)
                    break

                if (sensor <= 0) or (sensor > len(state_list)):
                    print("\nEsse estado não existe!\n")
                    break
