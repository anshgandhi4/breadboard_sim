from tkinter import *

class LED(Frame):
    def __init__(self, master, sim):
        """ LED(master, sim): creates a new LED object
        :param master: (Tk)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.columnconfigure(0, minsize = 65)
        self.columnconfigure(1, minsize = 65)
        self.grid()

        self.master = master
        self.sim = sim

        Label(self, bg = "white", font = ("Arial", 14), text = "LED Start").grid(row = 0, column = 0, columnspan = 2)
        Label(self, bg = "white", text = "Row").grid(row = 1, column = 0)
        Label(self, bg = "white", text = "Column").grid(row = 1, column = 1)
        self.startrow = Entry(self)
        self.startrow.grid(row = 2, column = 0)
        self.startcol = Entry(self)
        self.startcol.grid(row = 2, column = 1)

        Label(self, bg = "white", font = ("Arial", 14), text = "LED End").grid(row = 3, column = 0, columnspan = 2)
        Label(self, bg = "white", text = "Row").grid(row = 4, column = 0)
        Label(self, bg = "white", text = "Column").grid(row = 4, column = 1)
        self.endrow = Entry(self)
        self.endrow.grid(row = 5, column = 0)
        self.endcol = Entry(self)
        self.endcol.grid(row = 5, column = 1)

        Label(self, bg = "white", font = ("Arial", 14), text = "Color").grid(row = 6, column = 0, columnspan = 2)
        self.color = Entry(self)
        self.color.grid(row = 7, column = 0, columnspan = 2)

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

        color = self.color.get()

        taskSuccessful = self.create_led(color, startcoord, endcoord, self.sim)
        if taskSuccessful:
            self.master.destroy()

    @staticmethod
    def create_led(color, startcoord, endcoord, sim):
        startrow = startcoord[0]
        startcol = startcoord[1]
        endrow = endcoord[0]
        endcol = endcoord[1]

        if color in ["tomato", "saddle brown", "khaki1", "green2", "red3", "ivory3", "ivory4"]:
            color = "white"

        taskSuccessful = False

        try:
            colorvalid = sim.elements[startcoord].color == "khaki1" and sim.elements[endcoord].color == "khaki1"
            startcoordvalid = startcoord[0] in [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17] and startcoord[1] in range(1, 51)
            endcoordvalid = endcoord[0] in [1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17] and endcoord[1] in range(1, 51)

            if colorvalid and startcoordvalid and endcoordvalid:
                if startrow == endrow and startcol != endcol:
                    taskSuccessful = True
                    sim.ledcolors[startcoord] = color
                    sim.ledcolors[endcoord] = color

                    sim.ledstarts[startcoord] = endcoord
                    sim.ledends[endcoord] = startcoord
                    for col in range(min(startcol, endcol), max(startcol, endcol) + 1):
                        try:
                            sim.elements[(startrow, col)]["bg"] = color
                            sim.elements[(startrow, col)].color = color
                        except:
                            sim.elements[(startrow, col)]["bg"] = "white"
                            sim.elements[(startrow, col)].color = "white"

                elif startcol == endcol and startrow != endrow:
                    taskSuccessful = True
                    sim.ledcolors[startcoord] = color
                    sim.ledcolors[endcoord] = color

                    sim.ledstarts[startcoord] = endcoord
                    sim.ledends[endcoord] = startcoord
                    for row in range(min(startrow, endrow), max(startrow, endrow) + 1):
                        try:
                            sim.elements[(row, startcol)]["bg"] = color
                            sim.elements[(row, startcol)].color = color
                        except:
                            sim.elements[(row, startcol)]["bg"] = "white"
                            sim.elements[(row, startcol)].color = "white"
        except:
            pass

        return taskSuccessful

class LEDEdit(Frame):
    def __init__(self, master, hole, sim):
        """ LEDEdit(master): creates a new LEDEdit object
        :param master: (Tk)
        :param hole: (Hole)
        :param sim: (Simulator) """

        Frame.__init__(self, master, bg = "white")
        self.grid()

        self.master = master
        self.hole = hole
        self.coord = self.hole.coord
        self.sim = sim

        Label(self, bg = "white", font = ("Arial", 14), text = "Color").grid(row = 0, column = 0)
        self.color = Entry(self)
        self.color.grid(row = 1, column = 0)

        self.update = Button(self, bg = "white", text = "Update", command = self.update)
        self.update.grid(row = 2, column = 0)

        self.delete = Button(self, bg = "white", text = "Delete", command = self.delete)
        self.delete.grid(row = 3, column = 0)

    def update(self):
        color = self.color.get()

        endcoord = None
        try:
            endcoord = self.sim.ledends[self.coord]
        except:
            endcoord = self.sim.ledstarts[self.coord]

        if color not in ["tomato", "saddle brown", "khaki1", "green2", "red3", "ivory3", "ivory4"]:
            self.master.destroy()
            self.sim.ledcolors[self.coord] = color
            self.sim.ledcolors[endcoord] = color
            if self.coord[0] == endcoord[0]:
                for col in range(min(self.coord[1], endcoord[1]), max(self.coord[1], endcoord[1]) + 1):
                    try:
                        self.sim.elements[(self.coord[0], col)]["bg"] = color
                        self.sim.elements[(self.coord[0], col)].color = color
                    except:
                        self.sim.elements[(self.coord[0], col)]["bg"] = "white"
                        self.sim.elements[(self.coord[0], col)].color = "white"
            else:
                for row in range(min(self.coord[0], endcoord[0]), max(self.coord[0], endcoord[0]) + 1):
                    try:
                        self.sim.elements[(row, self.coord[1])]["bg"] = color
                        self.sim.elements[(row, self.coord[1])].color = color
                    except:
                        self.sim.elements[(row, self.coord[1])]["bg"] = "white"
                        self.sim.elements[(row, self.coord[1])].color = "white"

    def delete(self):
        endcoord = None
        try:
            endcoord = self.sim.ledends[self.coord]
        except:
            endcoord = self.sim.ledstarts[self.coord]

        self.master.destroy()
        if self.coord[0] == endcoord[0]:
            for col in range(min(self.coord[1], endcoord[1]), max(self.coord[1], endcoord[1]) + 1):
                self.sim.elements[(self.coord[0], col)]["bg"] = "khaki1"
                self.sim.elements[(self.coord[0], col)].color = "khaki1"
        else:
            for row in range(min(self.coord[0], endcoord[0]), max(self.coord[0], endcoord[0]) + 1):
                self.sim.elements[(row, self.coord[1])]["bg"] = "khaki1"
                self.sim.elements[(row, self.coord[1])].color = "khaki1"

        del self.sim.ledcolors[self.coord]
        del self.sim.ledcolors[endcoord]

        try:
            del self.sim.ledstarts[endcoord]
            del self.sim.ledends[self.coord]

        except:
            del self.sim.ledends[endcoord]
            del self.sim.ledstarts[self.coord]