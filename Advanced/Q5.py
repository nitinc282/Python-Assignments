
class time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def __add__(self,other_time):
        total_minutes=self.minutes+other_time.minutes 
        minutes_left = total_minutes % 60
        extra_hours=total_minutes//60
        total_hours=self.hours+other_time.hours+ extra_hours
        t3=time(total_hours,minutes_left)
        return t3
    '''
    def displaytime(self):
        total_hours = self.hours * 60 + self.minutes
        return total_hours
    '''
    def displayminutes(self):
        total_minutes = self.hours * 60 + self.minutes
        return total_minutes





t1 = time(2, 50)
t2 = time(1, 20)
t3=t1 + t2
print(f"Time1:",t1.hours,"hour", t1.minutes, "min")
print(f"Time2:",t2.hours,"hour", t2.minutes, "min")
print(f"Time:",t3.hours,"hour", t3.minutes, "min")
print(f"Total minutes in Time 1:",t1.displayminutes())
print(f"Total minutes in Time 2:",t2.displayminutes())
print(f"Total minutes:",t3.displayminutes())





