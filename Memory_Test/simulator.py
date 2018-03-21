from tkinter import *

class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        # Start the Simulator
        self.Start = Button(self)
        self.Start["text"] = "Start"
        #  self.Start["command"] = CALL TO CACHE METHOD OR WRITE THE FOR LOOP HERE
        self.Start.pack({"side": "left"})

        # Pause the Simulator
        # Suggestion: Creating a constant check every cycle to see if this button is pressed.
        self.Pause = Button(self)
        self.Pause["text"] = "Pause"
        # self.Pause["command"] = SET SOME VARIABLE FROM THE OTHER FILE TO BREAK A CONTINUE CONDITION
        self.Pause.pack({"side": "left"})

        # Reset the Simulator (Basically calling start again
        self.Reset = Button(self)
        self.Reset["text"] = "Reset"
        # self.Reset["command"] = SAME AS START COMMAND
        self.Reset.pack({"side": "left"})

        # Closes window
        self.EXIT = Button(self)
        self.EXIT["text"] = "EXIT Simulator"
        self.EXIT["fg"] = "red"
        self.EXIT["command"] = self.EXIT
        self.EXIT.pack({"side": "left"})




    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
root.destroy()
