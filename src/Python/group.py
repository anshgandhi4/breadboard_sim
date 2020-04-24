class Group:
    def __init__(self):
        """ Group(): creates a new Group object
        Group object has a list of holes """
        self.holes = []

    def add(self, hole):
        self.holes.append(hole)