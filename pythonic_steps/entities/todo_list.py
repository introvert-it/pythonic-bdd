from pythonic_steps.entities.base_entity import BasicEntity
from pythonic_steps.framework.reporter import chain_message
from todo_list import ToDoList


class ToDoListApi(BasicEntity):

    def __init__(self, current_instance, scenario_instance):
        super().__init__(current_instance, scenario_instance)
        self.todo_app = ToDoList()

    @chain_message("add item {item}")
    def add(self, item):
        return self.todo_app.add(item)

    @chain_message("add {number} items")
    def add_multiple_todo_items(self, number):
        item_name = "Relax"
        for _ in range(number):
            self.todo_app.add(f"{item_name} {_}")

    @chain_message("gets all items list")
    def list(self):
        return self.todo_app.list()
