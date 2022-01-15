class Device:
    count = 0
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name
        Device.count += 1
        # result = ping the devices
        if result:
            self.status = 'active'
        else:
            self.status = 'unknown'

class TV(Device):
    def turn_on(self):
        # connect the self.ip and turn on the tv
    def turn_off(self):
        # connect the self.ip and turn off the tv
class smart_tv(TV):
    def turn_on(self):
        # connect the self.ip to turn on the smart tv

