from tkinter import *

class Switch(Frame):
    def __init__(self, master, sim):
        """ Switch(master, sim): creates a new Switch object
        :param master: (Tk)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.columnconfigure(0, minsize = 65)
        self.columnconfigure(1, minsize = 65)
        self.grid()

        self.master = master
        self.sim = sim

        Label(self, bg = "white", font = ("Arial", 14), text = "Switch Start").grid(row = 0, column = 0, columnspan = 2)
        Label(self, bg = "white", text = "Row").grid(row = 1, column = 0)
        Label(self, bg = "white", text = "Column").grid(row = 1, column = 1)
        self.startrow = Entry(self)
        self.startrow.grid(row = 2, column = 0)
        self.startcol = Entry(self)
        self.startcol.grid(row = 2, column = 1)

        Label(self, bg = "white", font = ("Arial", 14), text = "Switch End").grid(row = 3, column = 0, columnspan = 2)
        Label(self, bg = "white", text = "Row").grid(row = 4, column = 0)
        Label(self, bg = "white", text = "Column").grid(row = 4, column = 1)
        self.endrow = Entry(self)
        self.endrow.grid(row = 5, column = 0)
        self.endcol = Entry(self)
        self.endcol.grid(row = 5, column = 1)

        self.on = None

        Label(self, bg = "white", font = ("Arial", 14), text = "Status").grid(row = 6, column = 0, columnspan = 2)
        self.topButton = Button(self, bg = "white", text = "On", command = self.turnon)
        self.topButton.grid(row = 7, column = 0)
        self.bottomButton = Button(self, bg = "white", text = "Off", command = self.turnoff)
        self.bottomButton.grid(row = 7, column = 1)
        self.tb = Label(self, bg = "white", font = ("Arial", 12), text = "")
        self.tb.grid(row = 8, column = 0, columnspan = 2)

        self.submit = Button(self, bg = "white", text = "Submit", command = self.submit)
        self.submit.grid(row = 9, column = 0, columnspan = 2)

    def turnon(self):
        self.tb["text"] = "On"
        self.on = True

    def turnoff(self):
        self.tb["text"] = "Off"
        self.on = False

    def submit(self):
        labelList = ("", "+t", "-t", "", "a", "b", "c", "d", "e", "", "f", "g", "h", "i", "j", "", "-b", "+b", "")

        try:
            startrow = labelList.index(self.startrow.get())
            startcol = int(self.startcol.get())
            startcoord = (startrow, startcol)
            endrow = labelList.index(self.endrow.get())
            endcol = int(self.endcol.get())
            endcoord = (endrow, endcol)

            colorvalid = self.sim.elements[startcoord].color == "khaki1" and self.sim.elements[endcoord].color == "khaki1"
            startcoordvalid = startcoord[0] in [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17] and startcoord[1] in range(1, 51)
            endcoordvalid = endcoord[0] in [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17] and endcoord[1] in range(1, 51)

            if colorvalid and startcoordvalid and endcoordvalid and self.on != None:
                if startrow == endrow and startcol != endcol:
                    self.master.destroy()
                    self.sim.switched[startcoord] = self.on
                    self.sim.switched[endcoord] = self.on

                    self.sim.switchstarts[startcoord] = self.sim.elements[endcoord]
                    self.sim.switchends[endcoord] = self.sim.elements[startcoord]
                    for col in range(min(startcol, endcol), max(startcol, endcol) + 1):
                        if self.on:
                            self.sim.elements[(startrow, col)]["bg"] = "green2"
                            self.sim.elements[(startrow, col)].color = "green2"
                        else:
                            self.sim.elements[(startrow, col)]["bg"] = "red3"
                            self.sim.elements[(startrow, col)].color = "red3"

                elif startcol == endcol and startrow != endrow:
                    self.master.destroy()
                    self.sim.switched[startcoord] = self.on
                    self.sim.switched[endcoord] = self.on

                    self.sim.switchstarts[startcoord] = self.sim.elements[endcoord]
                    self.sim.switchends[endcoord] = self.sim.elements[startcoord]
                    for row in range(min(startrow, endrow), max(startrow, endrow) + 1):
                        if self.on:
                            self.sim.elements[(row, startcol)]["bg"] = "green2"
                            self.sim.elements[(row, startcol)].color = "green2"
                        else:
                            self.sim.elements[(row, startcol)]["bg"] = "red3"
                            self.sim.elements[(row, startcol)].color = "red3"
        except:
            pass

class SwitchEdit(Frame):
    def __init__(self, master, hole, sim):
        """ SwitchEdit(master): creates a new SwitchEdit object
        :param master: (Tk)
        :param hole: (Hole)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.columnconfigure(0, minsize = 65)
        self.columnconfigure(1, minsize = 65)
        self.grid()

        self.master = master
        self.hole = hole
        self.coord = self.hole.coord
        self.sim = sim
        self.on = None

        Label(self, bg = "white", font = ("Arial", 14), text = "Status").grid(row = 0, column = 0, columnspan = 2)
        self.topButton = Button(self, bg = "white", text = "On", command = self.turnon)
        self.topButton.grid(row = 1, column = 0)
        self.bottomButton = Button(self, bg = "white", text = "Off", command = self.turnoff)
        self.bottomButton.grid(row = 1, column = 1)
        self.tb = Label(self, bg = "white", font = ("Arial", 12), text = "")
        self.tb.grid(row = 2, column = 0, columnspan = 2)

        self.update = Button(self, bg = "white", text = "Update", command = self.update)
        self.update.grid(row = 3, column = 0, columnspan = 2)

        self.delete = Button(self, bg = "white", text = "Delete", command = self.delete)
        self.delete.grid(row = 4, column = 0, columnspan = 2)

    def turnon(self):
        self.tb["text"] = "On"
        self.on = True

    def turnoff(self):
        self.tb["text"] = "Off"
        self.on = False

    def update(self):
        endcoord = None
        try:
            endcoord = self.sim.switchends[self.coord].coord
        except:
            endcoord = self.sim.switchstarts[self.coord].coord

        self.master.destroy()
        self.sim.switched[self.coord] = self.on
        self.sim.switched[endcoord] = self.on

        if self.coord[0] == endcoord[0]:
            for col in range(min(self.coord[1], endcoord[1]), max(self.coord[1], endcoord[1]) + 1):
                if self.on:
                    self.sim.elements[(self.coord[0], col)]["bg"] = "green2"
                    self.sim.elements[(self.coord[0], col)].color = "green2"
                else:
                    self.sim.elements[(self.coord[0], col)]["bg"] = "red3"
                    self.sim.elements[(self.coord[0], col)].color = "red3"
        else:
            for row in range(min(self.coord[0], endcoord[0]), max(self.coord[0], endcoord[0]) + 1):
                if self.on:
                    self.sim.elements[(row, self.coord[1])]["bg"] = "green2"
                    self.sim.elements[(row, self.coord[1])].color = "green2"
                else:
                    self.sim.elements[(row, self.coord[1])]["bg"] = "red3"
                    self.sim.elements[(row, self.coord[1])].color = "red3"

    def delete(self):
        endcoord = None
        try:
            endcoord = self.sim.switchends[self.coord].coord
        except:
            endcoord = self.sim.switchstarts[self.coord].coord

        self.master.destroy()
        if self.coord[0] == endcoord[0]:
            for col in range(min(self.coord[1], endcoord[1]), max(self.coord[1], endcoord[1]) + 1):
                self.sim.elements[(self.coord[0], col)]["bg"] = "khaki1"
                self.sim.elements[(self.coord[0], col)].color = "khaki1"
        else:
            for row in range(min(self.coord[0], endcoord[0]), max(self.coord[0], endcoord[0]) + 1):
                self.sim.elements[(row, self.coord[1])]["bg"] = "khaki1"
                self.sim.elements[(row, self.coord[1])].color = "khaki1"

        del self.sim.switched[self.coord]
        del self.sim.switched[endcoord]

        try:
            del self.sim.switchstarts[endcoord]
            del self.sim.switchends[self.coord]

        except:
            del self.sim.switchends[endcoord]
            del self.sim.switchstarts[self.coord]