
try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as msgbox

from . import storage, weight_tab, mood_tab, food_tab, activity_tab, graph_tab

class WM():
    def __init__(self, parent):
        self.root = parent
        self.widgets = []
        self.values = storage.Storage()
        self.button_layout()
        self.on_home()
    
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
        t = tk.Label(self.root, text=self.values.database['food_cal'])
        self.widgets.append(t)
        t.grid(row=1, column=1, pady=10)
        
        t = tk.Label(self.root, text=self.values.database['activity_cal'])
        self.widgets.append(t)
        t.grid(row=1, column=2)

        t = tk.Label(self.root, text=self.values.database['current_weight'])
        self.widgets.append(t)
        t.grid(row=1, column=3)
        
        t = tk.Label(self.root, text=self.values.database['mood'])
        self.widgets.append(t)
        t.grid(row=1, column=4)
        
        t = tk.Label(self.root, text=self.values.database['cal_budget'])
        self.widgets.append(t)
        t.grid(row=1, column=5)
        
        t = tk.Label(self.root, text=self.values.database['cal_net'])
        self.widgets.append(t)
        t.grid(row=1, column=6)
        
        

        
    def on_food(self):
        self.clear()
        self.root.title('Food')
        self.food = food_tab.Food(self.root, self.widgets, self.values)
        
    def on_activity(self):
        self.clear()
        self.root.title('Activity')
        self.activity = activity_tab.Activity(self.root, self.widgets, self.values)
        
    def on_weight(self):
        self.clear()
        self.root.title('Weight')
        self.weight = weight_tab.Weight(self.root, self.widgets, self.values)
        
    def on_mood(self):
        self.clear()
        self.root.title('Mood')
        self.mood = mood_tab.Mood(self.root, self.widgets, self.values)
        
    def on_cal_budget(self):
        self.clear()
        self.root.title('Calorie Budget')
        self.weight = weight_tab.Weight(self.root, self.widgets, self.values)
        
    def on_net_cal(self):
        self.clear()
        self.root.title('Net Calories')
        
        t = tk.Label(self.root, text='inside of netcal')
        self.widgets.append(t)
        t.grid(row=1, column=0)
        
    def on_graph(self):
        self.clear()
        self.root.title('Graph')
        self.graph = graph_tab.Graph(self.root, self.widgets, self.values)
