# Part A
a=int("7") + 3.5
b=str(10) * 3
c=bool(""), bool(" ")
d=int(3.99)
e=float("1e3")
f=int(True) + float("2.5")
g=round(2.5), round(3.5)
h=type(10 / 2)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

"""int("7") + 3.5  expected output: 10.5"""
"""str(10) * 3  expected output: 30"""
"""bool(""), bool(" ") expected output: (False, True)"""
"""int(3.99) expected output: 3"""
"""float("1e3") expected output: 1e3"""
"""int(True) + float("2.5") expected output: 2.5"""
"""round(2.5), round(3.5) expected output: (2, 4)"""
"""type(10 / 2) expected output: 5"""


# Part B
def safe_int(text):
    try:
        return int(float(text.strip()))
    except ValueError:
        return None
for sample in ["42"," -8 ","3.9","abc",""]:
    print(repr(sample), "->", safe_int(sample))



# Part C
for x in range(2):
    x=int(input("Please input your Number : "))
    print(x)

