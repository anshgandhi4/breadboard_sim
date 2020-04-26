from tkinter import *
from PIL import Image
from PIL import ImageTk

class Intro(Frame):

    def __init__(self, root):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        Label(self.frame, bg = "white", font = ("Arial", 20), text = "Welcome to Breadboard Simulator").grid(row = 0, column = 0)
        load = Image.open("breadboard.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.frame, image = render)
        img.image = render
        img.grid(row = 1, column = 0)

        Label(self.frame, bg = "white", font = ("Arial", 14), text = "This application allows you to simulate a breadboard on your computer.\n"
        "A breadboard is a board that can be used to prototype and experiment with electric circuits.\n"
        "As you can see above, a breadboard contains many holes.\n"
        "In each hole, you can connect electronic components like wires, resisters, leds, and switches in order to make a complete circuit.\n"
        "The image below shows the connections beneath the breadboard's surface. You can see individual red, blue, and green lines.\n"
        "By connecting these lines together with wires, leds, etc, you can create a complete circuit.\n"
        "Because of this, breadboards are very versatile, and you can use it to try to experiment with many cool things!").grid(row = 2, column = 0)

        load = Image.open("breadboardconnections.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.frame, image = render)
        img.image = render
        img.grid(row = 3, column = 0)

        Label(self.frame, bg = "white", font = ("Arial", 14), text = "Below you can see what the breadboard will look like when the simulator first opens.").grid(row = 4, column = 0)

        load = Image.open("main.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.frame, image = render)
        img.image = render
        img.grid(row = 5, column = 0)

        Label(self.frame, bg = "white", font = ("Arial", 14), text = "To start, simply click on one of the five components below- a wire, resistor, led, switch, or power supply (required for a circuit).").grid(row = 6, column = 0)

        load = Image.open("add.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.frame, image = render)
        img.image = render
        img.grid(row = 7, column = 0)

        Label(self.frame, bg = "white", font = ("Arial", 14), text = "Then enter the column (numbers on top and bottom) and row (letters on left and right), \nand the other applicable properties (like voltage or color).").grid(row = 8, column = 0)

        load = Image.open("edit.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.frame, image = render)
        img.image = render
        img.grid(row = 9, column = 0)

        Label(self.frame, bg = "white", font = ("Arial", 14), text = "If you want to edit one of the components on the breadboard, simply click on one end of the component,\n and a small window will pop up where you can change some of the settings.").grid(row = 10, column = 0)

        load = Image.open("save.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.frame, image = render)
        img.image = render
        img.grid(row = 11, column = 0)

        Label(self.frame, bg = "white", font = ("Arial", 14), text = "Once you have placed all your components, press run and see your creation come to life.").grid(row = 12, column = 0)

        load = Image.open("save.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.frame, image = render)
        img.image = render
        #img.grid(row = 13, column = 0)

        Label(self.frame, bg = "white", font = ("Arial", 14), text = "When you are done, make sure to save your breadboard using the handy save function.\n"
                                                                     "The next time you open up the simulator, you can quickly open the save file to continue where you left off!\nHappy experimenting!").grid(row = 14, column = 0)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
