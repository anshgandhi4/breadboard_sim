from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Python.breadboard import Breadboard

class MenuBar:
    def __init__(self, master, menubar, sim):
        """ Menubar(master, menubar): creates a new MenuBar object
        MenuBar object configures menubar and has menubar functions
        :param master: (Tk)
        :param menubar: (Menu)
        :param sim: (Simulator) """

        self.master = master
        self.menubar = menubar
        self.sim = sim

        filemenu = Menu(self.menubar, tearoff = 0)
        filemenu.add_command(label = "New", command = self.clear_file)
        filemenu.add_command(label = "Open", command = self.open_file)
        filemenu.add_command(label = "Save", command = self.save_file)
        self.menubar.add_cascade(label = "File", menu = filemenu)

        helpmenu = Menu(self.menubar, tearoff = 0)
        helpmenu.add_command(label = "About", command = self.about)
        #helpmenu.add_command(label = "Introduction", command = self.intropane())
        self.menubar.add_cascade(label = "Help", menu = helpmenu)

    def clear_file(self):
        messagebox.showinfo("New File", "This process may take some time. Please wait...", parent = self.master)
        Breadboard.reset(self.sim.breadboard)
        messagebox.showinfo("New File", "New File Created", parent = self.master)

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

    def intropane(self):
        self.sim.launchIntro()

    def about(self):
        messagebox.showinfo("Breadboard Simulator", "This simulator was made by Ansh Gandhi and Jonathan Ma.", parent = self.master)