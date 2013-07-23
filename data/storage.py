
import time

class Storage:
    def __init__(self):
        '''
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
        '''
        self.database = {
            'food_cal': 0,
            'activity_cal': 0,
            'current_weight': 0,
            'mood': 0,
            'cal_budget': 2000,
            'cal_net': 0,
            'start_weight': 0,
            'goal_weight': 0,
            
            'goal_date': 0,
            'current_date': 0,
            'goal_timespan': 0,
            'current_timespan': 0,
            'goal_pounds2lose': 0,
            'current_pounds2lose': 0,
            'goal_daypounds': 0,
            'current_daypounds': 0,
            'goal_weekpounds': 0,
            'current_weekpounds': 0,
            'goal_cal_burn': 0,
            'current_cal_burn': 0,
            'goal_cal2elim': 0,
            'current_cal2elim': 0,
            'goal_cal2eat': 0,
            'current_cal2eat': 0,
        }
        
    def format_current_date(self):
        self.database['current_date'] = time.time()
        return time.strftime('%B %d %Y', time.localtime(self.database['current_date']))
        
