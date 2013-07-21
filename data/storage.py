
class Storage:
    def __init__(self):
        
        #weight
        self.food_num = 0
        self.activity_num = 0
        self.weight_num = 250
        self.mood_num = 10
        self.cal_budget_num = 2000
        self.net_cal_num = -3000
        self.start_weight = 260
        self.goal_weight = 200
        #progress
        self.goal_date = 'Feb 7 2013'
        self.current_date = 'now placeholder'
        self.goal_timespan = '4 Weeks 2 Days'
        self.current_timespan = '2 Weeks 0 Days'
        self.goal_pound2lose = self.weight_num - self.goal_weight
        self.current_pound2lose = self.weight_num - self.goal_weight
        self.goal_daypounds = 'dtest'
        self.current_daypounds = 'dtest'
        self.goal_weekpounds = 'wtest'
        self.current_weekpounds = 'wtest'
        self.goal_cal_burn = 0
        self.current_cal_burn = 0
        self.goal_cal2elim = 0
        self.current_cal2elim = 0
        self.goal_cal2eat = 0
        self.current_cal2eat = 0
