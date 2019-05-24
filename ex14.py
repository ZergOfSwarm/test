from sys import argv
script, user_name = argv
prompt = '> '

#print(f"Hi {user_name}, I'm the {script} script."A)
print("Hi {} I'm the {} script.".format(user_name, script))
print("I'd like to ask you a few questions.")
#print(f"Do you like me {user_name}?")
print("Di you like me {}".format(user_name))
likes = input(prompt)

#print(f"Where do you live {user_name}?")
print("Where do you live {}".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

#print(f"""
#Alright, so you said {likes} about liking me.
#You live in {lives}. Not sure where that is.
#And you have a {computer} computer. Nice.
#""")

print("""
Alright, so you said {} about liking me
You live in {}. Not sure where that is.
And you have a {} computer. Nice.
""".format(likes, lives, computer))
