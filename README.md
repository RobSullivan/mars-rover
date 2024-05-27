
## What is this?

## How to install this project

Create a virtual environment and activate it. I use pyenv.

An editable installation of this project can be installed from the root directory with:

`pip install --editable .`



## How to run the tests
Pytest was used for writing tests so all the tests can be run with the command:

`pytest .`

## Modelling

`Surface` - a container that defines the boundaries for the robots to move around in. 
`Gps` - the gps has the logic for moving about the surface.
`Step` - a container of coordinates, direction and orientation
`Robot` - the rover. It has a gps from which it will get the Steps it needs to take to follow
the directions given to it.
## Assumptions