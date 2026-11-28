
"""(a) Print a profile card exactly like the one below. The GPA must always show 2 decimals (hint:
f"{gpa:.2f}")."""
name="sok dara"
age=25
major="Data Science"
GPA=3.9
print("====================================================")
print("Name. :", name)
print("Age.  :", age)
print("Major :", major)
print(f"GPA   :{GPA:.2f}")


"""(b) Below the card, print every value followed by the name of its type, using type(value).__name__."""
print("====================================================")
print(name,"->",type(name))
print(age,"->",type(age))
print(major,"->",type(major))
print(GPA,"->",type(GPA))


"""(c) Re-assign age = "20" and print type(age) again. What does this tell you about dynamic typing?"""
"""Dynamic typing tell me about a variable name is not  tied to a fixed type. The value carries the type, 
and the variable is just a label pointing at it
So age can refer to an int one moment and a str the next, with no declaration or error."""
re_age="20"
print(re_age,"->",type(re_age))



