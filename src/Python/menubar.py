from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Python.breadboard import Breadboard
import ast
from collections import defaultdict

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

        self.graph = defaultdict(list)
        self.bfswid = []
        self.pairs = []
        self.traversedList = []

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
        savelist = self.sim.save()
        rawData = self.data_to_action(savelist)

        # messagebox.showinfo("Simulation", "Simulation Running", parent = self.master)
        # ledData = []
        # allleds = []
        # for led in rawData[2]:
        #     ledData.append([-1, -1, -1, -1])
        #     allleds.append(led[0])
        #     allleds.append(led[1])
        # if len(rawData[2]) != 0: # ps must be there too
        #     starttime = time.perf_counter()
        #     busgroups = []
        #     for ps in rawData[3]:
        #         busgroups.append(ps[0][0])
        #         busgroups.append(ps[1][0])
        #     busgroups = list(set(busgroups))
        #     enabledGroups = busgroups.copy()
        #     for bus in busgroups:
        #         for hole in bus.holes:
        #             if hole.coord in rawData[0]: # if component FIX
        #                 if hole.coord in allleds:
        #                     ledindex = allleds.index(hole.coord)
        #
        #     # for every unit in power supply group
        #     # if there is a component, go to the other end
        #     # for every unit in the end
        #     # if the unit is led, then set ledvar to true
        #     # if the group was not enabled, enable it and continue recursion
        #     # repeat
        #     # repeat same thing for other end of power supply
        #     # repeat everything for the other power supply
        #     # if both globals are true then light led and exit
        #     # if timer is more than 20 seconds, exit
        #
        # time.sleep(2)
        # messagebox.showinfo("Simulation", "Simulation Complete", parent = self.master)

        components = []
        pses = []
        groups = []
        for widget in range(0, len(rawData)):
            if widget != 3:
                for component in rawData[widget]:
                    start = component[0]
                    end = component[1]
                    components.append(start)
                    components.append(end)
                    groups.append(self.sim.elements[start].group)
                    groups.append(self.sim.elements[end].group)
                    startnum = start[0] * 50 + start[1]
                    endnum = end[0] * 50 + end[1]
                    self.add(startnum, endnum)
                    self.add(endnum, startnum)
            if widget == 3:
                for component in rawData[widget]:
                    ps = component[0]
                    psnum = ps[0] * 50 + ps[1]
                    components.append(ps)
                    pses.append(psnum)
                    self.add(psnum, psnum)
                    groups.append(self.sim.elements[ps].group)
        print(components)
        print(pses)
        print(groups)

        for pair in self.pairs:
            p1 = pair[0]
            p2 = pair[1]
            if p1 != p2:
                self.graph[self.bfswid.index(p1)].append(self.bfswid.index(p2))
            else:
                row = int(p1 / 50)
                col = p1 % 50
                if col == 0:
                    col = 50
                coord = (row, col)
                group = self.sim.elements[coord].group
                holes = []
                for hole in group.holes:
                    if hole.coord in components:
                        holenum = hole.coord[0] * 50 + hole.coord[1]
                        holes.append(self.bfswid.index(holenum))
                for hole in range(1, len(holes)):
                    self.graph[holes[0]].append(holes[hole])
                    self.graph[holes[hole]].append(holes[0])
        print(self.pairs)
        print(self.bfswid)
        print(self.graph)
        # self.bfs(pses[0][0] * 50 + pses[0][1])
        # print(self.traversedList)

    def add(self, u, v):
        if u not in self.bfswid:
            self.bfswid.append(u)
        if v not in self.bfswid:
            self.bfswid.append(v)
        self.pairs.append((u, v))

    def bfs(self, s):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            self.traversedList.append(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True

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