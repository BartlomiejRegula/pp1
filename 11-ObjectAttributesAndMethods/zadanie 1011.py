class Phone():
    def __init__(self):
        self.ison=False
        self.volume=0
        self.wibracje=False

    def wlacz(self):
        self.ison=True

    def wylacz(self):
        self.ison=False

    def zwieksz_volume(self,volup):
        if self.volume+volup<=10:
            self.volume+=volup
    
    def zminiejsz_volume(self,voldown):
        if self.volume-voldown>=0:
            self.volume-=voldown

    #nie chce mi sie tego kończyć