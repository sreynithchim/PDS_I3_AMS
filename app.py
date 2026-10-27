# Problem 1

# name="sok dara"
# age=25
# major="Data Science"
# GPA=3.9
# print("====================================================")
# print("Name. :", name)
# print("Age.  :", age)
# print("Major :", major)
# print("GPA   :", GPA)
# print("====================================================")
# print(name,"->",type(name))
# print(age,"->",type(age))
# print(major,"->",type(major))
# print(GPA,"->",type(GPA))
# re_age="20"
# print(re_age,"->",type(re_age))

# Problem 2
# (a) Compute hours, minutes and seconds, then print the sentence shown below.

def transform_seconds(total_second):
    total_hour=total_second//3600
    hold=total_second%3600
    total_minute=hold//60
    total_second=hold%60
    return total_hour, total_minute, total_second
total_second=9875
total_hour, total_minute, total_second = transform_seconds(total_second)
print(f"{total_second} = {total_hour} hours {total_minute} minutes {total_second} seconds")

# (b) Check your answer: rebuild the total from the three parts and print whether it equals
# total_seconds.
check=total_hour*3600+total_minute*60+total_second
if check==9875:
    print("The calculation is correct.")
else:
    print("The calculation is incorrect.")
    
# (c) Test your code with 3600, 59 and 86399 seconds.

for test_seconds in [3600, 59, 86399]:
    total_hour, total_minute, total_second = transform_seconds(test_seconds)
    print(f"{test_seconds} seconds = {total_hour} hours {total_minute} minutes {total_second} seconds")
  


# Problem 3


# def celsius_to_fahrenheit(celcuis,round_to=1):
#     f=celcuis*9/5+32
#     return f


# def fahrenheit_to_celsius(fahrenheit,round_to=1):
#     c=(fahrenheit-32)*5/9
#     return c


# print(celsius_to_fahrenheit(67))
# print(fahrenheit_to_celsius(152.6))
# print("  °C |    °F")
# print("----------------")

# for c in range(0,101,20):
#     f = celsius_to_fahrenheit(c)
#     print(f"{c:4} | {celsius_to_fahrenheit(c):6}")
    

# print(f"Normal body temperature (98.6°F) in Celsius is: {fahrenheit_to_celsius(98.6):.1f}°C")

# f = celsius_to_fahrenheit(37)
# c=fahrenheit_to_celsius(f)
# print(f"37°C in Fahrenheit is: {f:.1f}°F and back to Celsius is: {c}°C")

# print(f"98.6 °F in Celsius is: {fahrenheit_to_celsius(98.6,round_to=3)}°C")





# Problem 4_A

# a=int("7") + 3.5
# b=str(10) * 3
# c=bool(""), bool(" ")
# d=int(3.99)
# e=float("1e3")
# f=int(True) + float("2.5")
# g=round(2.5), round(3.5)
# h=type(10 / 2)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)

# Problem 4_B
# def safe_int(text):
#     try:
#         return int(float(text.strip()))
#     except ValueError:
#         return None

# for sample in ["42"," -8 ","3.9","abc",""]:
#     print(repr(sample), "->", safe_int(sample))

# Problem 4_C

# for x in range(2):
#     x=int(input("Please input your Number : "))
#     print(x)










# Problem 5
# def letter_grade(score):
#     if score<0 or score>100:
#         return "Invalid score"
#     elif score>=97:
#         print("A+")
#     elif score>=90:
#         return "A"
#     elif score>=80:
#         return "B"
#     elif score>=70:
#         return "C"
#     elif score>=60:
#         return "D"
#     else:
#         print("F")
    
# print(letter_grade(99))
# print(letter_grade(90))
# print(letter_grade(85.5))
# print(letter_grade(72))
# print(letter_grade(60))
# print(letter_grade(59.9))
# print(letter_grade(-5))
# print(letter_grade(101))





# Problem 6

# def is_leap(year):
#     return (year%4==0 and year%100!=0) or (year%400==0)

# def day_in_month(month,year):
#     if month<1 or month>12:
#         return None
#     if month==2:
#         return 29 if is_leap(year) else 28
#     if month in [4,6,9,11]:
#         return 30
#     return 31

# for y in[1900,2000,2024,2026]:
#     print(y,"leap" if is_leap(y) else "not_leap")

# print("Feb 2024:", day_in_month(2, 2024), "|",
#       "Feb 2026:", day_in_month(2, 2026), "|",
#       "Apr:", day_in_month(4, 2026), "|",
#       "month 13:", day_in_month(13, 2026))
    
# count=0
# for y in range(2000,2101):
#     if is_leap(y):
#         count+=1
# print("Leap years from 2000 to 2100 is ",count)



# Problem 7

# def digit_sum(n):
#     total=0
#     while(n>0):
#         total+=n%10
#         n//=10
#     return total
    
# def reverse_number(n):
#     reversed_num=0
#     while(n>0):
#         reversed_num=reversed_num*10+n%10
#         n//=10
#     return reversed_num
    
# def is_palindrome(n):
#     return n==reverse_number(n)


# for number in (2026, 12321, 98789):
#     print("Number:", number)
#     print("Digit Sum:", digit_sum(number))
#     print("Reversed Number:", reverse_number(number))
#     print("Is Palindrome:", is_palindrome(number))
#     print("-----------------------------")
    
# count=0
# for number in range(10,1000):
#     if is_palindrome(number):
#         count+=1
# print("Total Palindrome numbers between 10 and 1000:", count)


# Problem 8

# def describe(*number, decimal=2,label="data"):
#     if not number:
#         return f"No {label} provided."
#     count=len(number)
#     smallest=min(number)
#     largest=max(number)
#     mean=round(sum(number)/count, decimal)
#     print(f"Count: {count}, Smallest: {smallest}, Largest: {largest}, Mean: {mean}")
#     return count, smallest, largest, mean


# def make_tag(text,**style):
#     attribute=""
#     for key, value in style.items():
#         attribute+=f' {key}="{value}"'
#     return f"<p{attribute}>{text}</p>"

# squre=lambda x:x**2
# is_adult=lambda age:age>=18

# describe(12, 7, 30, 4)
# describe(12, 7, 30, 4, decimal=3, label="Constants")
# describe()
# print(make_tag("Hello", style="color: red;",size=12))
# print(squre(5),is_adult(20), is_adult(15))


# Problem 9

# service_free=100
# vat=0.10
# RIEL_PER_USD = 4100

# def electricity_bill(kwh):
#     if kwh<0:
#         return None
#     tier1 = min(kwh, 50)                  # first 50 kWh
#     tier2 = min(max(kwh - 50, 0), 150)    # next 150 kWh
#     tier3 = max(kwh - 200, 0)
#     energy_cost = tier1 * 480 + tier2 * 610 + tier3 * 730
#     total = (energy_cost + service_free) * (1 + vat)
#     return round(total)

# for kwh in (0, 35, 50, 120, 200, 350):
#     bill = electricity_bill(kwh)
#     usd = bill / RIEL_PER_USD
#     print(f"{kwh:>3} kWh -> {bill:>9,} riel (≈ {usd:>6.2f} USD)")
    
# kwh = float(input("Enter your monthly consumption (kWh): "))
# bill = electricity_bill(kwh)

# if bill is None:
#     print("Invalid Value")
# else:
#     print(f"Your bill is {bill:,} riel (≈ {bill / RIEL_PER_USD:.2f} USD)")
    
    
    
    
    

# Problem 10

def is_prime(n):
    if n <2:
        return False
    d=2
    while d*d<=n:
        if n%d==0:
            return False
        d+=1
    return True


def goldbach(n):
    for p in range(2, n // 2 + 1):
        q = n - p
        if is_prime(p) and is_prime(q):
            return (p, q)
    return None


for n in range(2,50):
    if is_prime(n):
        print(n,end=" ")
        
print()
    
count=0
for n in range(2,100):
    if is_prime(n):
        count+=1
print("Total prime numbers between 2 and 100:", count)
        
for n in range(4, 31, 2):
    p,q=goldbach(n)
    print(f"{n} = {p} + {q}")
    
    
holds=True
for n in range(4,10000):
    if goldbach(n) is None:
        holds=False
        break

print("Goldbach holds for every even number from 4 to 10000:", holds)