from pythonic_steps.framework.scenario import Scenario


def test_add_one_todo_item():
    with Scenario().name("Test add one todo item") as _:
        _.given.user.named("admin").has("todo_list")
        _.when.user.does.todo_list.add("Hello BDD")
        result = _.also.todo_list.list()
        _.then.user.expects(len(result)).to.be.equal_to(1)


def test_add_multiple_todo_items():
    with Scenario().name("Test add multiple todo items") as s:
        s.given.user.named("admin").has("todo_list")
        s.when.user.does.todo_list.add_multiple_todo_items(10)
        result = s.also.todo_list.list()
        s.then.user.expects(len(result)).to.be.equal_to(10)


def test_prev_version_2():
    with Scenario().name("Test add multiple todo items") as s:
        s.given.user.named("admin").has("todo_list")
        for _ in range(15):
            s.when.user.does.todo_list.add("Hello BDD")
        result = s.also.todo_list.list()
        s.then.user.expects(len(result)).to.be.equal_to(15)
