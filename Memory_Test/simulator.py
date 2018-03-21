import tkinter as tk


class Application(tk.Frame):

    def start_simulator(self):
        print ("hi there, everyone!")

    def build_memory(self):
        self.rows = 2
        self.columns = 32
        # create the table of widgets
        vcmd = (self.register(self._validate), "%P")

        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(self.rows, weight=1)


    def createWidgets(self):
        # Start the Simulator
        self.Start = tk.Button(self)
        self.Start["text"] = "Start"
        self.Start["command"] = self.start_simulator
        # self.Start.pack(padx=10, pady=10, side=LEFT)
        self.Start.grid(row=0, column=0)

        # Pause the Simulator
        # Suggestion: Creating a constant check every cycle to see if this button is pressed.
        self.Pause = tk.Button(self)
        self.Pause["text"] = "Pause"
        # self.Pause["command"] = SET SOME VARIABLE FROM THE OTHER FILE TO BREAK A CONTINUE CONDITION
        self.Pause.grid(row=0, column=1)


        # Reset the Simulator (Basically calling start again
        self.Reset = tk.Button(self)
        self.Reset["text"] = "Reset"
        self.Reset["command"] = self.start_simulator
        self.Reset.grid(row=0, column=2)

        # Closes window
        self.EXIT = tk.Button(self)
        self.EXIT["text"] = "EXIT Simulator"
        self.EXIT["fg"] = "red"
        self.EXIT["command"] = self.EXIT
        self.EXIT.grid(row=0, column=3)

        self.build = tk.Button(self)
        self.build["text"] = "Build Table"
        self.build["command"] = self.build_memory
        # self.Start.pack(padx=10, pady=10, side=LEFT)
        self.build.grid(row=0, column=4)

        self.memoryLabel = tk.Label(self)
        self.memoryLabel["text"] = "Memory"
        self.memoryLabel.grid(row=1, column=0)






    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = tk.Tk()
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
root.destroy()
