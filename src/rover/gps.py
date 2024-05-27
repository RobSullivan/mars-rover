from dataclasses import dataclass

from rover import surface as rover_surface


@dataclass
class Gps:
    surface: rover_surface.Surface
