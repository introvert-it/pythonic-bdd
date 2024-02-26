from pythonic_steps.entities.todo_list import ToDoListApi
from pythonic_steps.entities.user import User

from pythonic_steps.framework.reporter import chain_message


class BDD:
    def __init__(self, scenario_inst):
        self._scenario = scenario_inst

    @property
    @chain_message("\nGiven")
    def given(self):
        return self

    @property
    @chain_message("\nWhen")
    def when(self):
        return self

    @property
    @chain_message("\nThen")
    def then(self):
        return self

    @property
    @chain_message("\nAnd")
    def also(self):
        return self


class ObjectStorage(BDD):
    def __init__(self, scenario_inst):
        super().__init__(scenario_inst)
        self._user = None
        self._todo_list = None

    @property
    @chain_message("todo list app")
    def todo_list(self):
        if not self._todo_list:
            self._todo_list = ToDoListApi(self, self._scenario)
        return self._todo_list

    @property
    @chain_message("user")
    def user(self):
        if not self._user:
            self._user = User(self, self._scenario)
        return self._user
