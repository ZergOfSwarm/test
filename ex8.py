

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Проверка",
	"русского языка",
	"будет ли он отображаться",
	"корректро!?!?!"
	"TEST" # Этой строки не будет! 
))

print("""
There's something going on here.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
