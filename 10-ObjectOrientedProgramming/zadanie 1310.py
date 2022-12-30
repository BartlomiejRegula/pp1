class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False

    # def channel_no(self):
    #     self.
            
    def change_channel(self,num):
        self.channel_no=num

    def set_channels(self,lista):
        for i in lista:
            self.channels.append(i)
        
    def show_channels(self):
        print('dostepne kanaly', self.channels)

    def increase_volume(self,ile):
        self.volume+=ile
        if self.volume>10:
            self.volume=10

    def decrease_volume(self,ile):
        self.volume-=ile
        if self.volume<0:
            self.volume=0

    def show_status(self):
        if self.is_on==True:
            try:
                print(f"TV is on, channel", self.channel_no, "(",self.channels[self.channel_no-1],")",'volume(',self.volume,')')
            except:
                print(f"TV is on, channel", self.channel_no,'volume(',self.volume,')')
        else:
            print('TV is off')    

tv=TV()
tv.set_channels(['TVP1',"TVP2",'Polsat','TVN','Filmbox','Discovery'])
tv.show_status()
tv.turn_on()
tv.change_channel(1)
tv.show_status()
tv.change_channel(3)
tv.show_status()
tv.change_channel(4)
tv.show_status()
tv.change_channel(5)
tv.show_status()
tv.change_channel(6)
tv.show_status()
tv.change_channel(3)
tv.show_status()
tv.show_channels()
tv.increase_volume(15)
tv.show_status()
tv.decrease_volume(2)
tv.show_status()