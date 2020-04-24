from tkinter import *
from PIL import Image
from PIL import ImageTk
from Python.menubar import MenuBar
from Python.breadboard import Breadboard

class Simulator(Frame):
    def __init__(self, master):
        """ Simulator(master): creates a new Simulator object
        Simulator object has a display at the bottom as well as many holes and labels
        :param master: (Tk) """

        Frame.__init__(self, master, bg = "white")
        self.grid()
        self.length = 52
        self.height = 19

        self.display = Label(self, bg = "white", font = ("Arial", 48))
        self.display.grid(row = self.height + 1, column = 0, columnspan = self.length)

        self.wires = []
        self.wireimg = ImageTk.PhotoImage(Image.open("icon.png").resize((50, 50), Image.ANTIALIAS))
        self.wirepic = Label(self, image = self.wireimg)
        self.wirepic.image = self.wireimg
        self.wirepic.grid(row = self.height, column = 1, columnspan = 9)
        self.wirepic.bind("<Button>", self.wire_select)

        self.resistors = []
        self.resistorimg = ImageTk.PhotoImage(Image.open("icon.png").resize((50, 50), Image.ANTIALIAS))
        self.resistorpic = Label(self, image = self.resistorimg)
        self.resistorpic.image = self.resistorimg
        self.resistorpic.grid(row = self.height, column = 11, columnspan = 9)
        self.resistorpic.bind("<Button>", self.resistor_select)

        self.leds = []
        self.ledimg = ImageTk.PhotoImage(Image.open("icon.png").resize((50, 50), Image.ANTIALIAS))
        self.ledpic = Label(self, image = self.ledimg)
        self.ledpic.image = self.ledimg
        self.ledpic.grid(row = self.height, column = 21, columnspan = 9)
        self.ledpic.bind("<Button>", self.led_select)

        self.powersupplies = []
        self.powersupplyimg = ImageTk.PhotoImage(Image.open("icon.png").resize((50, 50), Image.ANTIALIAS))
        self.powersupplypic = Label(self, image = self.powersupplyimg)
        self.powersupplypic.image = self.powersupplyimg
        self.powersupplypic.grid(row = self.height, column = 31, columnspan = 9)
        self.powersupplypic.bind("<Button>", self.powersupply_select)

        self.buttons = []
        self.buttonimg = ImageTk.PhotoImage(Image.open("icon.png").resize((50, 50), Image.ANTIALIAS))
        self.buttonpic = Label(self, image = self.buttonimg)
        self.buttonpic.image = self.buttonimg
        self.buttonpic.grid(row = self.height, column = 41, columnspan = 9)
        self.buttonpic.bind("<Button>", self.button_select)

        self.elements = {}
        self.groups = {}
        self.breadboard = Breadboard(self, self.length, self.height)
        self.breadboard.reset()

    def reset(self):
        self.elements = self.breadboard.elements
        self.groups = self.breadboard.groups
        self.grid_breadboard()
        self.display["text"] = ""

    def grid_breadboard(self):
        for row in range(0, self.height):
            for column in range(0, self.length):
                coord = (row, column)
                self.elements[coord].grid(row = row, column = column)

    def wire_select(self, event):
        print("wire")

    def resistor_select(self, event):
        print("resistor")

    def led_select(self, event):
        print("led")

    def powersupply_select(self, event):
        print("power supply")

    def button_select(self, event):
        print("button")

# Run Simulator
root = Tk()
root.title("Breadboard Simulator")
sim = Simulator(root)
menu = Menu(root)
menubar = MenuBar(root, menu, sim)
root.config(menu = menu)
sim.mainloop()