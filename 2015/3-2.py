"""
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""

data = ""
houses = {}

with  open ( "3_input" ,  "r" )  as  file:
    data = file.read()

x_santa = 0
y_santa = 0

x_robot = 0
y_robot = 0

turn = "santa"

houses[(x_santa,y_santa)] = 1

for char in data:
    if char == '>':
        locals()["x_"+turn] +=1
    elif char == '<':
        locals()["x_"+turn] -=1
    elif char == '^':
        locals()["y_"+turn] +=1
    elif char == 'v':
        locals()["y_"+turn] -=1

    houses[(locals()["x_"+turn],locals()["y_"+turn])] = 1 

    turn = "santa" if turn == "robot" else "robot"

print(len(houses))
