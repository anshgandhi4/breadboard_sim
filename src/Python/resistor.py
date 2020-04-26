from tkinter import *

class Resistor(Frame):
    def __init__(self, master, sim):
        """ Resistor(master, sim): creates a new Resistor object
        :param master: (Tk)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.columnconfigure(0, minsize = 65)
        self.columnconfigure(1, minsize = 65)
        self.grid()

        self.master = master
        self.sim = sim

        Label(self, bg = "white", font = ("Arial", 14), text = "Resistor Start").grid(row = 0, column = 0, columnspan = 2)
        Label(self, bg = "white", text = "Row").grid(row = 1, column = 0)
        Label(self, bg = "white", text = "Column").grid(row = 1, column = 1)
        self.startrow = Entry(self)
        self.startrow.grid(row = 2, column = 0)
        self.startcol = Entry(self)
        self.startcol.grid(row = 2, column = 1)

        Label(self, bg = "white", font = ("Arial", 14), text = "Resistor End").grid(row = 3, column = 0, columnspan = 2)
        Label(self, bg = "white", text = "Row").grid(row = 4, column = 0)
        Label(self, bg = "white", text = "Column").grid(row = 4, column = 1)
        self.endrow = Entry(self)
        self.endrow.grid(row = 5, column = 0)
        self.endcol = Entry(self)
        self.endcol.grid(row = 5, column = 1)

        Label(self, bg = "white", font = ("Arial", 14), text = "Resistance (Ω)").grid(row = 6, column = 0, columnspan = 2)
        self.resistance = Entry(self)
        self.resistance.grid(row = 7, column = 0, columnspan = 2)

        self.submit = Button(self, bg = "white", text = "Submit", command = self.submit)
        self.submit.grid(row = 8, column = 0, columnspan = 2)

    def submit(self):
        labelList = ("", "+t", "-t", "", "a", "b", "c", "d", "e", "", "f", "g", "h", "i", "j", "", "-b", "+b", "")

        startrow = labelList.index(self.startrow.get())
        startcol = int(self.startcol.get())
        startcoord = (startrow, startcol)
        endrow = labelList.index(self.endrow.get())
        endcol = int(self.endcol.get())
        endcoord = (endrow, endcol)

        resistance = 0
        try:
            resistance = int(self.resistance.get())
        except:
            pass

        self.create_resistor(resistance, startcoord, endcoord, self.sim)

    def create_resistor(self, resistance, startcoord, endcoord, sim):
        startrow = startcoord[0]
        startcol = startcoord[1]
        endrow = endcoord[0]
        endcol = endcoord[1]

        try:
            colorvalid = sim.elements[startcoord].color == "khaki1" and self.sim.elements[endcoord].color == "khaki1"
            startcoordvalid = startcoord[0] in [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17] and startcoord[1] in range(1, 51)
            endcoordvalid = endcoord[0] in [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17] and endcoord[1] in range(1, 51)

            if colorvalid and startcoordvalid and endcoordvalid:
                if startrow == endrow and startcol != endcol:
                    self.master.destroy()
                    sim.resistances[startcoord] = resistance
                    sim.resistances[endcoord] = resistance

                    sim.resistorstarts[startcoord] = sim.elements[endcoord]
                    sim.resistorends[endcoord] = sim.elements[startcoord]
                    for col in range(min(startcol, endcol), max(startcol, endcol) + 1):
                        sim.elements[(startrow, col)]["bg"] = "saddle brown"
                        sim.elements[(startrow, col)].color = "saddle brown"

                elif startcol == endcol and startrow != endrow:
                    self.master.destroy()
                    sim.resistances[startcoord] = resistance
                    sim.resistances[endcoord] = resistance

                    sim.resistorstarts[startcoord] = sim.elements[endcoord]
                    sim.resistorends[endcoord] = sim.elements[startcoord]
                    for row in range(min(startrow, endrow), max(startrow, endrow) + 1):
                        sim.elements[(row, startcol)]["bg"] = "saddle brown"
                        sim.elements[(row, startcol)].color = "saddle brown"
        except:
            pass

class ResistorEdit(Frame):
    def __init__(self, master, hole, sim):
        """ ResistorEdit(master): creates a new ResistorEdit object
        :param master: (Tk)
        :param hole: (Hole)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.grid()

        self.master = master
        self.hole = hole
        self.coord = self.hole.coord
        self.sim = sim

        Label(self, bg = "white", font = ("Arial", 14), text = "Resistance").grid(row = 0, column = 0)
        self.currentText = Label(self, bg = "white", font = ("Arial", 12))
        self.currentText.grid(row = 1, column = 0)
        self.currentText["text"] = "Current Value: " + str(self.sim.resistances[self.coord])

        self.resistance = Entry(self)
        self.resistance.grid(row = 2, column = 0)

        self.update = Button(self, bg = "white", text = "Update", command = self.update)
        self.update.grid(row = 3, column = 0)

        self.delete = Button(self, bg = "white", text = "Delete", command = self.delete)
        self.delete.grid(row = 4, column = 0)

    def update(self):
        resistance = 0
        try:
            resistance = int(self.resistance.get())
        except:
            pass

        endcoord = None
        try:
            endcoord = self.sim.resistorends[self.coord].coord
        except:
            endcoord = self.sim.resistorstarts[self.coord].coord

        self.master.destroy()
        self.sim.resistances[self.coord] = resistance
        self.sim.resistances[endcoord] = resistance

    def delete(self):
        endcoord = None
        try:
            endcoord = self.sim.resistorends[self.coord].coord
        except:
            endcoord = self.sim.resistorstarts[self.coord].coord

        self.master.destroy()
        if self.coord[0] == endcoord[0]:
            for col in range(min(self.coord[1], endcoord[1]), max(self.coord[1], endcoord[1]) + 1):
                self.sim.elements[(self.coord[0], col)]["bg"] = "khaki1"
                self.sim.elements[(self.coord[0], col)].color = "khaki1"
        else:
            for row in range(min(self.coord[0], endcoord[0]), max(self.coord[0], endcoord[0]) + 1):
                self.sim.elements[(row, self.coord[1])]["bg"] = "khaki1"
                self.sim.elements[(row, self.coord[1])].color = "khaki1"

        del self.sim.resistances[self.coord]
        del self.sim.resistances[endcoord]

        try:
            del self.sim.resistorstarts[endcoord]
            del self.sim.resistorends[self.coord]

        except:
            del self.sim.resistorends[endcoord]
            del self.sim.resistorstarts[self.coord]