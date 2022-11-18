

class user_list(object):

    def __init__(self, sourceCollection = None):
        self.user_items = list()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.user_items)

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        result = user_list(self)
        for item in other:
            result.add(item)
        return result

    def add(self, item):
        self.user_items.append(item)

    def pop(self):
        if self.isEmpty():
            raise KeyError('List is empty')
        return self.user_items.pop(0)
