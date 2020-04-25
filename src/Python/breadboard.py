from Python.hole import Hole
from Python.group import Group

class Breadboard:
    def __init__(self, master, length, height):
        """ Breadboard(master, length, height): creates a new Breadboard object
        Breadboard object contains many holes and groups
        :param master: (Integer), Simulator class (in this case)
        :param length: (Integer), length of Breadboard
        :param height: (Integer), height of Breadboard """

        self.master = master
        self.length = length
        self.height = height
        self.elements = {}
        self.groups = {}

    def reset(self):
        # Add Elements, Turn Certain Elements to Labels
        for row in range(0, self.height):
            for column in range(0, self.length):
                coord = (row, column)
                self.elements[coord] = Hole(self.master, coord)
                if row in [0, 3, 9, 15, 18]:
                    self.elements[coord].label("")
                if row in [3, 15] and column % 5 == 0:
                    self.elements[coord].label(str(column))
            labelList = ("", "+t", "-t", "", "a", "b", "c", "d", "e", "", "f", "g", "h", "i", "j", "", "-b", "+b", "")
            self.elements[(row, 0)].label(labelList[row])
            self.elements[(row, self.length - 1)].label(labelList[row])

        # Add Groups, Bus Groups and Terminal Groups are Added Separately
        for buses in [1, 2, 16, 17]:
            self.groups[buses] = Group()
            for column in range(1, self.length - 1):
                self.groups[buses].add(self.elements[(buses, column)])
                self.elements[(buses, column)].group = self.groups[buses]
        for terminals in range(1, self.length):
            self.groups[terminals * 6] = Group()
            self.groups[terminals * 6 - 3] = Group()
            for row in range(4, 9):
                self.groups[terminals * 6].add(self.elements[(row, terminals)])
                self.elements[(row, terminals)].group = self.groups[terminals * 6]
            for row in range(10, 15):
                self.groups[terminals * 6 - 3].add(self.elements[(row, terminals)])
                self.elements[(row, terminals)].group = self.groups[terminals * 6 - 3]

        # Reset Simulator
        self.master.reset()