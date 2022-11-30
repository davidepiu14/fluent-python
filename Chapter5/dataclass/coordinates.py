#!/usr/bin/env python3


from dataclasses import dataclass


@dataclass(frozen=True) # When frozen=True the class will raise an exception if you try to assign a value to a field after the instance is initialized
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
