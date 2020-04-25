from tkinter import *

class Hole(Canvas):
    def __init__(self, master, coord):
        """ Hole(master, coord): creates a new Hole object with given coordinates
        Hole object comes with click listener enabled
        :param master: (Simulator)
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
        if label[:-1] == "+":
            self.itemconfig(self.text, fill = "red")
        elif label[:-1] == "-":
            self.itemconfig(self.text, fill = "blue")

    def click(self, event):
        """ Hole.click(): updates Breadboard.display text with current coordinates
        highlights all Holes accordingly """

        if self["bg"] == "ivory4":
            for element in self.master.elements:
                if self.master.elements[element]["bg"] != self.master.elements[element].color:
                    self.master.elements[element]["bg"] = self.master.elements[element].color
        elif self.coord in self.master.supplies.keys():
            self.master.powersupply_edit(self.coord)
        elif self.coord in self.master.wirestarts.keys() or self.coord in self.master.wireends.keys():
            self.master.wire_edit(self.coord)
        elif self.coord in self.master.resistorstarts.keys() or self.coord in self.master.resistorends.keys():
            self.master.resistor_edit(self.coord)
        elif self.coord in self.master.ledstarts.keys() or self.coord in self.master.ledends.keys():
            self.master.led_edit(self.coord)
        elif self.coord in self.master.switchstarts.keys() or self.coord in self.master.switchends.keys():
            self.master.switch_edit(self.coord)
        else:
            for element in self.master.elements:
                if self.master.elements[element]["bg"] != self.master.elements[element].color:
                    self.master.elements[element]["bg"] = self.master.elements[element].color
            for element in self.group.holes:
                element["bg"] = "ivory3"
            self["bg"] = "ivory4"