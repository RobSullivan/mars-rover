from dataclasses import dataclass, field


@dataclass
class Surface:
    rows: int
    columns: int
    robots: list = field(default_factory=list)

    def add_robot(self, robot) -> None:
        if robot in self.robots:
            raise Exception("This robot is already on the surface")
        self.robots.append(robot)
