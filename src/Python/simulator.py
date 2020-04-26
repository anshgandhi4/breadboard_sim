from tkinter import *
from PIL import Image
from PIL import ImageTk
from Python.intro import Intro
from Python.menubar import MenuBar
from Python.breadboard import Breadboard
from Python.wire import Wire
from Python.wire import WireEdit
from Python.resistor import Resistor
from Python.resistor import ResistorEdit
from Python.led import LED
from Python.led import LEDEdit
from Python.powersupply import PowerSupply
from Python.powersupply import PowerSupplyEdit
from Python.switch import Switch
from Python.switch import SwitchEdit

class Simulator(Frame):
    def __init__(self, master):
        """ Simulator(master): creates a new Simulator object
        Simulator object has a display at the bottom as well as many holes and labels
        :param master: (Tk) """

        Frame.__init__(self, master, bg = "white")
        self.grid()
        self.length = 52
        self.height = 19

        self.wirestarts = {}
        self.wireends = {}
        self.wirecolors = {}
        self.wireimg = ImageTk.PhotoImage(Image.open("wire.jpg").resize((50, 50), Image.ANTIALIAS))
        self.wirepic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.wirepic.create_image(27, 27, image = self.wireimg)
        self.wirepic.image = self.wireimg
        self.wirepic.grid(row = self.height, column = 1, columnspan = 9)
        self.wirepic.bind("<Button>", self.wire_select)
        Label(self, bg = "white", font = ("Arial", 20), text = "Wire").grid(row = self.height + 1, column = 1, columnspan = 9)

        self.resistances = {}
        self.resistorstarts = {}
        self.resistorends = {}
        self.resistorimg = ImageTk.PhotoImage(Image.open("resistor.jpg").resize((50, 50), Image.ANTIALIAS))
        self.resistorpic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.resistorpic.create_image(27, 27, image = self.resistorimg)
        self.resistorpic.image = self.resistorimg
        self.resistorpic.grid(row = self.height, column = 11, columnspan = 9)
        self.resistorpic.bind("<Button>", self.resistor_select)
        Label(self, bg = "white", font = ("Arial", 20), text = "Resistor").grid(row = self.height + 1, column = 11, columnspan = 9)

        self.ledstarts = {}
        self.ledends = {}
        self.ledcolors = {}
        self.ledimg = ImageTk.PhotoImage(Image.open("led.jpg").resize((50, 50), Image.ANTIALIAS))
        self.ledpic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.ledpic.create_image(27, 27, image = self.ledimg)
        self.ledpic.image = self.ledimg
        self.ledpic.grid(row = self.height, column = 21, columnspan = 9)
        self.ledpic.bind("<Button>", self.led_select)
        Label(self, bg = "white", font = ("Arial", 20), text = "LED").grid(row = self.height + 1, column = 21, columnspan = 9)

        self.supplies = {}
        self.voltages = {}
        self.powersupplyimg = ImageTk.PhotoImage(Image.open("powersupply.jpg").resize((50, 50), Image.ANTIALIAS))
        self.powersupplypic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.powersupplypic.create_image(27, 27, image = self.powersupplyimg)
        self.powersupplypic.image = self.powersupplyimg
        self.powersupplypic.grid(row = self.height, column = 31, columnspan = 9)
        self.powersupplypic.bind("<Button>", self.powersupply_select)
        Label(self, bg = "white", font = ("Arial", 20), text = "Power Supply").grid(row = self.height + 1, column = 31, columnspan = 9)

        self.switched = {}
        self.switchstarts = {}
        self.switchends ={}
        self.switchimg = ImageTk.PhotoImage(Image.open("switch.jpg").resize((50, 50), Image.ANTIALIAS))
        self.switchpic = Canvas(self, width = 50, height = 50, highlightthickness = 4)
        self.switchpic.create_image(27, 27, image = self.switchimg)
        self.switchpic.image = self.switchimg
        self.switchpic.grid(row = self.height, column = 41, columnspan = 9)
        self.switchpic.bind("<Button>", self.switch_select)
        Label(self, bg = "white", font = ("Arial", 20), text = "Switch").grid(row = self.height + 1, column = 41, columnspan = 9)

        self.elements = {}
        self.groups = {}
        self.breadboard = Breadboard(self, self.length, self.height)
        self.breadboard.reset()

    def reset_highlight(self):
        self.wirepic["highlightbackground"] = "white"
        self.resistorpic["highlightbackground"] = "white"
        self.ledpic["highlightbackground"] = "white"
        self.powersupplypic["highlightbackground"] = "white"
        self.switchpic["highlightbackground"] = "white"

    def reset(self):
        self.elements = self.breadboard.elements
        self.groups = self.breadboard.groups
        self.grid_breadboard()
        self.reset_highlight()

    def grid_breadboard(self):
        for row in range(0, self.height):
            for column in range(0, self.length):
                coord = (row, column)
                self.elements[coord].grid(row = row, column = column)

    def save(self):
        savelist = []

        wires = {**self.wirestarts, **self.wireends}
        savelist.append(wires)
        savelist.append(self.wirecolors)

        resistors = {**self.resistorstarts, **self.resistorends}
        savelist.append(resistors)
        savelist.append(self.resistances)

        leds = {**self.ledstarts, **self.ledends}
        savelist.append(leds)
        savelist.append(self.ledcolors)

        savelist.append(self.supplies)
        savelist.append(self.voltages)

        switches = {**self.switchstarts, **self.switchends}
        savelist.append(switches)
        savelist.append(self.switched)

        return savelist

    def create_wire(self, start, end, color):
        Wire.create_wire(color, start, end, self)

    def create_resistor(self, start, end, resistance):
        Resistor.create_resistor(resistance, start, end, self)

    def create_led(self, start, end, color):
        LED.create_led(color, start, end, self)

    def create_powersupply(self, coord, voltage):
        PowerSupply.create_powersupply(voltage, coord, self)

    def create_switch(self, start, end, on):
        Switch.create_switch(on, start, end, self)

    def wire_select(self, event):
        self.reset_highlight()
        self.wirepic["highlightbackground"] = "gold"

        root = Tk()
        root.title("New Wire")
        wire = Wire(root, self)
        wire.mainloop()

    def wire_edit(self, coord):
        root = Tk()
        root.title("Edit Wire")
        wire = WireEdit(root, self.elements[coord], self)
        wire.mainloop()

    def resistor_select(self, event):
        self.reset_highlight()
        self.resistorpic["highlightbackground"] = "gold"

        root = Tk()
        root.title("New Resistor")
        resistor = Resistor(root, self)
        resistor.mainloop()

    def resistor_edit(self, coord):
        root = Tk()
        root.title("Edit Resistor")
        resistor = ResistorEdit(root, self.elements[coord], self)
        resistor.mainloop()

    def led_select(self, event):
        self.reset_highlight()
        self.ledpic["highlightbackground"] = "gold"

        root = Tk()
        root.title("New LED")
        led = LED(root, self)
        led.mainloop()

    def led_edit(self, coord):
        root = Tk()
        root.title("Edit LED")
        led = LEDEdit(root, self.elements[coord], self)
        led.mainloop()

    def powersupply_select(self, event):
        self.reset_highlight()
        self.powersupplypic["highlightbackground"] = "gold"

        root = Tk()
        root.title("New Power Supply")
        powersupply = PowerSupply(root, self)
        powersupply.mainloop()

    def powersupply_edit(self, coord):
        root = Tk()
        root.title("Edit Power Supply")
        powersupply = PowerSupplyEdit(root, self.elements[coord], self)
        powersupply.mainloop()

    def switch_select(self, event):
        self.reset_highlight()
        self.switchpic["highlightbackground"] = "gold"

        root = Tk()
        root.title("New Switch")
        switch = Switch(root, self)
        switch.mainloop()

    def switch_edit(self, coord):
        root = Tk()
        root.title("Edit Switch")
        switch = SwitchEdit(root, self.elements[coord], self)
        switch.mainloop()

    def launchIntro(self):
        root = Toplevel()
        root.title("Introduction")
        root.geometry("1000x700")
        intro = Intro(root)
        intro.mainloop()

# Run Simulator
root = Tk()
root.title("Breadboard Simulator")
sim = Simulator(root)
menu = Menu(root)
menubar = MenuBar(root, menu, sim)
root.config(menu = menu)
root.after(5000, sim.launchIntro())
sim.mainloop()