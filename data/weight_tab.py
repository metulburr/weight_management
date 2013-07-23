try:
    import tkinter as tk
    import tkinter.messagebox as msgbox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as msgbox
    
from . import calendar_

class Weight():
    def __init__(self, parent, widgets, values):
        self.root = parent
        self.widgets = widgets
        self.values = values
        
        self.v = tk.StringVar()

        self.v.set('{} {} {}'.format(
            self.values.database['month_name'], self.values.database['day_selected'], self.values.database['year_selected']))
        
        #weight
        weight_text = 'Current Weight\n{}'.format(str(self.values.database['current_weight']))
        weight_lbl = tk.Label(self.root, text=weight_text)
        self.widgets.append(weight_lbl)
        weight_lbl.grid(row=1, column=0, columnspan=2)
        
        weight_var = tk.StringVar()
        weight_entry = tk.Entry(self.root, width=7, textvariable=weight_var)
        self.widgets.append(weight_entry)
        weight_entry.grid(row=2, column=0, columnspan=2)
        weight_var.set(self.values.database['current_weight'])
        
        weight_entry.bind('<Return>', lambda x: self.set_value(
            weight_var, weight_lbl, 'weight'))
        weight_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            weight_var, weight_lbl, 'weight'))
        self.widgets.append(weight_btn)
        weight_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        
        #starting weight
        start_text = 'Starting Weight\n{}'.format(str(self.values.database['start_weight']))
        start_lbl = tk.Label(self.root, text=start_text)
        self.widgets.append(start_lbl)
        start_lbl.grid(row=1, column=2, columnspan=2)
        
        start_var = tk.StringVar()
        start_entry = tk.Entry(self.root, width=7, textvariable=start_var)
        self.widgets.append(start_entry)
        start_entry.grid(row=2, column=2, columnspan=2)
        start_var.set(self.values.database['start_weight'])
        
        start_entry.bind('<Return>', lambda x: self.set_value(
            start_var, start_lbl, 'start'))
        start_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            start_var, start_lbl, 'start'))
        self.widgets.append(start_btn)
        start_btn.grid(row=3, column=2, columnspan=2, pady=10)
        
        
        #goal weight
        goal_text = 'Goal Weight\n{}'.format(str(self.values.database['goal_weight']))
        goal_lbl = tk.Label(self.root, text=goal_text)
        self.widgets.append(goal_lbl)
        goal_lbl.grid(row=1, column=4, columnspan=2)
        
        goal_var = tk.StringVar()
        goal_entry = tk.Entry(self.root, width=7, textvariable=goal_var)
        self.widgets.append(goal_entry)
        goal_entry.grid(row=2, column=4, columnspan=2)
        goal_var.set(self.values.database['goal_weight'])
        
        goal_entry.bind('<Return>', lambda x: self.set_value(
            goal_var, goal_lbl, 'goal'))
        goal_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            goal_var, goal_lbl, 'goal'))
        self.widgets.append(goal_btn)
        goal_btn.grid(row=3, column=4, columnspan=2, pady=10)
        
        
        #cal goal
        cal_text = 'Calorie Goal\n{}'.format(str(self.values.database['cal_budget']))
        cal_lbl = tk.Label(self.root, text=cal_text)
        self.widgets.append(cal_lbl)
        cal_lbl.grid(row=1, column=6, columnspan=2)
        
        cal_var = tk.StringVar()
        cal_entry = tk.Entry(self.root, width=7, textvariable=cal_var)
        self.widgets.append(cal_entry)
        cal_entry.grid(row=2, column=6, columnspan=2)
        cal_var.set(self.values.database['cal_budget'])
        
        cal_entry.bind('<Return>', lambda x: self.set_value(
            cal_var, cal_lbl, 'cal'))
        cal_btn = tk.Button(self.root, text='Save', command=lambda:self.set_value(
            cal_var, cal_lbl, 'cal'))
        self.widgets.append(cal_btn)
        cal_btn.grid(row=3, column=6, columnspan=2, pady=10)
        
        
        
        #progress section 
        lbl = labelframe = tk.Frame(self.root)
        font=("Georgia", "11", "bold")
        tk.Label(labelframe, font=font, width=20, text='Goal').grid(row=4, column=2, columnspan=2, pady=20)
        tk.Label(labelframe, font=font, width= 20, text='Current').grid(row=4, column=4, columnspan=2)
        tk.Label(labelframe, font=font, text='Date').grid(row=5, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Timespan').grid(row=6, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Weight').grid(row=7, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Pounds to Lose').grid(row=8, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Pounds per Day').grid(row=9, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Pounds per Week').grid(row=10, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Calories You Burn').grid(row=11, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Calories to Eliminate').grid(row=12, column=0, columnspan=2, sticky='e')
        tk.Label(labelframe, font=font, text='Calories to Eat').grid(row=13, column=0, columnspan=2, sticky='e')
        
        tk.Button(labelframe, text='Set', command=lambda:self.win()).grid(row=5, column=3, columnspan=2)
        
        tk.Label(labelframe, text=self.v.get()).grid(row=5, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.format_current_date()).grid(row=5, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.database['goal_timespan']).grid(row=6, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.database['current_timespan']).grid(row=6, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.database['goal_weight']).grid(row=7, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.database['current_weight']).grid(row=7, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.format_pounds2lose()).grid(row=8, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.format_pounds2lose('goal')).grid(row=8, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.database['goal_daypounds']).grid(row=9, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.database['current_daypounds']).grid(row=9, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.database['goal_weekpounds']).grid(row=10, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.database['current_weekpounds']).grid(row=10, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.database['goal_cal_burn']).grid(row=11, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.database['current_cal_burn']).grid(row=11, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.database['goal_cal2elim']).grid(row=12, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.database['current_cal2elim']).grid(row=12, column=4, columnspan=2) #current
        tk.Label(labelframe, text=self.values.database['goal_cal2eat']).grid(row=13, column=2, columnspan=2) #goal
        tk.Label(labelframe, text=self.values.database['current_cal2eat']).grid(row=13, column=4, columnspan=2) #current
        
        self.widgets.append(lbl)
        lbl.grid(row=4, column=0, columnspan=6)
        
    def upon_destroy(self, parent):
        parent.destroy
  
    def win(self):
        win = tk.Toplevel(self.root)
        win.title('Goal Date')
        cal = calendar_.Calendar(win, self.values)
        ok = tk.Button(win, width=5, text='OK', command=win.destroy)
        ok.grid(row=9, column=2, columnspan=3, pady=10)
        self.root.protocol('WM_DELETE_WINDOW', win.quit)
        win.focus_set() #take over input focus
        win.grab_set() #disable other windows while im open
        win.wait_window() #and wait here until win destroyed
        Weight(self.root, self.widgets, self.values)
        
    def set_value(self, strvar, widget, select=None):
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
        else:
            num = abs(int(strvar.get()))
            
        if num:
            if select == 'weight':
                weight_text = 'Current Weight\n{}'.format(str(num))
                widget.config(text=weight_text)
                self.values.database['current_weight'] = num
            elif select == 'start':
                start_weight = 'Starting Weight\n{}'.format(str(num))
                widget.config(text=start_weight)
                self.values.database['start_weight'] = num
            elif select == 'goal':
                goal_weight = 'Goal Weight\n{}'.format(str(num))
                widget.config(text=goal_weight)
                self.values.database['goal_weight'] = num
            elif select == 'cal':
                msg = 'Editing this value will override your calories goal selected by your settings\nIs this OK'
                if msgbox.askokcancel('Warning', msg):
                    cal = 'Calorie Goal\n{}'.format(str(num))
                    widget.config(text=cal)
                    self.values.database['cal_budget'] = num
                else:
                    var.set(self.values.database['cal_budget'])
            Weight(self.root, self.widgets, self.values) #make recursion to reset progress values in weight tab
        
