try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as msgbox

class Mood():
    def __init__(self, parent, widgets, values):
        self.root = parent
        self.widgets = widgets
        self.values = values
        
        self.textarea()

    def textarea(self):
        t = tk.Text(self.root, height=4)
        self.widgets.append(t)
        t.grid(row=1, column=0, columnspan=8)
        
        lbl_btn = tk.Button(self.root, text='Save', command='disabled')
        self.widgets.append(lbl_btn)
        lbl_btn.grid(row=2, column=3, columnspan=2, pady=10)

        t.insert(tk.INSERT, 'Enter any thoughts or messages you want to remember for today.')
        
        good = ['happy', 'energetic', 'satisfied', 'calm', 'peaceful', 'healthy', 'clear']
        for num, i in enumerate(good):
            happy = tk.Label(self.root, text=i)
            self.widgets.append(happy)
            happy.grid(row=3, column=num, pady=10)
            
        bad = ['unhappy', 'worn out', 'hungry', 'stressed', 'angry', 'sick', 'confused']
        for num, i in enumerate(bad):
            happy = tk.Label(self.root, text=i)
            self.widgets.append(happy)
            happy.grid(row=5, column=num, pady=10)
        
        for num, i in enumerate(good):
            happy_scaler = tk.Scale(self.root, length=200, from_=100, to=0)
            happy_scaler.set(50)
            self.widgets.append(happy_scaler)
            happy_scaler.grid(row=4, column=num)
        
        slider_btn = tk.Button(self.root, text='Save', command='disabled')
        self.widgets.append(slider_btn)
        slider_btn.grid(row=6, column=3, columnspan=2, pady=10)
