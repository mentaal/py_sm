from py_sm import State, StateMachine

class StateOne(State):

    def exit(self):
        super().exit()
        self.next_state = 'StateTwo'

class StateTwo(State):

    def exit(self):
        self.next_state = 'StateOne'

def test_state_execution():

    state_machine = StateMachine()
    next_state = state_machine.run('StateOne')
    for i in range(5):
        next_state = state_machine.run(next_state)

