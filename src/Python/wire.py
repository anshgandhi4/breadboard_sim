from tkinter import *
import random

class Wire(Frame):
    def __init__(self, master, sim):
        # self.start = 0
        # self.end = 0
        # self.color = "white"
        Frame.__init__(self, master, bg = "white")
        self.grid()

        self.columnconfigure(0, minsize = 65)
        self.columnconfigure(1, minsize = 65)

        self.master = master
        self.sim = sim
        self.coord = None

        self.locationText = Label(self, bg = "white", font = ("Arial", 14), text = "Wire")
        self.locationText.grid(row = 0, column = 0, columnspan = 2)
        self.holeOneT = Label(self, bg ="white", font = ("Arial", 12), text ="Hole 1")
        self.holeOneT.grid(row = 1, column = 0)
        self.holeTwoT = Label(self, bg ="white", font = ("Arial", 12), text ="Hole 2")
        self.holeTwoT.grid(row = 1, column = 1)

        self.holeOneF = Entry(self)
        self.holeOneF.grid(row = 5, column = 0, columnspan = 1)
        self.holeTwoF = Entry(self)
        self.holeTwoF.grid(row = 5, column = 1, columnspan = 1)

        self.submit = Button(self, bg = "white", text = "Submit", command = self.submit)
        self.submit.grid(row = 6, column = 0, columnspan = 2)

    def submit(self):
        self.holeOne = self.holeOneF.get()
        self.holeTwo = self.holeTwoF.get()
        self.master.destroy()
        oneL = self.holeOne[0]
        oneN = int(self.holeOne[1:])
        twoL = self.holeTwo[0]
        twoN = int(self.holeTwo[1:])
        print(oneL + " " + str(oneN))
        print(twoL + " " + str(twoN))

        oneCharV = self.findIndex(oneL)
        twoCharV = self.findIndex(twoL)
        coordOne = (oneCharV,oneN)
        coordTwo = (twoCharV,twoN)
        rand = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        self.sim.elements[coordOne]["bg"] = rand
        self.sim.elements[coordOne].color = rand
        self.sim.elements[coordTwo]["bg"] = rand
        self.sim.elements[coordTwo].color = rand

        self.sim.wires.append([coordOne,coordTwo])
        print(self.sim.wires)

    def findIndex(self, char):
        charV = ord(char) - 96
        if charV <= 5:
            charV+=3
        else:
            charV+=4
        return  charV