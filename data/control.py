
try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk
	
from . import window_manager

class Control:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Weight Manager')
        self.root.resizable(0,0)
        #self.screensizeX = 800
        #self.screensizeY = 800

        #w, h, x, y = self.window_center(self.screensizeX, self.screensizeY)
        #self.root.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        #self.root.minsize(self.screensizeX, self.screensizeY)
        self.manager = window_manager.WM(self.root)
       # self.manager.button_layout()

        self.root.mainloop()
    def window_center(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        return (w, h, x, y)
        



        
