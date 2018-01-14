import logging

logger = logging.getLogger(__name__)

class State:
    next_state = None
    states = {}

    def entry(self):
        logger.debug("Entry into %s...", self.__class__.__name__)
    def main(self):
        logger.debug("Main method for  %s...", self.__class__.__name__)
    def exit(self):
        logger.debug("Exit method for  %s...", self.__class__.__name__)

    def __init_subclass__(cls, **kwargs):
        "add this state the dictionary of possible states"
        super().__init_subclass__(**kwargs)
        #logger.debug("In __init_subclass__ for: %s", cls.__name__)
        print("In __init_subclass__ for: %s" %cls.__name__)
        cls.states[cls.__name__] = cls

class StateMachine:
    states = {}

    def __init__(self):
        for s,cls in State.states.items():
            self.states[s] = cls()

    def run(self, state_name):
        state = self.states[state_name]
        state.entry()
        state.main()
        state.exit()
        return state.next_state


