try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as msgbox

class Weight(window_manager.WB):
    def __init__(self, parent, widgets, weight, start, goal, cal):
        self.root = parent
        self.widgets = widgets
        self.weight_num = weight
        self.start_weight = start
        self.goal_weight = goal
        self.cal_budget_num = cal
        #pass 
        #weight
        weight_text = 'Current Weight\n{}'.format(str(self.weight_num))
        weight_lbl = tk.Label(self.root, text=weight_text)
        self.widgets.append(weight_lbl)
        weight_lbl.grid(row=1, column=0, columnspan=2)
        
        weight_var = tk.StringVar()
        weight_entry = tk.Entry(self.root, width=7, textvariable=weight_var)
        self.widgets.append(weight_entry)
        weight_entry.grid(row=2, column=0, columnspan=2)
        weight_var.set(self.weight_num)
        
        weight_entry.bind('<Return>', lambda x: self.set_value(
            weight_var, weight_lbl, 'weight'))
        weight_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            weight_var, weight_lbl, 'weight'))
        self.widgets.append(weight_btn)
        weight_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        #starting weight
        start_text = 'Starting Weight\n{}'.format(str(self.start_weight))
        start_lbl = tk.Label(self.root, text=start_text)
        self.widgets.append(start_lbl)
        start_lbl.grid(row=1, column=2, columnspan=2)
        
        start_var = tk.StringVar()
        start_entry = tk.Entry(self.root, width=7, textvariable=start_var)
        self.widgets.append(start_entry)
        start_entry.grid(row=2, column=2, columnspan=2)
        start_var.set(self.start_weight)
        
        start_entry.bind('<Return>', lambda x: self.set_value(
            start_var, start_lbl, 'start'))
        start_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            start_var, start_lbl, 'start'))
        self.widgets.append(start_btn)
        start_btn.grid(row=3, column=2, columnspan=2, pady=10)
        
        
        #goal weight
        goal_text = 'Goal Weight\n{}'.format(str(self.goal_weight))
        goal_lbl = tk.Label(self.root, text=goal_text)
        self.widgets.append(goal_lbl)
        goal_lbl.grid(row=1, column=4, columnspan=2)
        
        goal_var = tk.StringVar()
        goal_entry = tk.Entry(self.root, width=7, textvariable=goal_var)
        self.widgets.append(goal_entry)
        goal_entry.grid(row=2, column=4, columnspan=2)
        goal_var.set(self.goal_weight)
        
        goal_entry.bind('<Return>', lambda x: self.set_value(
            goal_var, goal_lbl, 'goal'))
        goal_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            goal_var, goal_lbl, 'goal'))
        self.widgets.append(goal_btn)
        goal_btn.grid(row=3, column=4, columnspan=2, pady=10)
        
        
        #cal goal
        cal_text = 'Calorie Goal\n{}'.format(str(self.cal_budget_num))
        cal_lbl = tk.Label(self.root, text=cal_text)
        self.widgets.append(cal_lbl)
        cal_lbl.grid(row=1, column=6, columnspan=2)
        
        cal_var = tk.StringVar()
        cal_entry = tk.Entry(self.root, width=7, textvariable=cal_var)
        self.widgets.append(cal_entry)
        cal_entry.grid(row=2, column=6, columnspan=2)
        cal_var.set(self.cal_budget_num)
        
        cal_entry.bind('<Return>', lambda x: self.set_value(
            cal_var, cal_lbl, 'cal', cal_var))
        cal_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            cal_var, cal_lbl, 'cal', cal_var))
        self.widgets.append(cal_btn)
        cal_btn.grid(row=3, column=6, columnspan=2, pady=10)
        
    def set_value(self, strvar, widget, select=None, var=None):
        num = False
        if not strvar.get():
            msgbox.showwarning('Warning', 'Entry field cannot be empty!')
        elif len(strvar.get()) >= 7: #123.567:
            msgbox.showwarning('Warning', 'Entry field must contain 7 or less characters!')
        elif not strvar.get().isdigit():                     #if not digit
            try:
                num = abs(float(strvar.get()))
                
            except ValueError:  
                msgbox.showwarning('Warning', 'Field must be a number!')
                var.set(num)
        else:
            num = abs(int(strvar.get()))
            
        if num:
            if select == 'weight':
                weight_text = 'Current Weight\n{}'.format(str(num))
                widget.config(text=weight_text)
                self.weight_num = num
            elif select == 'start':
                start_weight = 'Starting Weight\n{}'.format(str(num))
                widget.config(text=start_weight)
                self.start_weight = num
            elif select == 'goal':
                goal_weight = 'Goal Weight\n{}'.format(str(num))
                widget.config(text=goal_weight)
                self.goal_weight = num
            elif select == 'cal':
                msg = 'Editing this value will override your calories goal selected by your settings\nIs this OK'
                if msgbox.askokcancel('Warning', msg):
                    cal = 'Calorie Goal\n{}'.format(str(num))
                    widget.config(text=cal)
                    self.cal_budget_num = num
                else:
                    var.set(self.cal_budget_num)
        