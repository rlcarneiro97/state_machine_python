from enum import IntEnum

class State(IntEnum):
    FICAR = 1,
    SENTAR = 2
    PATA = 3,
    FINGIR_MORTE = 4

# ----------------------- ESTADOS ----------------------

def state_ficar():
    print("\n FICAR\n")

def state_sentar():
    print("\n SENTAR\n")

def state_pata():
    print("\n PATA\n")

def state_fingir_morte():
    print("\n FINGIR_MORTE\n")

# ---------------- FUNCOES DE TRANSICAO ----------------

def set_state_ficar(current_state):

    if current_state == State.FINGIR_MORTE.value:
        current_state = State.FICAR.value
        state_ficar()
        return current_state
    else:
        get_current_state(current_state)
        return current_state

def set_state_sentar(current_state):
    
    if current_state == State.FICAR.value:
        current_state = State.SENTAR.value
        state_sentar()
        return current_state
    else:
        get_current_state(current_state)
        return current_state

def set_state_pata(current_state):

    if current_state == State.SENTAR.value:
        current_state = State.PATA.value
        state_pata()
        return current_state
    else:
        get_current_state(current_state)
        return current_state

def set_state_fingir_morte(current_state):

    if current_state == State.PATA.value:
        current_state = State.FINGIR_MORTE.value
        state_fingir_morte()
        return current_state
    else:
        get_current_state(current_state)
        return current_state

# ------------------- HELPERS --------------------------

def get_current_state(current_state):

    for state in State:
        if state.value == current_state:
            print("\n", state.name, "\n")

# ------------------------------------------------------

def state_machine(current_state):

    sensor = current_state

    while sensor != 0:

        sensor = int(input("Digite um estímulo: "))

        match sensor:
            case 1:
                current_state = set_state_ficar(current_state)
            case 2:
                current_state = set_state_sentar(current_state)
            case 3:
                current_state = set_state_pata(current_state)
            case 4:
                current_state = set_state_fingir_morte(current_state)
            case default:
                print("\nEstado nao encontrado!\n")

    return current_state

if __name__ == '__main__':

    current_state = 1
    current_state = state_machine(current_state)