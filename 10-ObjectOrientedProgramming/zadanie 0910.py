class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False

    # def channel_no(self):
    #     self.

    def show_status(self):
        if self.is_on==True:
            print('TV is on',)
            print(f'kanal to: {self.channel_no}')
        else:
            print('TV is off')
            
    def set_channel(self,num):
        self.channel_no=num
tv=TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.turn_off()
tv.show_status()
tv.turn_on()
tv.set_channel(2)
tv.show_status()

    

