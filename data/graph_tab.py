try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as msgbox

class Graph():
    def __init__(self, parent, widgets, values):
        self.root = parent
        self.widgets = widgets
        self.values = values
        
        self.options = [
            'Calorie Balance',
            'Calorie Intake',
            'Calorie Breakdown',
            'Caloires Burned',
            'Weight History',
            'BMI',
            'Measurement Hsitpry',
            'Mood History'
        ]
        
        var = tk.StringVar(self.root)
        var.set(self.options[0])
        
        optmenu = tk.OptionMenu(self.root, var, *self.options)
        self.widgets.append(optmenu)
        optmenu.grid(row=1, column=3, columnspan=2)
