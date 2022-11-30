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
    City = namedtuple('City','name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print("Tokio:", tokyo._asdict())
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo._fields)
    Coordinate = namedtuple('Coordinate', 'lat lon')
    delhi_data = ('Nelhi NCR', 'IN', 21.935, Coordinate(28.613889,77.208889))
    delhi = City._make(delhi_data)
    print(delhi._asdict())

