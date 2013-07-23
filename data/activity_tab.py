try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as msgbox

class Activity():
    def __init__(self, parent, widgets, values):
        self.root = parent
        self.widgets = widgets
        self.values = values
        
        s = tk.StringVar()
        e = tk.Entry(self.root, textvariable=s)
        self.widgets.append(e)
        e.grid(row=1, column=0, columnspan=7, ipadx=250, pady=10)
        s.set('What did you do today?')
        
        #e.bind('<Return>', lambda x:print('test'))
        search_btn = tk.Button(self.root, text='Search', command='disabled')
        self.widgets.append(search_btn)
        search_btn.grid(row=1, column=7)
