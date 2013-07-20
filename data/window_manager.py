
try:
	import tkinter as tk
except ImportError:
	import Tkinter as tk

class WM:
    def __init__(self, r):
        self.root = r
        self.widgets = []
        self.button_layout()
        
        
        #test
        self.food_num = 240
        self.activity_num = 100
        self.weight_num = 300
        self.mood_num = 3
        self.cal_budget_num = 1913
        self.net_cal_num = -3202
        
        self.on_home()
    
    def clear(self):
        for w in self.widgets[:]:
            w.grid_forget()
            w.destroy()
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
        
        t = tk.Label(self.root, text='inside of weight')
        self.widgets.append(t)
        t.grid(row=1, column=0)
        
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
