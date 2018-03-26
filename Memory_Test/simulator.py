import tkinter as tk


class Application(tk.Frame):


    def createWidgets(self):
        # Start the Simulator
        self.Start = tk.Button(self)
        self.Start["text"] = "Start"
        # self.Start["command"] = self.start_simulator
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
        self.Reset["command"] = self.updateMemory()
        self.Reset.grid(row=0, column=2)

        # Closes window
        self.EXIT = tk.Button(self)
        self.EXIT["text"] = "EXIT Simulator"
        self.EXIT["fg"] = "red"
        self.EXIT["command"] = self.quit
        self.EXIT.grid(row=0, column=3)

        self.build = tk.Button(self)
        self.build["text"] = "Build Table"
        # self.build["command"] = self.build_memory
        self.build.grid(row=0, column=4)

        self.memoryLabel = tk.Label(self)
        self.memoryLabel["text"] = "Memory"
        self.memoryLabel.grid(row=1, column=0)



    def updateMemory(self):
        index = 0
        for r in range(2,10):
            for c in range(2,10):
                self.memoryLabel = tk.Label(self)
                self.memoryLabel.grid(row = r, column = c)
                self.memoryLabel["text"] = memorySpots[index]
                index = index+1

    def edit_memory(self, slot, value):
        memorySpots[slot] = value
        self.updateMemory

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()



memorySpots = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[1, 0],[1, 1],[1, 2],[1, 3],[1, 4],[1, 5],[1, 6],[1, 7],[2, 0],[2, 1],[2, 2],[2, 3],[2, 4],[2, 5],[2, 6],[2, 7],[3, 0],[3, 1],[3, 2],[3, 3],[3, 4],[3, 5],[3, 6],[3, 7],[4, 0],[4, 1],[4, 2],[4, 3],[4, 4],[4, 5],[4, 6],[4, 7],[5, 0],[5, 1],[5, 2],[5, 3],[5, 4],[5, 5],[5, 6],[5, 7],[6, 0],[6, 1],[6, 2],[6, 3],[6, 4],[6, 5],[6, 6],[6, 7],[7, 0],[7, 1],[7, 2],[7, 3],[7, 4],[7, 5],[7, 6],[7, 7]]

root = tk.Tk()
root.geometry("800x400")
app = Application(master=root)
app.mainloop()
root.destroy()
