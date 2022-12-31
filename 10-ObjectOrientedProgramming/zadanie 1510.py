import random
class Termometr:
    def __init__(self):
        self.is_on=False

    def turnon(self):
        self.is_on=True
    def turnoff(self):
        self.is_on=False
    
    def measure(self):
        self.temperature=round(random.uniform(34.0,42.0),1)

    def display(self):
        if self.is_on==True:
            if self.temperature>=37.0 and self.temperature<41.0:
                print(f'is on, temperature: {self.temperature} FEVER')
            elif self.temperature>41.0:
                print(f'is on, temperature: {self.temperature} DANGERUS')
            else:    
                print(f'is on, temperature: {self.temperature}')
        else:
            print(f'is off')


t=Termometr()
t.turnon()
t.measure()
t.display()
t.turnoff()
t.display()