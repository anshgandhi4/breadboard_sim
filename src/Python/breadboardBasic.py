from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class Hole(Label):
    def __init__(self, master, coord):
        """ Hole(master, coord): creates a new Hole object with given coordinates
        Hole object comes with click listener enabled
        :param master: (Class), Breadboard class (in this case)
        :param coord: (Tuple), coordinates given by Breadboard class """

        Label.__init__(self, master, height = 1, width = 2, text = "", bg = "white", relief = "sunken", font = ("Arial", 13))
        self.coord = coord
        self.bind("<Button>", self.click)
        self.group = None

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

    def set_group(self, group):
        self.group = group

    def get_group(self):
        return self.group

    def click(self, event):
        """ Hole.click(): updates Breadboard.display text with current coordinates
        highlights all Holes accordingly """

        self.master.display["text"] = self.coord
        for element in self.master.elements:
            if self.master.elements[element]["bg"] != "white":
                self.master.elements[element]["bg"] = "white"
        for element in self.group.holes:
            element["bg"] = "lightgrey"
        self["bg"] = "grey"

class Group:
    def __init__(self):
        """ Group(): creates a new Group object
        Group object has a list of holes """
        self.holes = []

    def add(self, hole):
        self.holes.append(hole)

class Breadboard(Frame):
    def __init__(self, master):
        """ Breadboard(master): creates a new Breadboard object
        Breadboard object has a display at the bottom as well as many holes and labels
        :param master: (Tk) """

        Frame.__init__(self, master, bg = "white")
        self.grid()
        self.length = 52
        self.height = 18
        self.display = Label(self, bg = "white", font = ("Arial", 48))
        self.display.grid(row = self.height, column = 0, columnspan = self.length)
        self.elements = {}
        self.groups = {}
        self.reset()

    def reset(self):
        # Add Elements, Turn Certain Elements to Labels
        for row in range(0, self.height):
            for column in range(0, self.length):
                coord = (row, column)
                self.elements[coord] = Hole(self,coord)
                self.elements[coord].grid(row = row, column = column)
                if row in [0, 3, 9, 15]:
                    self.elements[coord].label("")
                if row in [3, 15] and column % 5 == 0:
                    self.elements[coord].label(str(column))
            labelList = ["", "+","-","","a","b","c","d","e","","f","g","h","i","j","","-","+"]
            self.elements[(row, 0)].label(labelList[row])
            self.elements[(row, self.length - 1)].label(labelList[row])

        # Add Groups, Bus Groups and Terminal Groups are Added Separately
        for buses in [1, 2, 16, 17]:
            self.groups[buses] = Group()
            for column in range(1, self.length - 1):
                self.groups[buses].add(self.elements[(buses, column)])
                self.elements[(buses, column)].set_group(self.groups[buses])
        for terminals in range(1, self.length):
            self.groups[terminals * 6] = Group()
            self.groups[terminals * 6 - 3] = Group()
            for row in range(4, 9):
                self.groups[terminals * 6].add(self.elements[(row, terminals)])
                self.elements[(row, terminals)].set_group(self.groups[terminals * 6])
            for row in range(10, 15):
                self.groups[terminals * 6 - 3].add(self.elements[(row, terminals)])
                self.elements[(row, terminals)].set_group(self.groups[terminals * 6 - 3])

class MenuBar:
    def __init__(self, master, menubar):
        """ Menubar(master, menubar): creates a new MenuBar object
        MenuBar object configures menubar and has menubar functions
        :param master: (Tk)
        :param menubar: (Menu) """

        self.master = master
        self.menubar = menubar

        filemenu = Menu(self.menubar, tearoff = 0)
        filemenu.add_command(label = "New", command = self.clear_file)
        filemenu.add_command(label = "Open", command = self.open_file)
        filemenu.add_command(label = "Save", command = self.save_file)
        self.menubar.add_cascade(label = "File", menu = filemenu)

        helpmenu = Menu(self.menubar, tearoff = 0)
        helpmenu.add_command(label = "About", command = self.about)
        self.menubar.add_cascade(label = "Help", menu = helpmenu)

    def clear_file(self):
        print("breadboard")

    def open_file(self):
        filename = filedialog.askopenfilename(defaultextension = ".txt")
        if filename:
            breadboardFile = open(filename, "r")
            rowList = breadboardFile.readlines()
            breadboardFile.close()

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension = ".txt")
        if filename:
            breadboardFile = open(filename, "w")
            breadboardFile.write("breadboard")
            breadboardFile.close()

    def about(self):
        messagebox.showinfo("Breadboard Simulator", "This simulator was made by Ansh Gandhi and Jonathan Ma.", parent = self.master)

    def get_menubar(self):
        return self.menubar

# Run Simulator
root = Tk()
root.title("Breadboard Simulator")
menu = Menu(root)
menubar = MenuBar(root, menu)
sim = Breadboard(root)
root.config(menu = menu)
sim.mainloop()