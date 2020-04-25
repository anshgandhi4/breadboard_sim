from tkinter import *

class Hole(Label):
    def __init__(self, master, coord):
        """ Hole(master, coord): creates a new Hole object with given coordinates
        Hole object comes with click listener enabled
        :param master: (Class), Breadboard class (in this case)
        :param coord: (Tuple), coordinates given by Breadboard class """

        Label.__init__(self, master, height = 1, width = 2, text = "", bg = "khaki1", relief = "sunken", font = ("Arial", 12))
        self.coord = coord
        self.bind("<Button>", self.click)
        self.group = None
        self.color = "khaki1"

        self.root = None
        self.powersupply = None

    def label(self, label):
        """ Hole.label(label): disables the hole and turns it into a basic label
        changes the text to red if it is "+" and blue if it is "-"
        :param label: (String), text to put on Hole """

        self["relief"] = "flat"
        self.unbind("<Button>")
        self["text"] = label
        if label == "+":
            self["fg"] = "red"
        elif label == "-":
            self["fg"] = "blue"

    def click(self, event):
        """ Hole.click(): updates Breadboard.display text with current coordinates
        highlights all Holes accordingly """

        if self["bg"] == "grey":
            for element in self.master.elements:
                if self.master.elements[element]["bg"] != self.master.elements[element].color:
                    self.master.elements[element]["bg"] = self.master.elements[element].color
        elif self["bg"] == "black":
            self.master.powersupply_edit(self.coord)
        else:
            self.master.display["text"] = self.coord
            for element in self.master.elements:
                if self.master.elements[element]["bg"] != self.master.elements[element].color:
                    self.master.elements[element]["bg"] = self.master.elements[element].color
            for element in self.group.holes:
                element["bg"] = "lightgrey"
            self["bg"] = "grey"