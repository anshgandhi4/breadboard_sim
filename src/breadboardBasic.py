from tkinter import *

class Hole(Label):
    def __init__(self, master, coord):
        Label.__init__(self, master, height = 1, width = 2, text = "", bg = "white", relief = "sunken", font = ("Arial", 12))
        self.coord = coord
        self.bind("<Button>", self.click)
        self.group = None

    def label(self, label):
        self["relief"] = "flat"
        self.unbind("<Button>")
        self["text"] = label

    def set_group(self, group):
        self.group = group

    def get_group(self):
        return self.group

    def click(self, event):
        self.master.name["text"] = self.coord
        for element in self.master.elements:
            self.master.elements[element]["bg"] = "white"
        for element in self.group.holes:
            element["bg"] = "lightgrey"
        self["bg"] = "grey"

class Group:
    def __init__(self):
        self.holes = []

    def add(self, hole):
        self.holes.append(hole)

class Breadboard(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = "white")
        self.grid()
        self.length = 61
        self.height = 20
        self.name = Label(self, bg = "white", font = ("Arial", 48))
        self.name.grid(row = self.height, column = 0, columnspan = self.length)
        self.elements = {}
        for row in range(0, self.height):
            for column in range(0, self.length):
                coord = (row, column)
                self.elements[coord] = Hole(self,coord)
                self.elements[coord].grid(row = row, column = column)
            if row in [2, 9, 10, 17]:
                for column in range(0, self.length):
                    coord = (row, column)
                    self.elements[coord].label("")
            elif row in [3, 16]:
                for column in range(0, self.length):
                    coord = (row, column)
                    self.elements[coord].label(str(column))
            coord = (row, 0)
            self.elements[coord].label(["+","-","","","a","b","c","d","e","","","f","g","h","i","j","","","-","+"][row])
        self.groups = {}
        for buses in [0, 1, 18, 19]:
            self.groups[buses] = Group()
            for column in range(0, self.length):
                self.groups[buses].add(self.elements[(buses, column)])
                self.elements[(buses, column)].set_group(self.groups[buses])
        for terminalColumns in range(1, self.length):
            self.groups[terminalColumns * 8] = Group()
            self.groups[terminalColumns * 8 - 4] = Group()
            for row in range(4, 9):
                self.groups[terminalColumns * 8].add(self.elements[(row, terminalColumns)])
                self.elements[(row, terminalColumns)].set_group(self.groups[terminalColumns * 8])
            for row in range(11, 16):
                self.groups[terminalColumns * 8 - 4].add(self.elements[(row, terminalColumns)])
                self.elements[(row, terminalColumns)].set_group(self.groups[terminalColumns * 8 - 4])

def breadboard():
    root = Tk()
    root.title("Breadboard")
    sim = Breadboard(root)
    sim.mainloop()

breadboard()