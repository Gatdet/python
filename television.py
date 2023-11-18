class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL =3

    def __init__(self, __status=False, __muted=False, __volume=MIN_VOLUME, __channel=MIN_VOLUME) -> None:
        
        """
        when an object is created it will have the status set to false, be muted, volume set to minimum, and have channel set to minimum volume
        all the variables will be private
        """
        
        self.status = __status
        self.muted = __muted
        self.volume = __volume
        self.channel = __channel
    
    def power(self) -> None:

        """
        Check if the status of the tv is true and if so set the status false
        else if the status is false set it true
        """
        if self.status==True:
            self.status=False
        else:
            self.status=True
    
    def mute(self) -> None:

        """
        Check if the status of the tv is true and if so:
            if the mute function is true set it false and increase volume by one
            else if the mute function is false set it to true and set volume to 0
        """
        if self.status:
            if self.muted==True:
                self.muted=False
                self.volume+=1
            else:
                self.muted=True
                self.volume=0
        
    def channel_up(self) -> None:
        """
        Check if the status of the tv is true and if so:
            if the channel is less than the max channel increase it by one
        """
        if self.status:
            if self.channel < self.MAX_CHANNEL:
                self.channel+=1
    
    def channel_down(self) -> None:
        """
        Check if the status of the tv is true and if so:
            if the channel is greater than the min channel decrease it by one
        """
        if self.status:
            if self.channel > self.MIN_CHANNEL:
                self.channel-=1

    def volume_up(self) -> None:
        """
        Check if the status of the tv is true and if so:
            if the muted variable is false turn it true
            if the volume is lower than the maximum volume, turn it up 1 value.
        """
        if self.status:
            if self.muted==True:
                self.volume+=1
            self.muted=False
            if self.volume < self.MAX_VOLUME:
                self.volume+=1
            

    def volume_down(self) -> None:
        """
        Check if the status of the tv is true and if so:
            if the muted variable is false turn it true
            if the volume is higher than the minumum volume, turn it down 1 value.
        
        """
        if self.status:
            if self.muted==True:
                self.volume-=1
            self.muted=False
            if self.volume > self.MIN_VOLUME:
                self.volume-=1
            self.volume = abs(self.volume)
           
            
        
    def __str__(self) -> str:

        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"

    
        