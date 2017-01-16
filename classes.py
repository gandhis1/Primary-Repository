class Transportation:
    def start(self):
        print("Starting transportation")

    def move(self):
        print("Moving transportation")

    def stop(self):
        print("Stopping transportation")


class Storage:
    def __init__(self):
        self.items = []

    def store_item(self, item):
        print("Storing ", item)
        self.items.append(item)

    def get_item(self, item):
        self.items.pop(item)

class Car(Transportation, Storage):
    pass

test = Car()