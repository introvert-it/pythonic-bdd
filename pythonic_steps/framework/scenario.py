from pythonic_steps.framework.object_storage import ObjectStorage


class Scenario:
    def __init__(self):
        self.msg_chain = []
        self.bdd = ObjectStorage(self)
        self.scenario_name = None

    @property
    def then(self):
        return self.bdd.then

    @property
    def given(self):
        return self.bdd.given

    @property
    def when(self):
        return self.bdd.when

    @property
    def also(self):
        return self.bdd.also

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        scenario_steps_list = self.msg_chain[self.msg_chain.index("--") + 1::]
        print(" ".join(scenario_steps_list))

    def name(self, name):
        self.scenario_name = name
        self.msg_chain.append("--")
        self.msg_chain.append(f"Scenario: {name}\n\n")
        return self


