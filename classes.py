class Transportation:
    def __init__(self):
        print("Initializing new transportation")

    def start(self):
        print("Starting transportation")

    def move(self):
        print("Moving transportation")

    def stop(self):
        print("Stopping transportation")


class Storage:
    items = []
    def __init__(self):
        print("Initializing new storage")

    def store_item(self, item):
        print("Storing", item)
        self.items.append(item)

    def get_item(self, item):
        self.items.pop(self.items.index(item))

class Car(Transportation, Storage):
    def __init__(self):
        print("Initializing new Car")
    pass

test = Car()
test.store_item("test")
test.get_item("test")
