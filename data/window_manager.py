
try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as msgbox

from . import storage, weight_tab

class WM():
    def __init__(self, parent):
        self.root = parent
        self.widgets = []
        
        self.values = storage.Storage()
        

        #test
        '''
        self.food_num = 0
        self.activity_num = 0
        self.weight_num = 250
        self.mood_num = 10
        self.cal_budget_num = 2000
        self.net_cal_num = -3000
        self.start_weight = 260
        self.goal_weight = 200
        '''
        
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
        t = tk.Label(self.root, text=self.values.food_num)
        self.widgets.append(t)
        t.grid(row=1, column=1)
        
        t = tk.Label(self.root, text=self.values.activity_num)
        self.widgets.append(t)
        t.grid(row=1, column=2)

        t = tk.Label(self.root, text=self.values.weight_num)
        self.widgets.append(t)
        t.grid(row=1, column=3)
        
        t = tk.Label(self.root, text=self.values.mood_num)
        self.widgets.append(t)
        t.grid(row=1, column=4)
        
        t = tk.Label(self.root, text=self.values.cal_budget_num)
        self.widgets.append(t)
        t.grid(row=1, column=5)
        
        t = tk.Label(self.root, text=self.values.net_cal_num)
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
        
        self.weight = weight_tab.Weight(self.root, self.widgets, self.values)

        
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
