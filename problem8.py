"""(a) Write describe(*numbers, decimals=2, label="Data") that accepts any number of values,
prints their count, min, max and mean (rounded to decimals), and returns them as a tuple. With
no values it prints "<label>: no values" and returns None."""
def describe(*number, decimal=2,label="data"):
    if not number:
        return f"No {label} provided."
    count=len(number)
    smallest=min(number)
    largest=max(number)
    mean=round(sum(number)/count, decimal)
    print(f"Count: {count}, Smallest: {smallest}, Largest: {largest}, Mean: {mean}")
    return count, smallest, largest, mean


"""(b) Write make_tag(text, **style) that builds an HTML-like string from keyword arguments:
make_tag("Hello", color="red", size=14) returns <span color="red"
size="14">Hello</span>."""
def make_tag(text,**style):
    attribute=""
    for key, value in style.items():
        attribute+=f' {key}="{value}"'
    return f"<p{attribute}>{text}</p>"
print(make_tag("Hello", style="color: red;",size=12))


"""(c) Write two lambdas: square (returns x²) and is_adult (returns True when age ≥ 18)"""
squre=lambda x:x**2
is_adult=lambda age:age>=18
describe(12, 7, 30, 4)
describe(12, 7, 30, 4, decimal=3, label="Constants")
describe()
print(squre(5),is_adult(20), is_adult(15))

