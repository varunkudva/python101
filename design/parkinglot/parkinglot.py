from enum import Enum

class SpotType(Enum):
    BIKE, CAR, VAN = 1, 2, 3


class SpotType(Enum):

class Spot(object):
    def __init__(self):
        self.id = 0
        self.type =

class Floor(object)
    """
    floor_num
    total_spots
    spot_pool = dict()
    add_spot(type)
    """

class ParkingLot(object):
    """
    Assumption: 1 floor, single entrance, exit
    name
    location
    add_entrance()
    add_exit()
    get_ticket()
    pay_ticket()
    """
    def __init__(self, name, location)
        self.name = name
        self.location = location
        self.spot_pool = dict # hashmap for free spots per pool type

    def add_spots(self, type, count):



    def get_ticket(self):


def main():
    my_lot = ParkingLot("VK_lot", "94560")







