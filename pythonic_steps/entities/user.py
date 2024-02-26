from pythonic_steps.entities.base_entity import BasicEntity
from pythonic_steps.framework.reporter import chain_message


class User(BasicEntity):
    def __init__(self, current_instance, scenario_inst):
        super().__init__(current_instance, scenario_inst)
        self.username = None

    @chain_message("named {username}")
    def named(self, username):
        self.username = username
        return self
