from tkinter import *

class PowerSupply(Frame):
    def __init__(self, master, sim):
        """ PowerSupply(master): creates a new PowerSupply object
        :param master: (Tk)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.columnconfigure(0, minsize = 65)
        self.columnconfigure(1, minsize = 65)
        self.grid()

        self.master = master
        self.sim = sim
        self.coord = None

        self.locationText = Label(self, bg = "white", font = ("Arial", 14), text = "Power Supply Bus")
        self.locationText.grid(row = 0, column = 0, columnspan = 2)
        self.topButton = Button(self, bg = "white", text = "Top", command = self.createtop)
        self.topButton.grid(row = 1, column = 0)
        self.bottomButton = Button(self, bg = "white", text = "Bottom", command = self.createbottom)
        self.bottomButton.grid(row = 1, column = 1)
        self.tb = Label(self, bg = "white", font = ("Arial", 12), text = "")
        self.tb.grid(row = 2, column = 0, columnspan = 2)

        self.voltageText = Label(self, bg = "white", font = ("Arial", 14), text = "Voltage (V)")
        self.voltageText.grid(row = 4, column = 0, columnspan = 2)
        self.voltage = Entry(self)
        self.voltage.grid(row = 5, column = 0, columnspan = 2)

        self.submit = Button(self, bg = "white", text = "Submit", command = self.submit)
        self.submit.grid(row = 6, column = 0, columnspan = 2)

        if self.sim.elements[(1, 1)].color != "khaki1":
            self.topButton["state"] = DISABLED
        if self.sim.elements[(17, 1)].color != "khaki1":
            self.bottomButton["state"] = DISABLED

    def createtop(self):
        self.tb["text"] = "Top"
        self.coord = (1, 1)

    def createbottom(self):
        self.tb["text"] = "Bottom"
        self.coord = (17, 1)

    def submit(self):
        voltage = 0
        try:
            voltage = int(self.voltage.get())
        except:
            pass

        self.master.destroy()
        self.sim.supplies[self.coord] = self.sim.elements[self.coord]
        self.sim.voltages[self.coord] = voltage
        self.sim.elements[self.coord]["bg"] = "tomato"
        self.sim.elements[self.coord].color = "tomato"

class PowerSupplyEdit(Frame):
    def __init__(self, master, hole, sim):
        """ PowerSupplyEdit(master): creates a new PowerSupplyEdit object
        :param master: (Tk)
        :param hole: (Hole)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.grid()

        self.master = master
        self.hole = hole
        self.coord = self.hole.coord
        self.sim = sim

        self.voltageText = Label(self, bg = "white", font = ("Arial", 14), text = "Voltage (V)")
        self.voltageText.grid(row = 0, column = 0)
        self.currentText = Label(self, bg = "white", font = ("Arial", 12))
        self.currentText.grid(row = 1, column = 0)
        self.currentText["text"] = "Current Value: " + str(self.sim.voltages[self.coord])
        self.voltage = Entry(self)
        self.voltage.grid(row = 2, column = 0)

        self.update = Button(self, bg = "white", text = "Update", command = self.update)
        self.update.grid(row = 3, column = 0)

        self.delete = Button(self, bg = "white", text = "Delete", command = self.delete)
        self.delete.grid(row = 4, column = 0)

    def update(self):
        voltage = 0
        try:
            voltage = int(self.voltage.get())
        except:
            pass

        self.master.destroy()
        self.sim.voltages[self.coord] = voltage

    def delete(self):
        self.master.destroy()
        del self.sim.supplies[self.coord]
        del self.sim.voltages[self.coord]
        self.hole["bg"] = "khaki1"
        self.hole.color = "khaki1"