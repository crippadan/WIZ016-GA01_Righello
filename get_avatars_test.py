from utils import get_avatars

# a = get_avatars()

# print(a)

# import os

# print(os.listdir(os.path.join('Data','Rules')))
# print(os.listdir(os.path.join('Data','Hints','1')))

path = r"C:\Users\cripp\OneDrive\Desktop\WIZ016-GA01_Righello\Data\Hints\1\rer.txt"

with open(path, 'r') as file:
    line = file.read()

name = 'Daniele'

line = line.format(name=name)

print(line)