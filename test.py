a = ['?', '?', '?', '?']
b = ['b', 'i', 'r', 'd']
c = ['1', '2', '3', '4']
d = []

"""-----------------------проверка совпадения------------------------------"""

leter_of_user = str(input('Ok, enter a leter: '))
match = 'No matches in the list!'
for i in  b:
    if i == leter_of_user:
        match = 'Such a letter is exist!'
print(match)

"""-----------------------замена '?' на совпадение------------------------------"""

for n, i in enumerate(b):
    if i == leter_of_user:
        a[n] = leter_of_user 
print (a)
