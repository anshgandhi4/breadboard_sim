from tkinter import *

class Hole(Canvas):
    def __init__(self, master, coord):
        """ Hole(master, coord): creates a new Hole object with given coordinates
        Hole object comes with click listener enabled
        :param master: (Class), Breadboard class (in this case)
        :param coord: (Tuple), coordinates given by Breadboard class """

        Canvas.__init__(self, master, height = 20, width = 20, bg = "khaki1", highlightthickness = 0, relief = "sunken", bd = 2)
        self.coord = coord
        self.bind("<Button>", self.click)
        self.group = None
        self.color = "khaki1"
        self.text = self.create_text(11, 11, text = "", font = ("Arial", 12))

        self.root = None
        self.powersupply = None

    def label(self, label):
        """ Hole.label(label): disables the hole and turns it into a basic label
        changes the text to red if it is "+" and blue if it is "-"
        :param label: (String), text to put on Hole """

        self["relief"] = "flat"
        self.unbind("<Button>")
        self.itemconfig(self.text, text = label)
        if label == "+":
            self.itemconfig(self.text, fill = "red")
        elif label == "-":
            self.itemconfig(self.text, fill = "blue")

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