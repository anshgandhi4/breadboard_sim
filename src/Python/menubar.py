from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Python.breadboard import Breadboard
import ast

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

        runmenu = Menu(self.menubar, tearoff = 0)
        runmenu.add_command(label = "Simulation", command = self.simulation)
        self.menubar.add_cascade(label = "Run", menu = runmenu)

        helpmenu = Menu(self.menubar, tearoff = 0)
        helpmenu.add_command(label = "About", command = self.about)
        helpmenu.add_command(label = "Introduction", command = self.intropane)
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
            rowList = ast.literal_eval(rowList[0])

            messagebox.showinfo("Open File", "This process may take some time. Please wait...", parent = self.master)

            rawData = self.data_to_action(rowList)
            self.sim.breadboard.reset()

            for wire in rawData[0]:
                self.sim.create_wire(wire[0], wire[1], wire[2])
            for resistor in rawData[1]:
                self.sim.create_resistor(resistor[0], resistor[1], resistor[2])
            for led in rawData[2]:
                self.sim.create_led(led[0], led[1], led[2])
            for powersupply in rawData[3]:
                self.sim.create_powersupply(powersupply[0], powersupply[2])
            for switch in rawData[4]:
                self.sim.create_switch(switch[0], switch[1], switch[2])

            messagebox.showinfo("Open File", "File Opened", parent = self.master)

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension = ".txt")
        if filename:
            breadboardFile = open(filename, "w")
            savelist = self.sim.save()
            breadboardFile.write(str(savelist))
            breadboardFile.close()

    def intropane(self):
        self.sim.launchIntro()

    def simulation(self):
        messagebox.showinfo("Simulation", "Nice Circuit!", parent = self.master)

    def about(self):
        messagebox.showinfo("Breadboard Simulator", "This simulator was made by Ansh Gandhi and Jonathan Ma.", parent = self.master)

    def process_data(self, data):
        info = [[], [], [], [], []]
        for row in range(0, self.sim.height):
            for col in range(0, self.sim.length):
                coord = (row, col)
                for widgetdata in range(0, len(data)):
                    for subdata in data[widgetdata]:
                        if coord in subdata.keys():
                            info[widgetdata].append(coord)
        for subdata in range(0, len(info)):
            info[subdata] = list(set(info[subdata]))
        return info

    def analyze_data(self, infoList, data):
        rawData = [[], [], [], [], []]
        info = infoList.copy()
        coord1index = 0
        coord2index = 0
        for widgetdata in range(0, len(info)):
            while coord1index < len(info[widgetdata]):
                while coord2index < len(info[widgetdata]):
                    coord1 = info[widgetdata][coord1index]
                    coord2 = info[widgetdata][coord2index]
                    if widgetdata != 3:
                        if coord1 != coord2:
                            primarycoord = None
                            secondarycoord = None
                            try:
                                secondarycoord = data[widgetdata][0][coord1]
                                primarycoord = coord1
                            except:
                                try:
                                    secondarycoord = data[widgetdata][0][coord2]
                                    primarycoord = coord2
                                except:
                                    pass
                            if secondarycoord != None:
                                tempList = [primarycoord, secondarycoord, data[widgetdata][1][primarycoord]]
                                try:
                                    info[widgetdata].remove(primarycoord)
                                    info[widgetdata].remove(secondarycoord)
                                    coord1index -= 1
                                    coord2index -= 1
                                except:
                                    pass
                                rawData[widgetdata].append(tempList)
                    else:
                        if coord1 == coord2:
                            bcoord1 = None
                            if coord1 == (1, 1):
                                bcoord1 = (2, 1)
                            elif coord1 == (17, 1):
                                bcoord1 = (16, 1)
                            rawData[widgetdata].append([coord1, bcoord1, data[widgetdata][1][coord1]])
                            try:
                                info[widgetdata].remove(coord1)
                                coord1index -= 1
                                coord2index -= 1
                            except:
                                pass
                        else:
                            bcoord1 = None
                            bcoord2 = None
                            if coord1 == (1, 1):
                                bcoord1 = (2, 1)
                            elif coord1 == (17, 1):
                                bcoord1 = (16, 1)
                            if coord2 == (1, 1):
                                bcoord2 = (2, 1)
                            elif coord2 == (17, 1):
                                bcoord2 = (16, 1)
                            rawData[widgetdata].append([coord1, bcoord1, data[widgetdata][1][coord1]])
                            rawData[widgetdata].append([coord2, bcoord2, data[widgetdata][1][coord2]])
                            try:
                                info[widgetdata].remove(coord1)
                                info[widgetdata].remove(coord2)
                                coord1index -= 1
                                coord2index -= 1
                            except:
                                pass
                    coord2index += 1
                coord1index += 1
                coord2index = 0
        return rawData

    def data_to_action(self, dataList):
        data = [dataList[0 : 2], dataList[2 : 4], dataList[4 : 6], dataList[6 : 8], dataList[8 : 10]]
        info = self.process_data(data)
        return self.analyze_data(info, data)