from tkinter import *

class Hole(Label):
    def __init__(self, master, coord):
        Label.__init__(self, master, height = 1, width = 2, text = "", bg = "white", relief = "sunken", font = ("Arial", 12))
        self.coord = coord
        self.bind("<Button>", self.click)

    def label(self, label):
        self["relief"] = "flat"
        self.unbind("<Button>")
        self["text"] = label

    def click(self, event):
        self.master.name["text"] = self.coord

class Breadboard(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = "white")
        self.grid()
        self.name = Label(self, bg = "white", font = ("Arial", 48))
        self.name.grid(row = 20, column = 0, columnspan = 21)
        self.elements = {}
        for row in range(0, 20):
            for column in range(0, 21):
                coord = (row, column)
                self.elements[coord] = Hole(self,coord)
                self.elements[coord].grid(row = row, column = column)
            if row in [2, 9, 10, 17]:
                for column in range(0, 21):
                    coord = (row, column)
                    self.elements[coord].label("")
            elif row in [3, 16]:
                for column in range(0, 21):
                    coord = (row, column)
                    self.elements[coord].label(str(20 - column))
            coord = (row, 20)
            self.elements[coord].label(["+","-","","","a","b","c","d","e","","","f","g","h","i","j","","","-","+"][row])

def breadboard():
    root = Tk()
    root.title("Breadboard")
    sim = Breadboard(root)
    sim.mainloop()

breadboard()