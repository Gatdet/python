class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL =3

    def __init__(self, __status=False, __muted=False, __volume=MIN_VOLUME, __channel=MIN_VOLUME) -> None:
        self.status = __status
        self.muted = __muted
        self.volume = __volume
        self.channel = __channel
    
    def power(self):
        if self.status==True:
            self.status=False
        else:
            self.status=True
    
    def mute(self):
        if self.status:
            if self.muted==True:
                self.muted=False
                self.volume+=1
            else:
                self.muted=True
                self.volume=0
        
    def channel_up(self):
        if self.status:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel+=1
    
    def channel_down(self):
        if self.status:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel-=1

    def volume_up(self):
        if self.status:
            if self.muted==True:
                self.volume+=1
            self.muted=False
            if self.volume < self.MAX_VOLUME:
                self.volume+=1
            

    def volume_down(self):
        if self.status:
            if self.muted==True:
                self.volume-=1
            self.muted=False
            if self.volume > self.MIN_VOLUME:
                self.volume-=1
            self.volume = abs(self.volume)
           
            
        
    def __str__(self):

        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"

    
        