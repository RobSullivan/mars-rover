
## What is this?
A program that takes in commands and moves one or more robots around Mars.

## How to install this project

Create a virtual environment and activate it. I use pyenv.

```
pyenv virtualenv mars-rover
pyenv activate mars-rover
```

An editable installation of this project can be installed from the root directory with:

`pip install --editable .`

This will only install `pytest`.



## How to run the tests
Pytest was used for writing tests so all the tests can be run with the command:

`pytest .`

There's a functional test at `test/functional/test_app.py` in lieu of a cli.

## Modelling

`Surface` - a container that defines the boundaries for the robots to move around in.

`Gps` - the gps has the logic for moving about the surface.

`Step` - a container of coordinates, direction and orientation.

`Robot` - the rover. It has a gps from which it will get the `Steps` it needs to take to follow
the directions given to it.

## Assumptions
1. A robot doesn't need to know directly about the surface, it will use the gps
2. A robot occupies a coordinate so that no other robot can be at that coordinate at the same time
3. The robot "moves" by iterating over a list of steps. It doesn't need "move" on the surface. By this I mean the surface doesn't need a `matrix` property that is updated everytime a robot moves. Doing that
seemed to error prone.
4. A surface should know how many robots there are on the surface

## TODOs
- [ ] Add a cli so program can be run
- [ ] Test out adding another robot to the surface
- [ ] Add a check for surface capacity. The number of robots can't exceed the size of the surface