#!/usr/bin/env python3

from collections import namedtuple


class Coordinate:

    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon



if __name__ == '__main__':
    Coordinate = namedtuple('Coordinate', 'lat lon')
    moscow = Coordinate(55.756, 37.617)
    