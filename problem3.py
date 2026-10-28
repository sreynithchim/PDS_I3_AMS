
def celsius_to_fahrenheit(celcuis,round_to=1):
    f=celcuis*9/5+32
    return round(f, round_to)

def fahrenheit_to_celsius(fahrenheit,round_to=1):
    c=(fahrenheit-32)*5/9
    return round(c, round_to)

"""(a) Use a for loop with range(0, 101, 20) to print the conversion table below."""
print(celsius_to_fahrenheit(67))
print(fahrenheit_to_celsius(152.6))
print("  °C |    °F")
print("----------------")
for c in range(0,101,20):
    f = celsius_to_fahrenheit(c)
    print(f"{c:4} | {celsius_to_fahrenheit(c):6}")
    
    
"""(b) Convert 98.6 °F (normal body temperature) to Celsius."""
print(f"Normal body temperature (98.6°F) in Celsius is: {fahrenheit_to_celsius(98.6):.1f}°C")


"""(c) Convert 37 °C to Fahrenheit and back again. Do you get 37.0? Yes , I got 37.0"""
f = celsius_to_fahrenheit(37)
c=fahrenheit_to_celsius(f)
print(f"37°C in Fahrenheit is: {f:.1f}°F and back to Celsius is: {c}°C")


"""(d) Call one function with round_to=3. Why is a default argument useful here?"""
""" A default argument is useful because most calls only need the common case (1 decimal place)"""
print(f"98.6 °F in Celsius is: {fahrenheit_to_celsius(98.6,round_to=3)}°C")

