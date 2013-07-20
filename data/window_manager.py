
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class WM:
    def __init__(self, parent):
        self.root = parent
        self.widgets = []

        self.body = tk.Frame(self.root, height=500)

        #test
        self.food_num = 0
        self.activity_num = 0
        self.weight_num = 200
        self.mood_num = 10
        self.cal_budget_num = 2000
        self.net_cal_num = -3000
        
        self.button_layout()
        self.on_home()
        
    def body_frame(self):
        self.widgets.append(self.body)
        self.body.grid(row=1, column=0)
    
    def clear(self):
        for w in self.widgets[:]:
            w.grid_forget()
            #w.destroy()
            self.widgets.remove(w)
        
    def button_layout(self):
        tk.Button(self.root, height=2, width=10, text="Home", command=lambda:self.on_home()).grid(
            row=0, column=0)
        tk.Button(self.root, height=2, width=10, text="Food", command=lambda:self.on_food()).grid(
            row=0, column=1)
        tk.Button(self.root, height=2, width=10, text="Activity", command=lambda:self.on_activity()).grid(
            row=0, column=2)
        tk.Button(self.root, height=2, width=10, text="Weight", command=lambda:self.on_weight()).grid(
            row=0, column=3)
        tk.Button(self.root, height=2, width=10, text="Mood", command=lambda:self.on_mood()).grid(
            row=0, column=4)
        tk.Button(self.root, height=2, width=10, text="Calorie\nBudget", command=lambda:self.on_cal_budget()).grid(
            row=0, column=5)
        tk.Button(self.root, height=2, width=10, text="Net\nCalories", command=lambda:self.on_net_cal()).grid(
            row=0, column=6)
        tk.Button(self.root, height=2, width=10, text="Graph", command=lambda:self.on_graph()).grid(
            row=0, column=7)
            
    def on_home(self):
        self.clear()
        self.root.title('Home')
        
        
        #display all values for corresponding section
        t = tk.Label(self.root, text=self.food_num)
        self.widgets.append(t)
        t.grid(row=1, column=1)
        
        t = tk.Label(self.root, text=self.activity_num)
        self.widgets.append(t)
        t.grid(row=1, column=2)

        t = tk.Label(self.root, text=self.weight_num)
        self.widgets.append(t)
        t.grid(row=1, column=3)
        
        t = tk.Label(self.root, text=self.mood_num)
        self.widgets.append(t)
        t.grid(row=1, column=4)
        
        t = tk.Label(self.root, text=self.cal_budget_num)
        self.widgets.append(t)
        t.grid(row=1, column=5)
        
        t = tk.Label(self.root, text=self.net_cal_num)
        self.widgets.append(t)
        t.grid(row=1, column=6)
        
        

        
    def on_food(self):
        self.clear()
        self.root.title('Food')
        
        t = tk.Label(self.root, text='inside of food')
        self.widgets.append(t)
        t.grid(row=1, column=0)
        

       
        
        
    def on_activity(self):
        self.clear()
        self.root.title('Activity')

        t = tk.Label(self.root, text='inside of Activity')
        self.widgets.append(t)
        t.grid(row=1, column=0)
        
    def on_weight(self):
        self.clear()
        self.root.title('Weight')
        
        t = tk.Label(self.root, text='Weight\n' + str(self.weight_num))
        self.widgets.append(t)
        t.grid(row=1, column=0, pady=10)
        
        v = tk.StringVar()
        e = tk.Entry(self.root, width=5, textvariable=v)
        self.widgets.append(e)
        e.grid(row=2, column=0)
        v.set(self.weight_num)

        btn = tk.Button(self.root, text='Save', command=lambda:self.set_weight_value(v,t))
        self.widgets.append(btn)
        btn.grid(pady=10)
        
    def set_weight_value(self, v, t):
        if not v.get():
            self.weight_num = 0
        elif not v.get().isdigit():                     #if not digit
            try:
                self.weight_num = float(v.get())
            except ValueError:                          #if not float
                self.weight_num = 0
        else:
            self.weight_num = int(v.get())
        t.config(text='Weight\n' + str(self.weight_num))
        
        
        
        
    def on_mood(self):
        self.clear()
        self.root.title('Mood')
        
        t = tk.Label(self.root, text='inside of mood')
        self.widgets.append(t)
        t.grid(row=1, column=0)
        
    def on_cal_budget(self):
        self.clear()
        self.root.title('Calorie Budget')
        
        t = tk.Label(self.root, text='inside of calbud')
        self.widgets.append(t)
        t.grid(row=1, column=0)
        
    def on_net_cal(self):
        self.clear()
        self.root.title('Net Calories')
        
        t = tk.Label(self.root, text='inside of netcal')
        self.widgets.append(t)
        t.grid(row=1, column=0)
       
        
    def on_graph(self):
        self.clear()
        self.root.title('Graph')
        
        t = tk.Label(self.root, text='inside of gragh')
        self.widgets.append(t)
        t.grid(row=1, column=0)
