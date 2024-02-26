from pythonic_steps.framework.reporter import chain_message


class BasicEntity:
    def __init__(self, current_instance, scenario_inst):
        self._actual_value = None
        self._current_instance = current_instance
        self._scenario = scenario_inst

    @chain_message("has")
    def has(self, what):
        return getattr(self._current_instance, what)

    @property
    @chain_message("makes:")
    def does(self):
        return self._current_instance

    @chain_message("expects {actual_value}")
    def expects(self, actual_value):
        self._actual_value = actual_value
        return self

    @property
    @chain_message("to")
    def to(self):
        return self

    @property
    @chain_message("be")
    def be(self):
        return self

    @chain_message("equal to {expected_value}")
    def equal_to(self, expected_value):
        assert self._actual_value == expected_value

