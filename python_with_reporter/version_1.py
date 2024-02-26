from todo_list import ToDoList


class BaseGherkin:

    def __init__(self):
        self._step_msg = None

    def __enter__(self):
        return self

    def do(self, what, *args, **kwargs):
        try:
            if callable(what):
                return what(*args, **kwargs)
            return what
        except Exception as e:
            raise Exception(self._step_msg)

    def verify(self, expression):
        assert expression, self._step_msg

    def _output_step_message(self, msg):
        self._step_msg = msg
        print(self._step_msg)
        return self

    def given(self, message):
        return self._output_step_message(f"Given {message}")

    def when(self, message):
        return self._output_step_message(f"When {message}")

    def then(self, message):
        return self._output_step_message(f"Given {message}")

    def also(self, message):
        return self._output_step_message(f"And {message}")


bdd = BaseGherkin()
given = bdd.given
when = bdd.when
then = bdd.then
also = bdd.also


def test_add_todo_item():
    thing = given("User has a TODO list").do(ToDoList())
    when("User create a new todo item 'visit theatre'").do(thing.add, 'visit theatre')
    new_todo_items_list = also("User gets updated list of TODO items").do(thing.list)
    then("List should contain one more todo item").verify(len(new_todo_items_list) > 0)
