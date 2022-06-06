from StateMachine import StateMachine

from Idle import Idle
from Up import Up
from Down import Down
from Left import Left
from Right import Right
from Clear import Clear

from enum import IntEnum

class State(IntEnum):
    IDLE = 1,
    UP = 2
    DOWN = 3,
    LEFT = 4,
    RIGHT = 5,
    CLEAR = 6

machine = StateMachine()

idle = Idle(State.IDLE.value)
up = Up(State.UP.value)
down = Down(State.DOWN.value)
left = Left(State.LEFT.value)
right = Right(State.RIGHT.value)
clear = Clear(State.CLEAR.value)

machine.setUniqueState(idle)
machine.setUniqueState(up)
machine.setUniqueState(down)
machine.setUniqueState(left)
machine.setUniqueState(right)
machine.setUniqueState(clear)

machine.runApplication()