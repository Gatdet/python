from television import Television
tv1 = Television()
def test_init():
    
    assert tv1.status==False
    assert tv1.channel==tv1.MIN_CHANNEL
    assert tv1.volume==tv1.MIN_VOLUME

def test_power():
    tv1.power()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 0"
    tv1.power()
    assert str(tv1)== f"Power = False, Channel = 0, Volume = 0"

def test_mute():
    tv1.power()
    tv1.volume_up()
    tv1.mute()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 0"

    tv1.mute()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 1"

    tv1.mute()
    tv1.power()
    assert str(tv1)== f"Power = False, Channel = 0, Volume = 0"

    tv1.mute()
    assert str(tv1)== f"Power = False, Channel = 0, Volume = 0"


def test_channel_up():
    tv1.channel_up
    assert str(tv1)== f"Power = False, Channel = 0, Volume = 0"
    tv1.power()
    tv1.channel_up()
    assert str(tv1)== f"Power = True, Channel = 1, Volume = 0"

    tv1.channel_up()
    tv1.channel_up()
    tv1.channel_up()
    assert str(tv1)== f"Power = True, Channel = 3, Volume = 0"

def test_channel_down():
    tv1.channel_down()
    tv1.channel_down()
    tv1.channel_down()
    tv1.power()
    tv1.channel_down()
    assert str(tv1)== f"Power = False, Channel = 0, Volume = 0"

    tv1.power()
    tv1.channel_down()
    tv1.channel_down()
    tv1.channel_down()
    tv1.channel_down()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 0"

def test_volume_up():
    tv1.power()
    tv1.volume_up()
    assert str(tv1)== f"Power = False, Channel = 0, Volume = 0"
   

    tv1.power()
    tv1.volume_up()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 2"

    tv1.mute()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 0"
    tv1.mute()
    tv1.volume_up()
    tv1.volume_up()
    tv1.volume_up()
    tv1.volume_up()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv1.power()
    assert str(tv1)== f"Power = False, Channel = 0, Volume = 2"
    tv1.power()
    tv1.volume_up()
    tv1.volume_up()
    tv1.volume_up()
    tv1.volume_down()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 1"
    tv1.mute()
    tv1.volume_down()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 1"
    tv1.volume_down()
    tv1.volume_down()
    tv1.volume_down()
    tv1.volume_down()
    assert str(tv1)== f"Power = True, Channel = 0, Volume = 0"
