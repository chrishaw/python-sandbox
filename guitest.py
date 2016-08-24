import Tkinter as tk
from Tkinter import N, E, S, W, NE, NW, SE, SW, NSEW, EW, NS
import ttk

class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.padding = (3,3,3,3)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.grid(padx=5, pady=5, sticky=NSEW)
        self.relief = "solid"
        self.borderwidth = 5

        ttk.Label(self, text="Hello world").grid(row=0, column=0)

        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hello World Application")
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    MainApplication(root) #.pack(side="top", fill="both", expand=True)
    root.mainloop()