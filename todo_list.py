
class ToDoList:
    def __init__(self):
        self._todo_items = []
        self._id = 0

    def add(self, item):
        self._id += 1
        self._todo_items.append({'id': self._id, 'text': item})
        return self._id

    def remove(self, item_id):
        for item in self._todo_items:
            if item['id'] == int(item_id):
                self._todo_items.remove(item)
                return

    def list(self):
        return self._todo_items
