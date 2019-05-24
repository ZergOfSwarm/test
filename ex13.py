# этот скрипт запускай так: python ex13.py First Second Third
''' When you declare like this, python will expect you
to pass in 4 arguments when you run python. the first one
is script, the the next 3 ones could be something else,
such as other text file, py file, etc.
In this example, you should run python like this:
python your-script.py First Second Third

Because First, Second and Third are not actually files,
python will treat them as strings
'''

from sys import argv
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
