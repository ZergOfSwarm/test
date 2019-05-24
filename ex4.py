my_name = 'Denis Khartskhaev'
my_age = 41 # i'm not lie
my_height = 175 # cm
my_weight = 78 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about {}".format(my_name))
print("He's {} inches tall".format(my_height))
print("He's {} pounds heavy".format(my_weight))
print("Actuallu that's not too heavy {} kg.".format(my_weight))
print("He's got {} eyes and {} hair.".format(my_eyes, my_hair))
print("His teeth are usually {} depending on the coffee." .format(my_teeth))

# this line is tricky, to get it exactly right
total = my_age + my_height + my_weight
#print("total {}".format(total))
print("if I add {}, {}, and {} I  get {}.".format(my_age, my_height, my_weight, total))
