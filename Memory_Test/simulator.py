import tkinter as tk
from tkinter import *
# from memory_demo import *
import memory_demo as md
import assembler


class Application(tk.Frame):

    # theClass = md.run()

    def start_simulator(self):
        # Add parameter pc for self.pcCount
        md.run(true_array,1,0)
        self.update_memory()
        self.update_cache()
        self.update_register()

    def pause_simulator(self):
        self.update_memory()
        self.update_cache()

    def step_simulator(self):
        md.run(true_array, 0, self.pcCount)
        self.update_memory()
        self.update_cache()
        self.update_register()

    def createWidgets(self):
        # Start the Simulator
        self.Start = tk.Button(self)
        self.Start["text"] = "Start/Reset"
        self.Start["command"] = self.start_simulator
        self.Start.grid(row=0, column=0)

        # Closes window
        self.EXIT = tk.Button(self)
        self.EXIT["text"] = "QUIT"
        self.EXIT["fg"] = "red"
        self.EXIT["command"] = self.quit
        self.EXIT.grid(row=0, column=1)


        self.pcCounter = tk.Label(self)
        self.pcCounter["text"] = "PC Counter:"
        self.pcCounter.grid(row=0, column=2)

        self.pcValue = tk.Label(self)
        self.pcValue["text"] = self.pcCount
        self.pcValue.grid(row=0, column=3)

        self.spacer = tk.Label(self)
        self.spacer["text"] = "   "
        self.spacer.grid(row=0, column=4)

        self.spacer = tk.Label(self)
        self.spacer["text"] = "   "
        self.spacer.grid(row=0, column=5)

        self.ccLabel = tk.Label(self)
        self.ccLabel["text"] = "Cycle Counter:   "
        self.ccLabel.grid(row=0, column=6)

        self.ccValue = tk.Label(self)
        self.ccValue["text"] = self.clockCycles
        self.ccValue.grid(row=0, column=7)

        for t in range(11, 33):
            self.build = tk.Label(self)
            self.build["text"] = "          "
            # self.build["command"] = self.build_memory
            self.build.grid(row=0, column=t)

        # ROW 0 ENDS HERE

        self.spacer = tk.Label(self)
        self.spacer["text"] = "   "
        self.spacer.grid(row=1, column=0)

        # Pause the Simulator
        # Suggestion: Creating a constant check every cycle to see if this button is pressed.
        self.Pause = tk.Button(self)
        self.Pause["text"] = "     Pause    "
        self.Pause["command"] = self.pause_simulator   # SET SOME VARIABLE FROM THE OTHER FILE TO BREAK A CONTINUE CONDITION
        self.Pause.grid(row=2, column=0)

        # Step
        self.Reset = tk.Button(self)
        self.Reset["text"] = "Step"
        self.Reset["command"] = self.step_simulator
        self.Reset.grid(row=2, column=1)

        # ROW 2 ENDS HERE

        self.spacer = tk.Label(self)
        self.spacer["text"] = "   "
        self.spacer.grid(row=3, column=0)

        self.memoryLabel = tk.Label(self)
        self.memoryLabel["text"] = "Memory Address :  Value"
        self.memoryLabel.grid(row=4, column=0)

        if self.initiator == 0:
            scrollbar1 = Scrollbar(root)
            scrollbar1.pack(side=LEFT, fill=Y)
            self.mylist1 = Listbox(root, yscrollcommand=scrollbar1.set)
            for line in range(100):
                if line < 10:
                    memoryValues.append(0)
                    self.mylist1.insert(END, str(line) + "                        :      " + str(memoryValues[line]))
                else:
                    memoryValues.append(0)
                    self.mylist1.insert(END, str(line) + "                      :      " + str(memoryValues[line]))
            self.mylist1.pack(side=LEFT, fill=BOTH)

            self.spacer = tk.Label(self)
            self.spacer["text"] = "   "
            self.spacer.grid(row=5, column=0)

            self.memoryLabel = tk.Label(self)
            self.memoryLabel["text"] = "       Register            :  Value"
            self.memoryLabel.grid(row=4, column=1)

            scrollbar2 = Scrollbar(root)
            scrollbar2.pack(side=LEFT, fill=Y)
            self.mylist2 = Listbox(root, yscrollcommand=scrollbar2.set)
            for line in range(32):
                if line < 10:
                    registerValues.append(0)
                    self.mylist2.insert(END, str(line) + "                        :      " + str(registerValues[line]))
                else:
                    registerValues.append(0)
                    self.mylist2.insert(END, str(line) + "                      :      " + str(registerValues[line]))
            self.mylist2.pack(side=LEFT, fill=BOTH)

            self.memoryLabel = tk.Label(self)
            self.memoryLabel["text"] = "       Cache              :  Value"
            self.memoryLabel.grid(row=4, column=2)

            scrollbar3 = Scrollbar(root)
            scrollbar3.pack(side=LEFT, fill=Y)
            self.mylist3 = Listbox(root, yscrollcommand=scrollbar3.set)
            for line in range(10):
                if line < 10:
                    cacheValues.append(0)
                    self.mylist3.insert(END, str(line) + "                        :      " + str(cacheValues[line]))
                else:
                    cacheValues.append(0)
                    self.mylist3.insert(END, str(line) + "                      :      " + str(cacheValues[line]))
            self.mylist3.pack(side=LEFT, fill=BOTH)
            self.initiator = 1
        else:
            scrollbar1 = Scrollbar(root)
            scrollbar1.pack(side=LEFT, fill=Y)
            mylist1 = Listbox(root, yscrollcommand=scrollbar1.set)
            for line in range(100):
                if line < 10:
                    mylist1.insert(END, str(line) + "                        :      " + str(memoryValues[line]))
                else:
                    mylist1.insert(END, str(line) + "                      :      " + str(memoryValues[line]))
            mylist1.pack(side=LEFT, fill=BOTH)

            self.spacer = tk.Label(self)
            self.spacer["text"] = "   "
            self.spacer.grid(row=5, column=0)

            self.memoryLabel = tk.Label(self)
            self.memoryLabel["text"] = "       Register            :  Value"
            self.memoryLabel.grid(row=4, column=1)

            scrollbar2 = Scrollbar(root)
            scrollbar2.pack(side=LEFT, fill=Y)
            mylist2 = Listbox(root, yscrollcommand=scrollbar2.set)
            for line in range(32):
                if line < 10:
                    mylist2.insert(END, str(line) + "                        :      " + str(registerValues[line]))
                else:
                    mylist2.insert(END, str(line) + "                      :      " + str(registerValues[line]))
            mylist2.pack(side=LEFT, fill=BOTH)

            self.memoryLabel = tk.Label(self)
            self.memoryLabel["text"] = "       Cache              :  Value"
            self.memoryLabel.grid(row=4, column=2)

            scrollbar3 = Scrollbar(root)
            scrollbar3.pack(side=LEFT, fill=Y)
            mylist3 = Listbox(root, yscrollcommand=scrollbar3.set)
            for line in range(10):
                if line < 10:
                    mylist3.insert(END, str(line) + "                        :      " + str(cacheValues[line]))
                else:
                    mylist3.insert(END, str(line) + "                      :      " + str(cacheValues[line]))
            mylist3.pack(side=LEFT, fill=BOTH)

    def increaseClockCycles(self):
        self.clockCycles = self.clockCycles + 1
        self.ccValue = tk.Label(self)
        self.ccValue.grid(row=0, column=7)
        self.ccValue["text"] = self.clockCycles


    def increasePCCounter(self):
        self.pcCount = self.pcCount + 1
        self.pcValue = tk.Label(self)
        self.pcValue["text"] = self.pcCount
        self.pcValue.grid(row=0, column=3)

    def edit_memory(self, slot, value):
        memoryValues[slot] = value
        self.mylist1.delete(slot, None)
        self.mylist1.insert(slot, str(slot) + "                        :      " + str(memoryValues[slot]))

    def edit_register(self, slot, value):
        registerValues[slot] = value
        self.mylist2.delete(slot, None)
        self.mylist2.insert(slot, str(slot) + "                        :      " + str(registerValues[slot]))

    def edit_cache(self, slot, value):
        cacheValues[slot] = value
        self.mylist3.delete(slot, None)
        self.mylist3.insert(slot, str(slot) + "                        :      " + str(cacheValues[slot]))

    def update_memory(self):
        for index in range(0,99):
            self.edit_memory(index,self.translate_to_int(md.main_memory.get_block(index)))

    def update_register(self):
        for index in range(0, 31):
            self.edit_register(index, self.translate_to_int(md.registers[index].get_block(0)))

    def update_cache(self):
        for index in range(0, 9):
            self.edit_cache(index, self.translate_to_int(md.cache[index].read()))

    def translate_to_int(self, translator):
        number = 0
        if '1' in translator:
            number = int("".join(str(x) for x in translator[translator.index('1'):]), 2)

        return number
        #  Translate the array of binary digits to binary.

    def translate_to_iter(self, translator):
        bin_arr = [int(d) for d in str(bin(binary))[2:]]
        # Translate binary into an array of binary digits.


    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.initiator = 0
        self.clockCycles = 0
        self.pcCount = 0
        self.initiator = 0
        self.createWidgets()

memoryValues = []
registerValues = []
cacheValues = []
mylist1 = []
mylist2 = []
mylist3 = []
new_list = []

# translator = []

file_name = "instructions.txt"

true_array = assembler.assemble(file_name)

root = tk.Tk()
root.geometry("800x400")
app = Application(master=root)
app.mainloop()
root.destroy()
