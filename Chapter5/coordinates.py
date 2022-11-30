#!/usr/bin/env python3

import typing
from collections import namedtuple

class Coordinate:

    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon



if __name__ == '__main__':
    moscow = Coordinate(55.76, 37.62)

    Coordinate = namedtuple('Coordinate', 'lat lon')
    moscow = Coordinate(55.76, 37.62)
    # newer type typing.NamedTuple 
    print("Namedtupe:", moscow)
    print("*"*72)
    Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon',float)])
    moscow = Coordinate(55.76, 37.62)
    print("New namedtuple:", moscow)
    print("*"*72)
