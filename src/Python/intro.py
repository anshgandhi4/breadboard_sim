from tkinter import *
from PIL import Image, ImageTk

class Intro(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")

        self.columnconfigure(0, minsize = 65)
        self.columnconfigure(1, minsize = 65)
        self.grid()

        Label(self, bg = "white", font = ("Arial", 18), text = "Welcome to Breadboard Simulator").grid(row = 1, column = 0)
        load = Image.open("breadboard.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.grid(row = 2, column = 0, columnspan = 1)

        Label(self, bg = "white", font = ("Arial", 9), text = "This application allows you to simulate a breadboard on your computer."
                                                               " A breadboard is a board that can be used to prototype and experiment with electric circuits.\n"
                                                               "As you can see above, a breadboard contains many holes. "
                                                               "In each hole, you can connect electronic components like wires, resisters, leds, and switches in order to\n"
                                                               "make a complete circuit. The image below shows the connections beneath the breadboard's surface. You can see individual red, blue, and green lines. By connecting these lines \n"
                                                               "together with wires, leds, etc, you can create a complete circuit. "
                                                               "Because of this, breadboards are very versatile, and you can use it to try to experiment with many cool things!").grid(row = 3, column = 0)

        load = Image.open("breadboardconnections.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.grid(row = 4, column = 0, columnspan = 1)

        Label(self, bg = "white", font = ("Arial", 9), text =
        "Below you can see what the breadboard will look like when the simulator first opens.\n"
        "To start, simply click on one of the five components below- a wire, resistor, led, switch, or power supply (required for a circuit).\n"
        "Then enter the column (numbers on top and bottom) and row (letters on left and right) and the other applicable properties (like voltage or color)\n"
        "Once you have placed all your components, press run and see your creation come to life.").grid(row = 5, column = 0)

        load = Image.open("simimg.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.grid(row = 6, column = 0, columnspan = 1)